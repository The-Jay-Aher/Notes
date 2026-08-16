# 6 - High Availability and Scalability with ELB and ASG

## Quick Summary

High availability means an application stays usable even when part of the infrastructure fails. Scalability means an application can handle more or less load by changing capacity.

In AWS, two core services for EC2-based application design are:

- **Elastic Load Balancing (ELB):** Distributes traffic across targets.
- **Amazon EC2 Auto Scaling Groups (ASG):** Adds, removes, and replaces EC2 instances based on desired capacity, health, and scaling policies.

Common pattern:

```text
Users -> Route 53 -> Load Balancer -> Auto Scaling Group -> EC2 instances
```

## Why It Matters

Without load balancing and auto scaling:

- One unhealthy instance can break the application.
- Traffic spikes can overload fixed capacity.
- Manual instance replacement is slow.
- Deployments and maintenance create more downtime.

With ELB and ASG:

- Users get one stable entry point.
- Failed instances can be removed from traffic.
- New instances can be launched automatically.
- Applications can run across multiple Availability Zones.

## Core Concepts

| Concept | Meaning |
| --- | --- |
| Scalability | Ability to handle changing load. |
| Vertical scaling | Increase/decrease the size of one server. |
| Horizontal scaling | Increase/decrease the number of servers. |
| Elasticity | Automatically match capacity to demand. |
| High availability | Keep service running during component failure. |
| Fault tolerance | Continue operating even when failures happen. |
| Load balancer | Distributes traffic across targets. |
| Target group | Set of targets behind a load balancer listener/rule. |
| Auto Scaling Group | Manages a fleet of EC2 instances. |
| Health check | Determines whether a target or instance is healthy. |

## Scalability vs High Availability

| Topic | Main Question | Example |
| --- | --- | --- |
| Scalability | Can it handle more load? | Add more EC2 instances when CPU is high. |
| High availability | Can it survive failure? | Run instances in at least two Availability Zones. |
| Elasticity | Can capacity adjust automatically? | ASG scales out/in based on target tracking. |

They are related but not identical. A system can scale but still not be highly available if all capacity is in one Availability Zone.

## Vertical Scaling

Vertical scaling means changing the size of one machine.

Example:

```text
t3.micro -> t3.large -> m7i.2xlarge
```

Good for:

- Databases with limited horizontal scaling.
- Stateful systems.
- Quick capacity increase when architecture is simple.

Limits:

- Hardware size has a ceiling.
- Often needs restart or replacement.
- One big instance can still be a single point of failure.
- Cost can rise quickly.

AWS examples:

- EC2 instance size changes.
- RDS instance class changes.
- ElastiCache node type changes.

## Horizontal Scaling

Horizontal scaling means adding more machines.

Example:

```text
2 app instances -> 4 app instances -> 8 app instances
```

Good for:

- Stateless web applications.
- API servers.
- Worker fleets.
- Containerized applications.

Requirements:

- Load balancer or queue-based distribution.
- Stateless application design, or externalized state.
- Shared database/cache/storage where needed.
- Deployment strategy that handles multiple versions safely.

## High Availability Design

Basic HA EC2 design:

```text
Availability Zone A: app instance 1
Availability Zone B: app instance 2
Load Balancer spans both AZs
Auto Scaling Group spans both AZs
```

Important:

- Use at least two Availability Zones for production-facing workloads.
- Put load balancer subnets in multiple AZs.
- Put ASG subnets in multiple AZs.
- Keep application state outside individual instances.
- Use health checks to remove broken targets.

## Elastic Load Balancing Overview

Elastic Load Balancing is AWS's managed load balancing service.

It helps with:

- Traffic distribution.
- Health checks.
- TLS termination.
- One DNS endpoint for users.
- Multi-AZ application entry points.
- Integration with Auto Scaling, ECS, ACM, CloudWatch, Route 53, WAF, and Global Accelerator.

Why use managed ELB instead of self-managed HAProxy/Nginx?

- AWS manages availability and maintenance of the load balancer service.
- It integrates directly with AWS target groups and health checks.
- It scales the load balancer infrastructure.
- It reduces operational work.

Self-managed load balancers may still be used for special requirements, but they add patching, scaling, HA, and monitoring responsibility.

## ELB Types

AWS supports four load balancer families.

| Load Balancer | Layer | Protocols / Use |
| --- | --- | --- |
| Application Load Balancer (ALB) | Layer 7 | HTTP, HTTPS, WebSocket, HTTP/2/gRPC scenarios. |
| Network Load Balancer (NLB) | Layer 4 | TCP, UDP, TLS, very high performance, static IP per AZ. |
| Gateway Load Balancer (GWLB) | Layer 3/4 appliance pattern | Third-party virtual appliances such as firewalls and inspection tools. |
| Classic Load Balancer (CLB) | Legacy | Older generation; prefer ALB/NLB for new designs. |

For new solutions, choose ALB, NLB, or GWLB unless you are maintaining a legacy CLB design.

## Application Load Balancer

ALB is best for HTTP/HTTPS applications.

Use ALB when you need:

- Host-based routing.
- Path-based routing.
- Header/query based routing.
- HTTP to HTTPS redirects.
- TLS termination with AWS Certificate Manager.
- AWS WAF integration.
- WebSocket support.
- Container or microservice routing.
- Lambda targets for HTTP-style requests.

