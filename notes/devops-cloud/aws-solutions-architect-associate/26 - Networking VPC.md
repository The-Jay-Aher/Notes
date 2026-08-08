# Networking VPC

## Quick Summary
- A VPC is your private network boundary inside AWS.
- Subnets divide a VPC by Availability Zone and routing purpose.
- Route tables decide where traffic goes.
- Internet Gateways allow public internet access for public subnets.
- NAT Gateways allow private subnet workloads to reach the internet without accepting inbound internet connections.
- Security groups are stateful instance-level firewalls; NACLs are stateless subnet-level filters.
- VPC design is one of the most important Solutions Architect topics.

## VPC Mental Model
A VPC is like a private data center network in AWS.

Inside a VPC, you create:
- IP address range.
- Subnets.
- Route tables.
- Gateways.
- Security rules.
- Endpoints.
- Peering or transit connections.

Basic high-availability layout:

```text
VPC 10.0.0.0/16
  AZ A:
    public subnet 10.0.1.0/24
    private app subnet 10.0.2.0/24
    private data subnet 10.0.3.0/24
  AZ B:
    public subnet 10.0.11.0/24
    private app subnet 10.0.12.0/24
    private data subnet 10.0.13.0/24
```

## CIDR Blocks
CIDR defines IP address ranges.

Example:
- `10.0.0.0/16` is a large VPC range.
- `10.0.1.0/24` is a smaller subnet range.

Beginner tips:
- VPC CIDR ranges should not overlap with networks you need to connect to.
- Plan enough IP addresses for growth.
- Each subnet loses some IP addresses reserved by AWS.

## Subnets
A subnet exists in one Availability Zone.

Common subnet types:
- Public subnet.
- Private application subnet.
- Private database subnet.

A subnet is public if its route table has a route to an Internet Gateway and resources have public IPs or public-facing load balancer placement.

A subnet is private if it does not route inbound internet traffic directly.

## Route Tables
Route tables decide where traffic goes.

Example public route table:

```text
10.0.0.0/16 -> local
0.0.0.0/0  -> internet gateway
```

Example private route table:

```text
10.0.0.0/16 -> local
0.0.0.0/0  -> NAT gateway
```

Most routing bugs are route table bugs, not EC2 bugs.

## Internet Gateway
An Internet Gateway enables internet connectivity for a VPC.

For an EC2 instance to be reachable from the internet:
- VPC has an Internet Gateway.
- Subnet route table routes `0.0.0.0/0` to the Internet Gateway.
- Instance has public IPv4 or appropriate IPv6 setup.
- Security group allows inbound traffic.
- NACL allows traffic.
- OS firewall/application listens on the port.

## NAT Gateway
NAT Gateway lets private subnet resources initiate outbound internet connections.

Example:
- Private EC2 instance downloads OS updates.
- It reaches internet through NAT Gateway.
- Internet cannot initiate connections directly to that private instance through the NAT Gateway.

High availability:
- Create NAT Gateway per AZ for resilient architecture.
- Route private subnets in each AZ to the NAT Gateway in the same AZ where possible.

Cost note:
- NAT Gateway has hourly and data processing charges. For high-volume traffic to AWS services, VPC endpoints may reduce cost and improve private connectivity.

## Security Groups
Security groups are stateful firewalls attached to network interfaces/resources.

Stateful means:
- If inbound request is allowed, response traffic is automatically allowed.
- If outbound request is allowed, response traffic is automatically allowed.

Common design:
- ALB security group allows inbound 80/443 from internet.
- App security group allows inbound app port only from ALB security group.
- DB security group allows inbound database port only from app security group.

```text
Internet -> ALB SG -> App SG -> DB SG
```

Best practice:
- Reference security groups instead of broad IP ranges for internal tiers.

## Network ACLs
NACLs are subnet-level stateless filters.

Stateless means:
- Inbound and outbound rules must both allow traffic.
- Return traffic must be explicitly allowed.

NACLs have numbered allow/deny rules evaluated in order.

Use NACLs for:
- Broad subnet guardrails.
- Explicit deny at subnet boundary.

