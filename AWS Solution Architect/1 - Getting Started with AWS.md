# 1 - Getting Started with AWS

## Quick Summary

AWS is organized around global infrastructure, managed services, identity, networking, security, and billing. For Solutions Architect learning, start with Regions, Availability Zones, edge locations, account boundaries, and the Well-Architected way of thinking.

The core design question is:

```text
How do I place services so the system is secure, reliable, performant, and cost-effective?
```

## AWS Global Infrastructure Basics

AWS infrastructure is organized into:

| Term | Meaning |
| --- | --- |
| Region | A geographic area containing multiple Availability Zones. Example: `ap-south-1`, `us-east-1`. |
| Availability Zone | One or more discrete data centers with independent power, networking, and connectivity inside a Region. |
| Edge Location | Site used by edge services such as CloudFront to serve users closer to their location. |
| Local Zone | Extension of a Region near a metropolitan area for low-latency workloads. |
| Wavelength Zone | AWS infrastructure embedded in telecom networks for ultra-low-latency 5G edge workloads. |
| Outposts | AWS infrastructure installed on-premises for hybrid workloads. |

## Region

A Region is the first major placement decision.

Choose a Region based on:

- Compliance and data residency.
- User proximity and latency.
- Service availability.
- Pricing.
- Disaster recovery design.
- Existing network connectivity.
- Operational support and team familiarity.

Example:

```text
Indian retail application with mostly Indian users -> ap-south-1 may reduce latency and help data locality.
Global SaaS app -> primary Region plus DR/multi-Region strategy may be needed.
```

## Availability Zones

Availability Zones are separate facilities inside a Region connected by low-latency, high-bandwidth, redundant networking.

Design use:

- Run production workloads across at least two AZs.
- Place public load balancer subnets in multiple AZs.
- Place application instances across multiple AZs.
- Use managed database Multi-AZ options where appropriate.

Simple pattern:

```text
Region
  AZ A: public subnet + private app subnet
  AZ B: public subnet + private app subnet
  ALB spans AZ A and AZ B
  ASG launches app instances across AZ A and AZ B
```

## Edge Locations

Edge locations are used by services that benefit from being closer to users.

Examples:

- CloudFront content delivery.
- AWS WAF on CloudFront distributions.
- Route 53 DNS resolution.

Use edge services when:

- Global users need lower latency.
- Static content should be cached.
- You want edge protection before traffic reaches origins.

## Local Zones, Wavelength, and Outposts

| Option | Use Case |
| --- | --- |
| Local Zones | Low-latency apps near a city, such as media, gaming, real-time collaboration. |
| Wavelength | Ultra-low-latency apps at telecom 5G edge. |
| Outposts | Run AWS services on-premises for latency, data residency, or hybrid requirements. |

These are specialized. Most beginner architectures start with Regions and AZs.

## How To Choose An AWS Region

Use this checklist:

1. Is the service available in the Region?
2. Are there legal/data residency constraints?
3. Where are the users?
4. What latency is acceptable?
5. What is the cost difference?
6. What DR strategy is required?
7. Does the team already operate there?
8. Are required partner/network connections available?

## AWS Account Basics

An AWS account is a security, billing, and resource boundary.

Important points:

- Root user should not be used for daily work.
- Enable MFA on root user.
- Use IAM Identity Center or IAM users/roles for access.
- Separate environments with accounts where possible.
- Use AWS Organizations for multi-account management.

Common account layout:

```text
management account
security/logging account
shared services account
dev account
staging account
prod account
```

## Shared Responsibility Model

AWS is responsible for security of the cloud. Customers are responsible for security in the cloud.

Customer responsibilities often include:

- IAM.
- Data protection.
- Network rules.
- OS/app patching depending on service.
- Encryption settings.
- Logging and monitoring.
- Application code.

Managed services reduce operational responsibility but do not remove configuration responsibility.

## AWS Well-Architected Framework

The AWS Well-Architected Framework has six pillars:

| Pillar | Focus |
| --- | --- |
| Operational Excellence | Operate, monitor, and improve systems. |
| Security | Protect data, systems, and assets. |
| Reliability | Recover from failures and meet availability goals. |
| Performance Efficiency | Use resources efficiently as demand changes. |
| Cost Optimization | Avoid unnecessary cost. |
| Sustainability | Minimize environmental impact of workloads. |

Use these pillars as design review questions, not as theory.

## Quick Example Architecture Pattern

Starter production web app:

```text
Route 53
  -> CloudFront/WAF if global/edge protection needed
  -> Application Load Balancer across two AZs
  -> Auto Scaling Group in private subnets
  -> RDS Multi-AZ or managed database
  -> CloudWatch logs/metrics/alarms
```

Design ideas:

- Users hit DNS/load balancer, not instances directly.
- App instances are replaceable.
- Persistent data lives in managed durable services.
- Logs and metrics are collected centrally.
- IAM roles give least-privilege access.

## Practical Starter Guidance

- Start in one Region close to users unless requirements say otherwise.
- Use at least two AZs for production workloads.
- Keep public resources minimal.
- Put app/database systems in private subnets where possible.
- Use managed services for undifferentiated heavy lifting.
- Tag resources consistently.
- Enable logging early.
- Create budgets and billing alarms.
- Use IAM roles instead of long-lived keys where possible.

## Benefits

- Regions and AZs support resilient architecture.
- Edge services improve global performance.
- Accounts provide security and billing boundaries.
- Well-Architected pillars guide design trade-offs.

## Drawbacks / Limitations

- Multi-AZ and multi-Region designs add cost and complexity.
- Not every service is available in every Region.
- Data transfer costs can surprise beginners.
- Misconfigured IAM/networking can expose resources even if architecture looks good.

## Hidden Details / Caveats

- AZ names such as `ap-south-1a` can map differently between AWS accounts.
- Service quotas vary and may need increases.
- Multi-Region is not automatically required; use it when RTO/RPO or global design demands it.
- Edge caching can serve stale content if cache invalidation is not planned.
- Public subnet means route to internet gateway, not automatically "secure" or "insecure" by itself.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Everything in one AZ | Spread production across at least two AZs. |
| Using root user daily | Enable MFA and use IAM/Identity Center. |
| Choosing Region only by habit | Check users, compliance, service availability, and cost. |
| No tags | Define required tags from day one. |
| Public databases | Keep databases private unless there is a reviewed requirement. |
| No budget alarm | Add cost visibility early. |

## Interview Notes

- Region is geographic; AZ is isolated data center grouping inside a Region.
- Use multiple AZs for high availability.
- Edge locations support services such as CloudFront and Route 53.
- AWS account is a security and billing boundary.
- Shared responsibility changes depending on service model.
- Well-Architected has six pillars.

## Related Topics

- [IAM and AWS CLI](2%20-%20IAM%20and%20AWS%20CLI.md)
- [High Availability and Scalability ELB and ASG](6%20-%20High%20Availability%20and%20Scalability%20ELB%20and%20ASG.md)
- [Networking Fundamentals](../Networking%20Fundamentals/1%20-%20Fundamentals%20of%20Networking.md)

## Official References

- AWS Regions and Availability Zones: <https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html>
- AWS Well-Architected Framework pillars: <https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html>