Example routing:

```text
app.example.com/api  -> API target group
app.example.com/web  -> web target group
admin.example.com    -> admin target group
```

### ALB Components

| Component | Purpose |
| --- | --- |
| Listener | Checks for traffic on a port/protocol such as HTTPS 443. |
| Rule | Matches request conditions and forwards/redirects/responds. |
| Target group | Group of targets such as instances, IPs, Lambda, or ALB targets in supported cases. |
| Health check | Verifies target health. |

### ALB Target Types

| Target Type | Use |
| --- | --- |
| Instance | Targets EC2 instances by instance ID. |
| IP | Targets private IP addresses, useful for containers or on-prem via private connectivity. |
| Lambda | Invokes Lambda functions through ALB. |

### ALB Client IP Headers

Application targets do not see the load balancer as the same as direct client access.

Common headers:

| Header | Meaning |
| --- | --- |
| `X-Forwarded-For` | Original client IP chain. |
| `X-Forwarded-Port` | Original destination port. |
| `X-Forwarded-Proto` | Original protocol, such as `http` or `https`. |

Applications should use these carefully and only trust them when they come from the expected load balancer/proxy path.

## Network Load Balancer

NLB is best for high-performance Layer 4 traffic.

Use NLB when you need:

- TCP or UDP load balancing.
- TLS pass-through or TLS listener behavior.
- Very high throughput and low latency.
- Static IP addresses per enabled Availability Zone.
- Elastic IP attachment for allow-listing.
- Source IP preservation depending on target type/configuration.
- ALB behind NLB for static-IP plus Layer 7 routing patterns.

Common use cases:

- Non-HTTP protocols.
- High-throughput TCP services.
- PrivateLink endpoint services.
- Static IP requirements.

## Gateway Load Balancer

GWLB is used for virtual network appliances.

Use it for:

- Firewalls.
- Intrusion detection/prevention systems.
- Deep packet inspection.
- Traffic inspection appliances.

Mental model:

```text
Traffic source -> Gateway Load Balancer Endpoint -> Gateway Load Balancer -> appliance fleet
```

Do not choose GWLB for normal web application routing. Choose ALB or NLB instead.

## Health Checks

Health checks decide whether targets receive traffic.

ALB health checks commonly use:

- Protocol: HTTP or HTTPS.
- Path: `/health`, `/ready`, or another endpoint.
- Expected success codes.
- Interval, timeout, healthy threshold, unhealthy threshold.

NLB health checks can use TCP, HTTP, or HTTPS depending on configuration.

Good health endpoint rules:

- Fast response.
- Does not require user authentication.
- Checks the app process and critical dependencies carefully.
- Does not fail because of optional dependencies.
- Returns a clear success status only when the target should receive traffic.

Common problem:

```text
App works on port 8080
Target group checks port 80
Result: target unhealthy
```

## Cross-Zone Load Balancing

Cross-zone load balancing lets load balancer nodes distribute traffic across targets in all enabled Availability Zones.

Important design point:

- If cross-zone is disabled, each zone should have enough healthy targets for the traffic landing in that zone.
- With NLB and GWLB, cross-zone load balancing has historically had different defaults/cost behavior than ALB. Check current AWS docs before exam or production design.

## Internal vs Internet-Facing Load Balancers

| Scheme | Use |
| --- | --- |
| Internet-facing | Public entry point for users on the internet. |
| Internal | Private entry point inside a VPC or connected network. |

Use internal load balancers for:

- Private APIs.
- Internal microservices.
- Admin tools.
- Back-office systems.

## Auto Scaling Group Overview

An Auto Scaling Group maintains EC2 instance capacity.

It controls:

- Minimum capacity.
- Desired capacity.
- Maximum capacity.
- Which subnets/AZs instances can launch into.
- Launch template or launch configuration.
- Health check behavior.
- Scaling policies.
- Termination policies.

Basic capacity fields:

| Field | Meaning |
| --- | --- |
| Minimum | Lowest number of instances ASG should keep. |
| Desired | Current intended number of instances. |
| Maximum | Highest number of instances ASG can scale to. |

Example:

```text
min = 2
desired = 4
max = 10
```

## Launch Templates

A launch template defines how new EC2 instances are created.

It can include:

- AMI ID.
- Instance type.
- Key pair.
- Security groups.
- IAM instance profile.
- User data.
- EBS volume configuration.
- Purchase options.

Best practice: use launch templates instead of legacy launch configurations for new designs.

## ASG Health Checks

ASG can replace unhealthy instances.

Health check sources:

- EC2 status checks.
- Elastic Load Balancing health checks, if enabled/attached.
- Custom health status set by automation.

Health check grace period:

- Gives a new instance time to boot and start the application before health checks cause replacement.
- Set it long enough for user data, package install, app startup, and registration.

## Scaling Policies

| Policy Type | Use |
| --- | --- |
| Target tracking | Keep a metric near a target, such as average CPU 50%. |
| Step scaling | Add/remove capacity in steps based on alarm thresholds. |
| Simple scaling | Older/simple policy with cooldown behavior. |
| Scheduled scaling | Change capacity at known times. |
| Predictive scaling | Forecasts demand from historical patterns. |

Target tracking is often the easiest default.

