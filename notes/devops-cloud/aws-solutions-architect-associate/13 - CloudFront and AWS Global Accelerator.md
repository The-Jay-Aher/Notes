# 13 - CloudFront and AWS Global Accelerator

## Quick Summary

Amazon CloudFront is a content delivery network for caching and delivering HTTP/HTTPS content from edge locations. AWS Global Accelerator improves global TCP/UDP application availability and performance using static anycast IPs and the AWS global network.

Beginner difference:

```text
CloudFront = HTTP content/API acceleration and caching
Global Accelerator = static IPs and global network routing for TCP/UDP endpoints
```

## Amazon CloudFront

CloudFront sits between users and your origin.

```text
User -> nearest CloudFront edge -> origin such as S3, ALB, EC2, API Gateway
```

Origins can include:

- S3 bucket.
- Application Load Balancer.
- EC2/custom HTTP server.
- API Gateway.
- Media services.

## Why Use CloudFront

- Lower latency for global users.
- Cache static content near users.
- Reduce origin load.
- Add HTTPS at edge.
- Integrate AWS WAF.
- Protect private S3 origins.
- Support signed URLs/cookies for restricted content.

## Cache Behavior

CloudFront uses cache behaviors to decide how requests are handled.

Cache behavior can match:

- Path pattern.
- Origin.
- Allowed HTTP methods.
- Cache policy.
- Origin request policy.
- Viewer protocol policy.

Example:

```text
/static/* -> S3 origin, cached for long time
/api/*    -> ALB origin, limited/no caching
```

## TTL And Invalidation

TTL controls how long CloudFront caches content.

If content changes before TTL expires:

- Use versioned filenames, such as `app.v123.js`.
- Or create invalidation.

Invalidation:

```text
Tell CloudFront to remove cached object/path from edge caches.
```

Versioned filenames are often better for static assets.

## Origin Access Control

For private S3 origins, use CloudFront origin access controls so users cannot bypass CloudFront and directly read from S3.

Pattern:

```text
User -> CloudFront -> private S3 bucket
Direct public S3 access blocked
```

## Signed URLs And Signed Cookies

Use signed URLs/cookies for private content distribution.

Use when:

- Paid content.
- Private downloads.
- Time-limited access.

## CloudFront Security

Security features:

- HTTPS viewer connections.
- ACM certificates in required Region for CloudFront.
- AWS WAF integration.
- Origin access control.
- Geo restriction.
- Signed URLs/cookies.

## AWS Global Accelerator

Global Accelerator provides static anycast IP addresses and routes user traffic over the AWS global network to healthy endpoints.

Endpoint types can include:

- Application Load Balancers.
- Network Load Balancers.
- EC2 instances.
- Elastic IPs.

## Why Use Global Accelerator

Use when:

- Need static public IPs for global app.
- Need TCP/UDP acceleration, not just HTTP caching.
- Need fast failover across Regions/endpoints.
- Clients cannot easily use DNS changes.

## CloudFront vs Global Accelerator

| Need | Use |
| --- | --- |
| Cache static HTTP content | CloudFront. |
| Accelerate HTTP APIs with edge caching/security | CloudFront. |
| Static anycast IPs | Global Accelerator. |
| TCP/UDP non-HTTP acceleration | Global Accelerator. |
| Private S3 origin protection | CloudFront. |
| WAF at edge | CloudFront with AWS WAF. |

## Benefits

- CloudFront reduces latency and origin load.
- CloudFront integrates with S3 and WAF.
- Global Accelerator gives static IPs and fast global routing.
- Both use AWS edge/global network capabilities.

## Drawbacks / Limitations

- CloudFront caching must be designed carefully.
- Invalidation has cost/operational considerations.
- Global Accelerator is not a cache.
- Certificates/domain setup must be correct.
- Debugging includes DNS, edge, origin, cache policy, and headers.

## Hidden Details / Caveats

- CloudFront alternate domain names need valid certificates.
- CloudFront can cache error responses.
- Query strings, headers, and cookies affect cache keys depending on policy.
- Global Accelerator static IPs are anycast.
- Route 53 alias can point to CloudFront or Global Accelerator.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Expecting CloudFront to update instantly | Use TTL/versioning/invalidation. |
| Caching API responses accidentally | Configure cache policies carefully. |
| Public S3 origin behind CloudFront | Use private bucket plus origin access control. |
| Using Global Accelerator for static web caching | Use CloudFront. |
| Wrong certificate Region/config | Follow CloudFront certificate requirements. |

## Troubleshooting

| Problem | Check |
| --- | --- |
| Old content served | TTL, invalidation, browser cache, object versioning. |
| 403 from S3 origin | Bucket policy, origin access control, object key. |
| API cached incorrectly | Cache behavior, cache key, headers/query/cookies. |
| Custom domain fails | DNS alias, certificate, alternate domain name. |
| Global app slow | Endpoint health, Region routing, accelerator listener. |

## Interview Notes

- CloudFront is CDN for HTTP/HTTPS content and APIs.
- CloudFront caches at edge locations.
- Global Accelerator provides static anycast IPs and global routing.
- CloudFront is for caching/content delivery; Global Accelerator is for network acceleration/failover.
- Use origin access control to keep S3 private behind CloudFront.

## Official References

- CloudFront documentation: <https://docs.aws.amazon.com/cloudfront/>
- Global Accelerator documentation: <https://docs.aws.amazon.com/global-accelerator/>
- Route 53 to Global Accelerator: <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-global-accelerator.html>
