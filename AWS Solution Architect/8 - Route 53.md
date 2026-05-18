# 8 - Route 53

## Quick Summary

Amazon Route 53 is AWS's DNS and domain registration service. It helps users reach applications by translating domain names into destinations such as IP addresses, load balancers, CloudFront distributions, or other AWS resources.

Beginner mental model:

```text
user enters app.example.com -> DNS lookup -> Route 53 returns where to go
```

## Why DNS Matters

Applications move:

- Instances are replaced.
- Load balancers scale.
- CloudFront edge locations change.
- Disaster recovery may shift traffic.

DNS gives users a stable name while infrastructure changes behind it.

## Core Concepts

| Term | Meaning |
| --- | --- |
| Domain | Human-readable name, such as `example.com`. |
| Hosted zone | Container for DNS records for a domain. |
| Record | DNS entry, such as A, AAAA, CNAME, MX, TXT. |
| TTL | Time resolvers can cache a record. |
| Resolver | DNS server that looks up names for clients. |
| Registrar | Company/service where a domain is registered. |
| Authoritative DNS | DNS service that owns final answers for a domain. |

## Hosted Zones

Public hosted zone:

- Used for internet DNS.
- Example: `example.com`.
- Answers public DNS queries.

Private hosted zone:

- Used inside VPCs.
- Example: internal names like `db.internal.example.com`.
- Associated with one or more VPCs.

## Common Record Types

| Record | Purpose |
| --- | --- |
| A | Name to IPv4 address. |
| AAAA | Name to IPv6 address. |
| CNAME | Alias one DNS name to another DNS name. |
| MX | Mail servers. |
| TXT | Text records for verification, SPF, DKIM, etc. |
| NS | Name servers for zone delegation. |
| SOA | Start of authority metadata. |

## Alias Records

Route 53 alias records point to selected AWS resources.

Common targets:

- Elastic Load Balancer.
- CloudFront distribution.
- API Gateway custom domain.
- S3 static website endpoint.
- Global Accelerator.

Alias records are useful because the target can have changing IP addresses while Route 53 resolves it correctly.

## CNAME vs Alias

| Feature | CNAME | Alias |
| --- | --- | --- |
| Points to | Another DNS name. | Supported AWS resources or records. |
| Zone apex support | No for root like `example.com`. | Yes. |
| AWS integration | Generic DNS. | AWS-specific integration. |
| Query charge behavior | Normal DNS behavior. | Some AWS alias targets have special billing behavior. |

Use alias for root domain to AWS resources.

## Routing Policies

| Policy | Use |
| --- | --- |
| Simple | One basic answer. |
| Weighted | Split traffic by weights. |
| Latency | Route to Region with lowest latency. |
| Failover | Active-passive DR with health checks. |
| Geolocation | Route by user location. |
| Geoproximity | Route by location with optional bias. |
| Multi-value answer | Return multiple healthy records. |

## Health Checks

Route 53 health checks can monitor endpoints and affect DNS answers.

Use cases:

- Failover routing.
- Remove unhealthy endpoints.
- Monitor application endpoint health.

Health checks can check:

- HTTP.
- HTTPS.
- TCP.

Design warning:

```text
DNS failover is not instant because clients and resolvers cache records based on TTL.
```

## TTL

TTL is caching duration in seconds.

Short TTL:

- Faster changes.
- More DNS queries.

Long TTL:

- More caching.
- Slower failover/changes.

Choose TTL based on stability and failover needs.

## Domain Registration

Route 53 can register domains and automatically create/assign name servers. You can also use another registrar and point name servers to Route 53.

## Common Architectures

Public web app:

```text
app.example.com -> Route 53 alias -> ALB
```

Static website/CDN:

```text
www.example.com -> Route 53 alias -> CloudFront -> S3/origin
```

Active-passive DR:

```text
primary.example.com -> Region A endpoint
secondary.example.com -> Region B endpoint
app.example.com -> failover routing
```

## Benefits

- Managed DNS.
- Tight AWS integration.
- Routing policies for global/DR patterns.
- Health-check-driven failover.
- Supports public and private hosted zones.

## Drawbacks / Limitations

- DNS caching means changes are not always instant.
- Incorrect NS records can break whole domain.
- Private hosted zones only work where associated/resolved.
- Routing policy mistakes can send users to wrong endpoint.

## Hidden Details / Caveats

- A hosted zone has name servers; your registrar must delegate to them.
- Alias records are Route 53-specific.
- CloudFront alternate domain names require certificate/domain configuration.
- Root/apex domains cannot use CNAME in standard DNS; use alias for AWS targets.
- Health checks must test the real user path where possible.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| CNAME at zone apex | Use Route 53 alias. |
| Wrong NS delegation | Match registrar name servers to hosted zone NS records. |
| TTL too high for failover | Lower TTL for records needing quick change. |
| Health check tests wrong path | Check actual health endpoint. |
| Confusing private and public zones | Verify resolver/VPC association. |

## Troubleshooting

```bash
dig example.com
dig NS example.com
dig +trace example.com
nslookup app.example.com
```

| Problem | Check |
| --- | --- |
| Domain does not resolve | Registrar delegation, hosted zone, record name. |
| Old value still returned | TTL/cache. |
| Private name not resolving | VPC association, resolver settings, zone name conflict. |
| Failover not happening | Health check status, routing policy, TTL. |

## Interview Notes

- Route 53 is DNS plus domain registration and health checking.
- Hosted zone stores DNS records.
- Alias records integrate with AWS resources and support apex records.
- TTL controls DNS cache duration.
- Routing policies support weighted, latency, failover, geolocation, geoproximity, and multi-value answer patterns.

## Official References

- Route 53 documentation: <https://docs.aws.amazon.com/route53/>
- Routing to Global Accelerator: <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-global-accelerator.html>