Example:

```text
Keep average ASG CPU utilization near 50%
If CPU rises, scale out
If CPU falls, scale in
```

## Scaling Metrics

Useful metrics:

- CPUUtilization.
- Request count per target for ALB.
- Target response time.
- Queue depth per instance for worker fleets.
- Custom CloudWatch metrics.

Choose metrics that reflect real bottlenecks.

Bad metric example:

```text
Scale API servers only on CPU when the real bottleneck is database connections.
```

Better:

- Use request count per target for web traffic.
- Use queue depth per worker for asynchronous workers.
- Use custom business/load metrics where needed.

## Lifecycle Hooks

Lifecycle hooks pause instance launch or termination so automation can run.

Use cases:

- Install or register software before entering service.
- Drain connections before termination.
- Upload logs before shutdown.
- Deregister from external systems.

States:

- Launching.
- Terminating.

## Instance Refresh

Instance refresh replaces instances in an ASG gradually, commonly after changing launch template version or AMI.

Use for:

- Rolling out a new AMI.
- Updating instance configuration.
- Replacing old instances without manually terminating them.

Watch:

- Health checks.
- Minimum healthy percentage.
- Warmup time.
- Rollback behavior if configured.

## ELB + ASG Integration

Best-practice EC2 web app pattern:

```text
Route 53 alias
  -> ALB
      -> target group
          -> Auto Scaling Group instances across AZs
```

Flow:

1. User resolves DNS to the load balancer.
2. Load balancer receives request.
3. Listener rule selects target group.
4. Target group forwards to a healthy instance.
5. ASG replaces unhealthy instances and adjusts capacity.

## Security Groups

Common rule pattern:

```text
ALB security group:
  inbound 443 from internet or allowed CIDRs
  outbound app port to EC2 security group

EC2 app security group:
  inbound app port from ALB security group only
  outbound required dependencies
```

Avoid allowing direct internet access to app instances unless required.

## Benefits

- Better availability across Availability Zones.
- Automatic unhealthy instance replacement.
- Managed traffic distribution.
- Easier rolling deployments and instance refreshes.
- Supports least-privilege network access through security group chaining.
- Can scale capacity based on demand.

## Drawbacks / Limitations

- Load balancers add cost.
- Bad health checks can remove healthy capacity or keep broken targets in rotation.
- ASG scale-in can terminate instances that still have work unless lifecycle/draining is handled.
- Scaling metrics can lag behind real demand.
- Stateful applications need externalized state before horizontal scaling works well.
- Load balancer choice matters; ALB, NLB, and GWLB solve different problems.

## Hidden Details / Caveats

- ELB DNS names are stable, but underlying IPs can change except for NLB static IP per AZ patterns.
- ALB works at HTTP layer and can inspect host/path/header/query conditions.
- NLB works at transport layer and is better for non-HTTP/static-IP/high-throughput cases.
- A target can be unhealthy because of security group rules, wrong port, wrong path, slow startup, bad response code, or app dependency failure.
- ASG launch template changes do not automatically replace existing instances unless you trigger a deployment/instance refresh or scale events replace them.
- Desired capacity is not "maximum"; ASG can scale between min and max.
- Cross-zone behavior and pricing/defaults can differ by load balancer type, so check current AWS docs before production design.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Using one EC2 instance in one AZ | Use ASG across multiple AZs behind a load balancer. |
| Exposing app instances directly | Put ALB/NLB in front and restrict instance security group to LB source. |
| Health check path requires login | Use a simple unauthenticated health endpoint. |
| Wrong target port | Match target group port/protocol to app listener. |
| Scaling on weak metric | Use request count, queue depth, or app-specific metrics where CPU is not enough. |
| Updating launch template and expecting instant replacement | Use instance refresh or deployment process. |
| Choosing ALB for raw TCP/UDP | Use NLB. |
| Choosing NLB for path-based HTTP routing | Use ALB. |

## Troubleshooting

### Target Is Unhealthy

Check:

- Target group health reason.
- Instance security group allows health check from load balancer.
- App listens on target port.
- Health check path returns expected status.
- Network ACLs and route tables.
- Instance boot/user-data logs.

Commands:

```bash
aws elbv2 describe-target-health --target-group-arn <target-group-arn>
aws autoscaling describe-auto-scaling-groups --auto-scaling-group-names <asg-name>
```

### ASG Does Not Scale Out

Check:

- Desired/max capacity.
- Scaling policy and CloudWatch alarm.
- Metric data exists.
- Launch template is valid.
- Subnet capacity.
- Service quotas.
- IAM permissions.

### New Instances Launch But App Fails

Check:

- User data logs.
- Security group egress.
- IAM instance profile.
- App config/secrets.
- AMI contents.
- Health check grace period.

## Interview Notes

- ALB is Layer 7 and supports host/path/header/query routing.
- NLB is Layer 4 and supports TCP/UDP/TLS, high performance, and static IP per AZ.
- GWLB is for third-party network appliances.
- Classic Load Balancer is legacy.
- ASG maintains min/desired/max EC2 capacity.
- Launch templates define instance configuration.
- Target tracking scaling keeps a metric near a target.
- Health checks remove broken targets from load balancer traffic and can trigger ASG replacement.
- Multi-AZ design is central to high availability.

## Related Topics

