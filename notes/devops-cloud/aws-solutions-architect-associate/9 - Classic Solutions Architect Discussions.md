# 9 - Classic Solutions Architect Discussions

## Quick Summary

This note collects common AWS Solutions Architect design patterns and trade-offs. These are not single-service facts; they are scenario-thinking patterns used in exam questions and real architecture reviews.

## How To Think Like A Solutions Architect

For every scenario, ask:

1. What is the workload?
2. Is it stateless or stateful?
3. What are the availability requirements?
4. What are the latency requirements?
5. What data must be durable?
6. What traffic pattern exists?
7. What security boundary is required?
8. What is the cost constraint?
9. What is the operational burden?
10. What is the simplest managed service that fits?

## Classic Web Application

Pattern:

```text
Route 53 -> CloudFront/WAF -> ALB -> Auto Scaling Group -> RDS/Aurora
```

Use when:

- HTTP/HTTPS app.
- Multiple users.
- Needs high availability.
- Relational database required.

Key design:

- ALB in public subnets.
- App instances in private subnets.
- Database in private DB subnets.
- ASG across multiple AZs.
- RDS/Aurora Multi-AZ.
- Logs/metrics in CloudWatch.

## Static Website

Pattern:

```text
Route 53 -> CloudFront -> S3 static content
```

Use when:

- HTML/CSS/JS/image assets.
- No server-side compute needed.
- Need global caching.

Security:

- Keep S3 bucket private when using CloudFront origin access controls.
- Use HTTPS with ACM certificate.
- Use WAF if request filtering is needed.

## Serverless API

Pattern:

```text
Route 53 -> API Gateway -> Lambda -> DynamoDB
```

Use when:

- Event-driven app.
- Variable traffic.
- Minimal server management desired.
- Stateless request handling.

Watch-outs:

- Lambda timeout.
- Cold starts.
- API Gateway throttling.
- DynamoDB partition key design.
- IAM permissions.

## Decoupled Worker System

Pattern:

```text
Producer -> SQS queue -> Worker ASG/Lambda -> Database/S3
```

Use when:

- Work can happen asynchronously.
- Spikes need buffering.
- Producer should not wait for slow processing.

Benefits:

- Queue absorbs traffic spikes.
- Workers scale independently.
- Failures can be retried.

## Fanout Messaging

Pattern:

```text
Publisher -> SNS topic -> SQS queue A
                       -> SQS queue B
                       -> Lambda
```

Use when:

- One event should go to multiple consumers.
- Consumers process independently.
- Filtering may be useful.

## Multi-Region Disaster Recovery

Common strategies:

| Strategy | Cost | Recovery Speed |
| --- | --- | --- |
| Backup and restore | Low | Slowest. |
| Pilot light | Low-medium | Medium. |
| Warm standby | Medium-high | Faster. |
| Active-active | Highest | Fastest. |

Choose based on RTO/RPO, not because multi-Region sounds impressive.

## Caching Pattern

```text
Users -> CloudFront -> ALB/API -> ElastiCache -> Database
```

Use caching to:

- Reduce database reads.
- Reduce latency.
- Absorb read spikes.

Watch-outs:

- Cache invalidation.
- TTL.
- Stale reads.
- Memory limits.

## File Upload Pattern

Good pattern:

```text
Client -> pre-signed S3 URL -> S3
S3 event -> Lambda/queue -> processing
```

Why:

- Avoids sending large files through app server.
- S3 handles storage.
- Processing can be asynchronous.

## Benefits Of Pattern Thinking

- Faster service selection.
- Better exam performance.
- Easier architecture explanation.
- Avoids overengineering.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Putting EC2 in public subnets by default | Use ALB public, app private. |
| Making everything synchronous | Use queues/events for slow work. |
| Multi-Region without requirement | Match RTO/RPO and budget. |
| Using RDS for all data | Consider DynamoDB/S3/cache/analytics stores based on access pattern. |
| Ignoring IAM/network boundaries | Design least privilege and private access. |

## Interview Notes

- Stateless app tier scales horizontally behind load balancer.
- State belongs in databases, S3, EFS, or managed stores, not instance disks.
- Use SQS to decouple producers and consumers.
- Use SNS for pub/sub fanout.
- Use CloudFront for global cache and edge delivery.
- Choose DR strategy from RTO/RPO.

## Official References

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html)
- [Elastic Load Balancing documentation](https://docs.aws.amazon.com/elasticloadbalancing/)
- [Amazon SQS documentation](https://docs.aws.amazon.com/sqs/)
- [Amazon SNS documentation](https://docs.aws.amazon.com/sns/)
- [AWS disaster recovery whitepaper](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