Most workload-level access control should be done with security groups.

## VPC Endpoints
VPC endpoints allow private connectivity to AWS services without using the public internet.

Types:
- Gateway endpoints.
- Interface endpoints.

### Gateway Endpoints
Supported for:
- S3.
- DynamoDB.

They are added to route tables.

### Interface Endpoints
Powered by AWS PrivateLink.

They create ENIs in your subnets and provide private access to supported services.

Use interface endpoints for services like:
- Secrets Manager.
- SSM.
- CloudWatch Logs.
- ECR.
- STS.

Benefits:
- Private traffic path.
- Less dependence on NAT Gateway for AWS service calls.
- Better security controls with endpoint policies.

## VPC Peering
VPC Peering connects two VPCs privately.

Important limitations:
- No transitive routing.
- CIDR blocks must not overlap.
- Route tables must be updated on both sides.

No transitive routing means:

```text
VPC A peered to VPC B
VPC B peered to VPC C
VPC A cannot reach VPC C through VPC B by peering alone
```

## Transit Gateway
Transit Gateway is a hub for connecting many networks.

Use it when:
- Many VPCs need connectivity.
- On-premises networks connect to multiple VPCs.
- You want centralized routing.

Mental model:

```text
VPC A \
VPC B  -> Transit Gateway -> VPN/Direct Connect/on-prem
VPC C /
```

## Site-to-Site VPN
AWS Site-to-Site VPN connects on-premises networks to AWS over encrypted tunnels through the internet.

Use it for:
- Quick hybrid connectivity.
- Backup connectivity.
- Lower-cost connections.

Tradeoffs:
- Internet path can have variable latency.
- Bandwidth is limited compared with Direct Connect options.

## Direct Connect
AWS Direct Connect provides dedicated network connectivity to AWS.

Use it when:
- You need more predictable network performance.
- You need higher bandwidth.
- You have hybrid workloads.
- You want private connectivity from a data center or colocation.

Direct Connect does not automatically encrypt traffic. Use VPN over Direct Connect or application-layer encryption where required.

## VPC Flow Logs
VPC Flow Logs capture metadata about network traffic.

Use them for:
- Troubleshooting security group/NACL issues.
- Audit.
- Traffic analysis.

They show accepted/rejected flow metadata, not packet payloads.

## Public vs Private Workload Pattern
Common 3-tier architecture:

```text
Public subnet:
  ALB, NAT Gateway

Private app subnet:
  EC2/ECS application tasks

Private data subnet:
  RDS/ElastiCache
```

Users reach only the ALB. Apps reach databases privately.

## Common Troubleshooting Checklist
If an instance cannot reach the internet:
- Does subnet route table have `0.0.0.0/0` to IGW or NAT?
- Is the instance public or private?
- Does it have public IP if using IGW?
- Does security group allow outbound?
- Does NACL allow outbound and return traffic?
- Is DNS resolution enabled if using hostnames?

If internet cannot reach a web app:
- Is the app in a public subnet or behind a public load balancer?
- Does the route table point to IGW?
- Does security group allow inbound port?
- Does NACL allow inbound and ephemeral return ports?
- Is the application listening on the expected port?
- Is the OS firewall blocking it?

## Common Mistakes
- Putting databases in public subnets.
- Creating a public subnet route but forgetting public IPs or load balancer.
- Routing private subnet traffic to an Internet Gateway instead of NAT Gateway.
- Using one NAT Gateway for all AZs without understanding AZ failure impact.
- Forgetting NACL return traffic rules.
- Creating overlapping VPC CIDRs and then needing peering/VPN later.
- Assuming VPC peering is transitive.
- Ignoring NAT Gateway data processing cost.

## Official References
- [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/)
- [VPC route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)
- [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/)
- [AWS Transit Gateway documentation](https://docs.aws.amazon.com/vpc/latest/tgw/)
- [AWS Direct Connect documentation](https://docs.aws.amazon.com/directconnect/)
- [AWS Site-to-Site VPN documentation](https://docs.aws.amazon.com/vpn/latest/s2svpn/)