- [EC2 Fundamentals](3%20-%20EC2%20Fundamentals.md)
- [EC2 Instance Storage](5%20-%20EC2%20Instance%20Storage.md)
- [AWS Cloud Practitioner - Storage, Networking and Database](../aws-cloud-practitioner/2%20-%20Storage,%20Networking%20and%20Database.md)
- [Networking Fundamentals](../../shared-foundations/networking/1%20-%20Fundamentals%20of%20Networking.md)

## Official References

- Elastic Load Balancing documentation: <https://docs.aws.amazon.com/elasticloadbalancing/>
- Application Load Balancer documentation: <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html>
- ELB health checks: <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html>
- EC2 Auto Scaling groups: <https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html>
- Auto Scaling health checks: <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html>

## Further Exploration — Remaining Knowledge Gaps

The following topics deliberately go beyond the scope of this AWS Solutions Architect Associate chapter. Use this as a future research backlog after mastering the high-availability, load-balancing, and Auto Scaling foundations above.

### High Availability and Distributed-Systems Foundations

- Availability, reliability, durability, and resilience.
- Fault domains and failure isolation.
- Availability Zone independence assumptions.
- Regional versus zonal failure models.
- Control-plane versus data-plane failures.
- Partial failures in distributed systems.
- Correlated failures and common-mode failures.
- Failure detection and false positives.
- Heartbeats, leases, and timeouts.
- Recovery time objective (RTO).
- Recovery point objective (RPO).
- Service-level indicators (SLIs).
- Service-level objectives (SLOs).
- Error budgets.
- Mean time between failures (MTBF).
- Mean time to recovery (MTTR).
- Redundancy models: active-active and active-passive.
- N+1, N+2, and overprovisioning strategies.
- Graceful degradation.
- Load shedding.
- Backpressure.
- Bulkheads and fault containment.
- Circuit breakers.
- Retry storms and exponential backoff.
- Jittered retries.
- Idempotency during retries.
- Thundering-herd prevention.
- Queue-based load leveling.
- Cell-based architecture.
- Shuffle sharding.
- Multi-Region active-active architecture.
- Multi-Region active-passive architecture.
- Disaster-recovery testing.

### Networking, DNS, and Protocol Internals

- OSI model and TCP/IP model.
- Layer 4 versus Layer 7 load balancing.
- TCP three-way handshake.
- TCP connection state and teardown.
- TCP retransmission and congestion control.
- TCP keepalive.
- UDP behavior and failure semantics.
- TLS handshake.
- TLS session resumption.
- Server Name Indication (SNI).
- Application-Layer Protocol Negotiation (ALPN).
- HTTP/1.1 connection reuse.
- HTTP/2 streams and multiplexing.
- HTTP/3 and QUIC.
- WebSocket upgrade and persistent connections.
- gRPC over HTTP/2.
- DNS resolution and caching.
- DNS TTL during failover.
- Route 53 alias records.
- Route 53 routing policies.
- Route 53 health checks.
- Split-horizon DNS.
- Public versus private hosted zones.
- Anycast networking.
- Static, dynamic, and ephemeral IP addresses.
- Elastic network interfaces.
- Security-group statefulness.
- Network ACL statelessness.
- Ephemeral client ports.
- Source network address translation (SNAT).
- Proxy Protocol versions 1 and 2.
- `X-Forwarded-For` trust boundaries.
- `X-Forwarded-Proto` and `X-Forwarded-Port`.
- Client IP preservation.
- Connection tracking.
- Idle timeouts.
- Path maximum transmission unit discovery.
- Fragmentation and MTU mismatches.

### Application Load Balancer Deep Dive

- ALB nodes and Availability Zone mappings.
- ALB listener architecture.
- Listener rule priority evaluation.
- Default listener actions.
- Forward actions.
- Redirect actions.
- Fixed-response actions.
- Host-header routing.
- Path-pattern routing.
- HTTP-header routing.
- HTTP-request-method routing.
- Query-string routing.
- Source-IP routing.
- Weighted target groups.
- Target-group stickiness.
- Load-balancer-generated application cookies.
- Application-generated cookie stickiness.
- Slow-start mode.
- Least outstanding requests routing.
- Round-robin routing.
- ALB rule transforms.
- URL rewrite transforms.
- Host-header rewrite transforms.
- HTTP header modification.
- HTTP desync mitigation modes.
- Invalid-header-field handling.
- Preserve-host-header behavior.
- Drop-invalid-header-fields behavior.
- ALB HTTP/2 configuration.
- ALB gRPC support.
- ALB WebSocket support.
- ALB Lambda targets.
- ALB IP targets.
- ALB instance targets.
- ALB target registration across VPCs.
- ALB target registration for on-premises IPs.
- ALB authentication with Amazon Cognito.
- ALB authentication with OpenID Connect.
- ALB mutual TLS.
- Trust stores and certificate revocation lists.
- ALB TLS security policies.
- Multiple TLS certificates with SNI.
- ALB certificate discovery and renewal.
- ALB access logs.
- ALB connection logs.
- ALB request tracing.
- ALB zonal shift.
- ALB minimum load-balancer capacity.
- ALB capacity-unit reservation.
- ALB resource map.
- ALB deletion protection.
- ALB IPv4, dualstack, and IPv6 modes.
- ALB cross-zone load balancing behavior.
- ALB DNS failover behavior.
- ALB fail-open behavior when all targets are unhealthy.
- ALB quotas and rule-evaluation limits.

