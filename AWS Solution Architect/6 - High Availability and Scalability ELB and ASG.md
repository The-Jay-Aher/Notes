# 6 - High Availability and Scalability with ELB and ASG

## Why This Chapter Matters

Most real applications do not fail because one command was typed wrongly. They fail because the architecture assumes that one server, one data center, one health check, one scaling metric, or one deployment path will always behave correctly.

High availability and scalability exist because production traffic is uneven and infrastructure is imperfect:

```text
User demand changes
-> one server becomes too small or one Availability Zone fails
-> users experience slow responses or downtime
-> the architecture needs traffic distribution, health checks, replacement, and capacity adjustment
-> Elastic Load Balancing and Auto Scaling Groups become core EC2 design tools
```

For the AWS Solutions Architect Associate exam, ELB and ASG are not only "services to memorize". They are the machinery behind many scenario questions:

- "The application must survive an Availability Zone failure."
- "Users should not connect directly to EC2 instances."
- "The application should scale out during traffic spikes and scale in afterwards."
- "Unhealthy instances should stop receiving traffic."
- "A static IP is required in front of a high-performance TCP service."
- "Microservices need path-based routing."
- "Instances need time to drain requests before termination."

If you understand this chapter properly, an EC2 web architecture stops looking like separate AWS icons and starts looking like a self-healing traffic system.

## The Big Picture

A common production pattern is:

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

Self-managed load balancers may still be valid for special appliances, custom routing behaviour, or legacy constraints, but then you own patching, scaling, monitoring, security hardening, and HA.

## ELB Types

AWS supports four ELB families.

| Load Balancer                   | OSI Layer                   | Protocols / Main Use                                           | New Design Guidance                                                                     |
| ------------------------------- | --------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Application Load Balancer (ALB) | Layer 7                     | HTTP, HTTPS, HTTP/2, WebSocket, gRPC-style HTTP routing        | Use for web apps, APIs, microservices, host/path/header/query routing.                  |
| Network Load Balancer (NLB)     | Layer 4                     | TCP, UDP, TCP_UDP, TLS, newer protocols where supported by AWS | Use for high-performance transport traffic, static IP, PrivateLink, non-HTTP workloads. |
| Gateway Load Balancer (GWLB)    | Layer 3/4 appliance pattern | IP packets using GENEVE on port 6081                           | Use for third-party virtual appliances such as firewalls and inspection tools.          |
| Classic Load Balancer (CLB)     | Legacy                      | HTTP, HTTPS, TCP, SSL                                          | Avoid for new designs unless maintaining legacy architecture.                           |

Historic release clues often seen in courses:

- CLB: older generation.
- ALB: newer generation for Layer 7 HTTP routing.
- NLB: newer generation for Layer 4 performance.
- GWLB: appliance fleet pattern.

Exam rule:

```text
Path-based routing, host-based routing, WAF on web traffic -> ALB
TCP/UDP, static IP per AZ, ultra-low latency -> NLB
Third-party firewall/inspection appliance fleet -> GWLB
Legacy simple load balancer already exists -> CLB only if migration is not required
```

## Internal vs Internet-Facing Load Balancers

| Scheme | Meaning | Use |
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
- [AWS Cloud Practitioner - Storage, Networking and Database](../AWS%20Cloud%20Practitioner/2%20-%20Storage%2C%20Networking%20and%20Database.md)
- [Networking Fundamentals](../Networking%20Fundamentals/1%20-%20Fundamentals%20of%20Networking.md)

## Official References

- Elastic Load Balancing documentation: <https://docs.aws.amazon.com/elasticloadbalancing/>
- Application Load Balancer documentation: <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html>
- ELB health checks: <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html>
- EC2 Auto Scaling groups: <https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html>
- Auto Scaling health checks: <https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.html>