### Network Load Balancer Deep Dive

- NLB connection-flow hashing.
- NLB flow stickiness.
- NLB static IP addresses per Availability Zone.
- Elastic IP addresses with internet-facing NLBs.
- NLB TCP listeners.
- NLB TLS listeners.
- NLB UDP listeners.
- NLB TCP_UDP listeners.
- NLB TLS termination.
- NLB TLS pass-through.
- NLB TLS security policies.
- NLB mutual TLS pass-through.
- NLB client IP preservation.
- NLB Proxy Protocol v2.
- NLB source-IP affinity for UDP.
- NLB security groups.
- NLB target security-group referencing.
- NLB IP targets.
- NLB instance targets.
- ALB as an NLB target.
- NLB cross-zone load balancing.
- NLB zonal shift.
- NLB DNS zonal affinity.
- NLB zonal DNS names.
- NLB unhealthy-target connection termination.
- NLB connection draining.
- NLB passive and active health checks.
- NLB fail-open behavior.
- NLB PrivateLink endpoint services.
- NLB with AWS Global Accelerator.
- NLB with hybrid and on-premises targets.
- NLB access and TLS connection logs.
- NLB capacity units.
- NLB capacity reservation.
- NLB quotas and port-exhaustion limits.
- NLB IPv6 and dualstack behavior.

### Gateway Load Balancer and Network Appliances

- Gateway Load Balancer architecture.
- Gateway Load Balancer endpoints.
- AWS PrivateLink for GWLB.
- GENEVE encapsulation.
- Transparent bump-in-the-wire appliances.
- Centralized inspection VPCs.
- Distributed inspection architectures.
- North-south traffic inspection.
- East-west traffic inspection.
- Ingress routing.
- Appliance VPC route-table design.
- Symmetric routing requirements.
- Appliance stickiness.
- Flow hashing and appliance state.
- Stateful firewall scaling.
- Intrusion detection systems.
- Intrusion prevention systems.
- Deep packet inspection.
- Secure web gateways.
- Third-party virtual appliances.
- Appliance health checks.
- Appliance Auto Scaling.
- Multi-AZ appliance failure handling.
- GWLB cross-zone load balancing.
- GWLB endpoint service permissions.
- GWLB observability and flow diagnosis.
- GWLB quotas and pricing.

### Classic Load Balancer and Migration

- Classic Load Balancer architecture.
- Classic Load Balancer listeners.
- Classic Load Balancer health checks.
- EC2-Classic historical networking model.
- Classic Load Balancer feature limitations.
- Classic Load Balancer security policies.
- Classic Load Balancer stickiness.
- Classic Load Balancer access logs.
- Classic Load Balancer migration assessment.
- Classic Load Balancer to ALB migration.
- Classic Load Balancer to NLB migration.
- `aws elbv2` versus legacy `aws elb` APIs.

### Target Groups, Health Checks, and Target Lifecycle

- Target-group protocol and protocol-version selection.
- Target-group port overrides.
- Health-check protocol selection.
- Health-check interval and timeout.
- Healthy and unhealthy thresholds.
- Health-check matcher codes.
- HTTP health endpoint design.
- gRPC health-check codes.
- Deep versus shallow health checks.
- Liveness versus readiness.
- Dependency-aware health checks.
- Health-check amplification.
- Flapping-target prevention.
- Target registration lifecycle.
- Initial, healthy, unhealthy, draining, unused, and unavailable states.
- Deregistration delay.
- Connection draining.
- Unhealthy-target connection termination.
- Target warm-up and slow start.
- Target-group attributes.
- Target-group cross-zone overrides.
- Target-group failover thresholds.
- Target-group DNS failover thresholds.
- Target-group routing thresholds.
- Target Administrative Override states.
- Multi-port target registration.
- Target-group sharing boundaries.
- Target-group quotas.
- Health-check reason codes.
- Fail-open versus fail-closed behavior.
- Health checks for long-starting applications.
- Health checks during rolling deployments.

### TLS, Identity, and Load-Balancer Security

- AWS Certificate Manager certificate lifecycle.
- Public and private certificates.
- ACM certificate validation.
- Certificate renewal.
- Certificate rotation without downtime.
- Multiple certificates and SNI selection.
- TLS cipher suites.
- TLS protocol versions.
- Forward secrecy.
- FIPS security policies.
- Front-end versus back-end encryption.
- End-to-end TLS.
- TLS re-encryption to targets.
- Mutual TLS passthrough and verification modes.
- Client-certificate trust stores.
- Certificate revocation lists.
- OIDC authorization code flow.
- Cognito user-pool authentication.
- Authentication cookies and session timeout.
- AWS WAF integration with ALB.
- Web ACL rule evaluation.
- Rate-based WAF rules.
- AWS Shield Standard and Shield Advanced.
- Distributed denial-of-service protection.
- Security-group chaining.
- Prefix lists and source restrictions.
- Listener-rule security boundaries.
- Header spoofing and trusted proxy chains.
- Desync and request-smuggling defenses.
- Host-header attacks.
- TLS policy compliance.
- Access-log protection and retention.
- Least-privilege IAM for ELB administration.
- Service-linked roles for Elastic Load Balancing.

### Auto Scaling Group Internals and Lifecycle

- Auto Scaling group control loop.
- Minimum, desired, and maximum capacity semantics.
- Desired capacity units.
- Instance lifecycle states.
- Pending and `Pending:Wait` states.
- In-service state.
- Standby state.
- Terminating and `Terminating:Wait` states.
- Detaching and entering standby.
- Instance attachment and detachment.
- Replace unhealthy process.
- AZ rebalancing process.
- Availability Zone distribution strategies.
- Balanced best effort behavior.
- Balanced only behavior.
- Impaired Availability Zone handling.
- Auto Scaling group suspended processes.
- Administrative suspension.
- Health-check grace period.
- Default instance warmup.
- Scaling cooldowns.
- Lifecycle hooks.
- Lifecycle-hook heartbeats.
- Lifecycle-hook timeouts and default results.
- EventBridge events for lifecycle actions.
- Lifecycle hooks with SQS and SNS.
- Lifecycle hooks with Lambda and Systems Manager.
- Scale-in protection.
- Custom termination policies.
- Default termination-policy evaluation.
- Availability Zone balance during termination.
- Instance maintenance policies.
- Maximum and minimum healthy percentages.
- Instance refresh checkpoints.
- Instance refresh bake time.
- Instance refresh skip matching.
- Instance refresh auto rollback.
- Instance refresh CloudWatch alarm integration.
- Instance refresh failure states.
- Standby capacity and billing.
- Maximum instance lifetime.
- Instance refresh after launch-template changes.

### Scaling Policies and Control Behavior

- Target tracking scaling policies.
- Predefined target-tracking metrics.
- Custom target-tracking metrics.
- Metric math for target tracking.
- Step scaling policies.
- Simple scaling policies.
- Scheduled scaling.
- Predictive scaling.
- Predictive scaling forecast-only mode.
- Predictive scaling forecast-and-scale mode.
- Predictive scaling scheduling buffer.
- Predictive scaling maximum-capacity behavior.
- Dynamic and predictive scaling interaction.
- Multiple scaling-policy arbitration.
- Scale-out and scale-in asymmetry.
- High-resolution CloudWatch metrics.
- One-minute versus five-minute EC2 metrics.
- CPU utilization as a scaling metric.
- ALB request count per target.
- Queue depth per instance.
- Concurrency-based scaling.
- Latency-based scaling.
- Business-metric scaling.
- Metric proportionality requirements.
- Metric aggregation dimensions.
- Missing metric data.
- CloudWatch alarm evaluation periods.
- Datapoints to alarm.
- Alarm state transitions.
- Warmup effects on aggregated metrics.
- Cooldown and warmup differences.
- Scaling oscillation and hysteresis.
- Scaling overshoot and undershoot.
- Delayed feedback loops.
- Long instance-bootstrap times.
- Capacity buffers and headroom.
- Scale-to-zero alternatives.
- Scaling-policy testing and simulation.
- Scaling activity history analysis.

### Mixed Instances, Spot, and Capacity Procurement

- Mixed instances policies.
- On-Demand base capacity.
- On-Demand percentage above base capacity.
- Instance type overrides.
- Attribute-based instance type selection.
- Instance weighting.
- Desired capacity type: instances, vCPU, and memory.
- On-Demand allocation strategies.
- Spot allocation strategies.
- Price-capacity-optimized allocation.
- Capacity-optimized allocation.
- Capacity-optimized-prioritized allocation.
- Lowest-price allocation risks.
- Spot capacity pools.
- Spot interruption notices.
- EC2 instance rebalance recommendations.
- Auto Scaling Capacity Rebalancing.
- Temporary desired-capacity increase during rebalancing.
- Graceful Spot interruption handling.
- EC2 Auto Scaling with Capacity Reservations.
- Capacity Reservation groups.
- On-Demand Capacity Reservations.
- Capacity Blocks for ML.
- Regional EC2 capacity shortages.
- Instance-type flexibility.
- Availability Zone flexibility.
- Diversifying Spot capacity.
- Base capacity for critical workloads.
- Cost-versus-interruption tradeoffs.
- Mixed-instance performance normalization.

### Warm Pools and Fast Scale-Out

- Auto Scaling warm pools.
- Running warm-pool instances.
- Stopped warm-pool instances.
- Hibernated warm-pool instances.
- Minimum warm-pool size.
- Maximum prepared capacity.
- Warm-pool lifecycle hooks.
- Warm-pool instance reuse on scale-in.
- Warm-pool cost modelling.
- EBS charges for stopped warm instances.
- Hibernation prerequisites.
- Warm-pool limitations with Spot Instances.
- Warm-pool limitations with instance weighting.
- ECS registration with warm pools.
- Application pre-initialization.
- AMI baking versus runtime bootstrap.
- Snapshot-based application startup.
- Lazy loading during instance warmup.

### Launch Templates, Images, and Bootstrap Engineering

- Launch template versions.
- Default versus latest launch-template version.
- Launch template inheritance and overrides.
- Launch templates with mixed instances policies.
- AMI lifecycle management.
- EC2 Image Builder.
- Golden AMI pipelines.
- Immutable infrastructure.
- User-data execution lifecycle.
- Cloud-init stages and logs.
- Idempotent bootstrap scripts.
- Bootstrap failure reporting.
- Secrets retrieval during bootstrap.
- IAM instance profiles.
- Systems Manager Parameter Store integration.
- Secrets Manager integration.
- CloudFormation helper scripts.
- `cfn-init` and `cfn-signal`.
- Auto Scaling creation policies.
- Auto Scaling update policies.
- Bootstrap dependency failure.
- Package-repository availability.
- Configuration drift.
- AMI vulnerability scanning.
- AMI deprecation and deregistration.
- EBS snapshot lifecycle.
- Instance metadata service version 2.
- Metadata hop limits.
- User-data secret-exposure risks.
- EC2 detailed monitoring.
- Termination protection versus scale-in protection.

### Deployment and Traffic-Shifting Strategies

- In-place deployments.
- Rolling deployments.
- Immutable deployments.
- Blue/green deployments.
- Canary deployments.
- Linear traffic shifting.
- All-at-once deployments.
- Weighted target-group deployments.
- DNS-weighted deployments.
- Separate-ALB blue/green deployments.
- CodeDeploy with ALB and Auto Scaling.
- CodeDeploy lifecycle hooks.
- Deployment health alarms.
- Automatic rollback.
- Connection draining during deployments.
- Long-lived connection migration.
- WebSocket deployment behavior.
- Database compatibility during rolling deployments.
- Backward-compatible API and schema changes.
- Instance refresh versus CodeDeploy.
- Instance refresh checkpoint validation.
- Bake-time selection.
- Launch-before-terminate replacement.
- Terminate-before-launch replacement.
- Capacity surge during deployment.
- Zero-downtime deployment assumptions.
- Deployment rollback testing.

### Observability, Logging, and Troubleshooting

- ELB CloudWatch metric namespaces.
- Request count and new connection count.
- Active connection count.
- Target response time.
- Target connection error count.
- HTTP 4xx and 5xx attribution.
- ELB-generated versus target-generated errors.
- Rejected connection count.
- Processed bytes.
- Healthy and unhealthy host counts.
- Consumed LCU and NLCU metrics.
- Reserved capacity metrics.
- ALB access-log schema.
- NLB access-log schema.
- ALB connection-log schema.
- S3 access-log bucket policies.
- Log delivery delays.
- Athena queries for ELB logs.
- CloudWatch Logs ingestion pipelines.
- OpenTelemetry trace propagation.
- `X-Amzn-Trace-Id`.
- AWS X-Ray integration patterns.
- VPC Flow Logs.
- Reachability Analyzer.
- Traffic Mirroring.
- CloudTrail ELB and Auto Scaling events.
- EventBridge Auto Scaling events.
- Auto Scaling activity history.
- Target health reason codes.
- HTTP 502 diagnosis.
- HTTP 503 diagnosis.
- HTTP 504 diagnosis.
- TLS handshake failures.
- Certificate mismatch diagnosis.
- Intermittent unhealthy-target diagnosis.
- Cross-zone traffic imbalance.
- Uneven target utilization.
- Sticky-session imbalance.
- Port exhaustion.
- Connection-reset diagnosis.
- Idle-timeout mismatch.
- Scale-out launch failure diagnosis.
- Insufficient instance capacity errors.
- EC2 service-quota failures.
- Bootstrap and cloud-init log analysis.
- Scaling-policy oscillation diagnosis.

### Infrastructure as Code and Automation

- CloudFormation ELBv2 resources.
- CloudFormation Auto Scaling resources.
- CloudFormation launch templates.
- CloudFormation target groups and listener rules.
- CloudFormation creation and update policies.
- CloudFormation rolling-update behavior.
- AWS CDK load-balancer constructs.
- AWS CDK Auto Scaling constructs.
- Terraform `aws_lb` resources.
- Terraform target-group and listener resources.
- Terraform Auto Scaling group resources.
- Terraform lifecycle and replacement behavior.
- Pulumi load-balancer and Auto Scaling resources.
- AWS CLI `elbv2` command family.
- AWS CLI `autoscaling` command family.
- ELBv2 and Auto Scaling SDK paginators.
- Waiters for asynchronous resource states.
- Idempotent deployment automation.
- Cross-account deployment pipelines.
- Tagging standards.
- AWS Config managed rules.
- Service Control Policies for ELB and Auto Scaling.
- Policy-as-code validation.
- Drift detection.
- Automated quota checks.
- Automated certificate-expiry checks.
- Automated target-health validation.
- Automated scaling-policy tests.

### Quotas, Limits, and Regional Availability

- Load balancers per Region.
- Target groups per Region.
- Targets per target group.
- Listeners per load balancer.
- Listener rules per ALB.
- Certificates per load balancer.
- Trust stores per ALB.
- Target-group association limits.
- Security groups per load balancer.
- NLB targets per Availability Zone.
- NLB ports per target and source tuple.
- Load-balancer capacity-unit reservation limits.
- Gateway Load Balancer quotas.
- GWLB endpoint quotas.
- Auto Scaling groups per Region.
- Launch configurations per Region.
- Scaling policies per Auto Scaling group.
- Scheduled actions per Auto Scaling group.
- Lifecycle hooks per Auto Scaling group.
- Warm-pool limitations.
- Instance-refresh limitations.
- EC2 instance quotas by family.
- Elastic IP address quotas.
- ENI and private-IP limits.
- VPC, subnet, and security-group quotas.
- CloudWatch alarm and metric quotas.
- Service Quotas requests and lead times.
- Feature availability by Region.
- New-Region feature rollout differences.
- Availability Zone capacity differences.

### Pricing and Cost Engineering

- ALB hourly pricing.
- Load Balancer Capacity Units (LCUs).
- LCU new-connection dimension.
- LCU active-connection dimension.
- LCU processed-bytes dimension.
- LCU rule-evaluation dimension.
- NLB hourly pricing.
- Network Load Balancer Capacity Units (NLCUs).
- NLCU flow, connection, and byte dimensions.
- GWLB hourly and capacity-unit pricing.
- Capacity-unit reservation pricing.
- Cross-zone data-transfer pricing.
- Inter-AZ data-transfer costs.
- Public IPv4 address charges.
- Elastic IP address charges.
- AWS PrivateLink endpoint-hour and data charges.
- NAT Gateway costs in load-balanced architectures.
- AWS WAF request and rule charges.
- Shield Advanced pricing.
- ACM public versus Private CA costs.
- EC2 Auto Scaling service pricing boundary.
- EC2 On-Demand pricing.
- Reserved Instances and Savings Plans.
- Spot Instance savings and interruption cost.
- Warm-pool compute and storage costs.
- Detailed monitoring costs.
- Access-log storage and query costs.
- CloudWatch custom metric and alarm costs.
- Cost allocation tags.
- Cost Explorer analysis for elastic workloads.
- AWS Pricing Calculator load-balancer modelling.
- Cost per request.
- Cost per concurrent connection.
- Cost-versus-headroom tradeoffs.
- Cost anomalies caused by scaling loops.

### Performance Engineering and Load Testing

- Workload modelling.
- Requests per second and transactions per second.
- Concurrent connections.
- Connection establishment rate.
- Throughput and processed bytes.
- Latency percentiles: p50, p90, p95, p99, and p99.9.
- Tail latency.
- Coordinated omission in load tests.
- Open-loop versus closed-loop load generation.
- Ramp, spike, soak, and stress tests.
- Capacity and saturation tests.
- Failover load tests.
- Cold-start and warm-start measurements.
- Connection reuse and pooling.
- HTTP keep-alive tuning.
- HTTP/2 multiplexing behavior.
- TLS handshake cost.
- Backend connection limits.
- Target accept-queue saturation.
- Linux socket backlog.
- File descriptor limits.
- Ephemeral-port exhaustion.
- NAT port exhaustion.
- Application thread and worker pools.
- Queue-depth scaling.
- Little's Law.
- Load-distribution fairness.
- Sticky-session skew.
- Hot-target detection.
- Cross-zone latency and traffic effects.
- Slow-start tuning.
- Deregistration-delay tuning.
- Health-check tuning.
- Default-instance-warmup tuning.
- Scaling reaction time.
- Scaling stabilization and oscillation.
- Capacity headroom modelling.
- Load-test safety controls.
- Production traffic replay risks.

### Resilience Testing and Chaos Engineering

- EC2 instance termination experiments.
- Target-process failure experiments.
- Health-endpoint failure experiments.
- Availability Zone evacuation tests.
- AWS Application Recovery Controller zonal shift.
- Autoshift and practice runs.
- NLB zonal-shift prerequisites.
- Multi-AZ capacity verification.
- Subnet exhaustion experiments.
- Security-group misconfiguration simulations.
- Dependency latency injection.
- Packet-loss and connection-reset injection.
- DNS failure simulations.
- TLS certificate-expiry exercises.
- Failed deployment rollback drills.
- Auto Scaling launch-failure exercises.
- Spot interruption exercises.
- Capacity Rebalancing validation.
- Warm-pool failure exercises.
- Scaling-policy runaway simulations.
- Retry-storm simulations.
- Load-shedding validation.
- Circuit-breaker validation.
- Fail-open risk assessment.
- AWS Fault Injection Service.
- Game days.
- Recovery runbooks.
- Incident command and escalation.
- Post-incident review and corrective actions.

### Adjacent AWS Traffic and Compute Services

- Amazon Route 53 routing and health evaluation.
- Amazon CloudFront origin failover.
- AWS Global Accelerator.
- AWS Global Accelerator endpoint groups and traffic dials.
- Amazon API Gateway throttling and integration scaling.
- Amazon VPC Lattice.
- AWS App Mesh lifecycle and alternatives.
- Amazon ECS Service Auto Scaling.
- ECS capacity providers.
- Amazon EKS Cluster Autoscaler.
- Kubernetes Horizontal Pod Autoscaler.
- Karpenter.
- Lambda reserved and provisioned concurrency.
- AWS App Runner Auto Scaling.
- Elastic Beanstalk load-balanced environments.
- AWS Elastic Disaster Recovery.
- AWS Application Recovery Controller.
- Route 53 Application Recovery Controller readiness checks.
- AWS WAF and Shield architectures.
- Service discovery with AWS Cloud Map.
- Amazon SQS queue-depth-based scaling.
- Event-driven scaling patterns.
- KEDA on Kubernetes.
- Multi-Region ingress architectures.
