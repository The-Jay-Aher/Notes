# 30 - SAA-C03 Rapid Revision Cheatsheet and Glossary

## Purpose

This file is a final-pass revision sheet for AWS Solutions Architect Associate. It compresses the service notes into decision clues, traps, and glossary terms.

Source snapshot: 2026-05-27. AWS service capabilities and certification guides change; recheck official docs before exam booking.

## Exam Domain Snapshot

| Domain | Weight | Core question |
| --- | ---: | --- |
| Secure architectures | 30% | Who can access what, through which network path, and under which encryption/policy controls? |
| Resilient architectures | 26% | What fails, how quickly do we recover, and how much data can be lost? |
| High-performing architectures | 24% | Which service pattern meets latency, throughput, scale, and access-pattern needs? |
| Cost-optimized architectures | 20% | What is the least wasteful option that still meets requirements? |

## Service Decision Clues

| Requirement clue | Likely answer |
| --- | --- |
| Static global content | S3 + CloudFront |
| Dynamic HTTP routing | ALB |
| Ultra-low latency static/dynamic edge acceleration to AWS endpoints | Global Accelerator |
| TCP/UDP high performance load balancing | NLB |
| Private S3 access from VPC | S3 gateway endpoint |
| Private access to many AWS services through ENI | Interface VPC endpoint / PrivateLink |
| Shared Linux file system | EFS |
| EC2 block storage | EBS |
| Temporary high IOPS local disk | Instance store |
| Object storage | S3 |
| Long-term archive | S3 Glacier storage classes |
| Relational managed database | RDS or Aurora |
| Read scaling relational DB | Read replicas / Aurora replicas |
| Relational HA failover | Multi-AZ / Aurora cluster design |
| Key-value serverless database | DynamoDB |
| In-memory cache | ElastiCache / MemoryDB depending durability requirements |
| Async queue | SQS |
| Pub/sub fanout | SNS to SQS/Lambda/etc. |
| Event routing | EventBridge |
| Streaming records | Kinesis or MSK depending requirements |
| Serverless function | Lambda |
| Workflow orchestration | Step Functions |
| Container orchestration with AWS-managed control plane | ECS/EKS depending ecosystem |
| Consistent private hybrid connectivity | Direct Connect |
| Encrypted secret value | Secrets Manager or SSM Parameter Store depending rotation/use case |
| Centralized audit of API calls | CloudTrail |
| Metrics and alarms | CloudWatch |
| Resource configuration compliance | AWS Config |

## Common Elimination Rules

- If the question says "no public internet," eliminate public subnet/public IP/NAT-only paths where a private endpoint is the intended answer.
- If the question says "least operational overhead," eliminate self-managed clusters/servers when a managed/serverless option directly fits.
- If the question says "ordered messages," eliminate standard SQS.
- If the question says "shared file system," eliminate EBS unless the question is single-node block storage.
- If the question says "survive AZ failure," eliminate single-AZ designs.
- If the question says "survive Region failure," eliminate only Multi-AZ.
- If the question says "read scaling," do not choose Multi-AZ alone.
- If the question says "cost optimized and interruptible," consider Spot.
- If the question says "steady predictable compute," consider Savings Plans or Reserved Instances.
- If the question says "rarely accessed archive," consider lifecycle to Glacier storage classes.

## Architecture Pattern Cheatsheet

### Secure Web Application

```text
Route 53 -> CloudFront/WAF -> ALB -> private EC2/ECS/Lambda integration -> private database
IAM roles, security groups, KMS, Secrets Manager, CloudTrail
```

### Highly Available EC2 Application

```text
ALB across AZs -> ASG across AZs -> stateless app instances -> RDS Multi-AZ or distributed data store
```

### Async Worker System

```text
producer -> SQS -> worker ASG/Lambda -> database
failed messages -> DLQ
```

### Serverless API

```text
API Gateway -> Lambda -> DynamoDB
CloudWatch logs/metrics, IAM role, retries, idempotency
```

### Static Website

```text
S3 origin -> CloudFront -> Route 53
private bucket access through OAC where applicable
```

### Multi-Region DR

```text
backup/restore -> pilot light -> warm standby -> active/active
cost and complexity increase as RTO/RPO decrease
```

## Small Details That Matter Later

- Security groups are stateful; NACLs are stateless.
- Explicit deny beats allow.
- IAM role on EC2 avoids long-term keys.
- S3 Block Public Access can override public bucket policies/ACL-style exposure.
- KMS key policy matters in addition to IAM.
- CloudFront caches at edge; invalidations can cost and take time.
- ALB operates at Layer 7; NLB operates at Layer 4.
- NAT Gateway is AZ-scoped and charged hourly plus data processing.
- Gateway endpoints exist for S3 and DynamoDB; many other services use interface endpoints.
- EBS snapshots are stored in S3-managed infrastructure but are used through EBS APIs.
- EBS is AZ-scoped; snapshots are regional.
- EFS can be mounted from multiple AZs.
- DynamoDB partition key design controls scalability and hot-partition risk.
- SQS visibility timeout must exceed processing time or messages can reappear.
- DLQ is for poison-message analysis, not automatic business correction.
- Lambda concurrency can protect downstream systems but can also throttle workloads.
- RTO is time to recover; RPO is data-loss tolerance.

## Glossary

### Availability Zone

One or more discrete data centers with independent power, networking, and connectivity inside a Region. Multi-AZ design survives many single-AZ failures.

### Edge Location

AWS edge site used by services such as CloudFront to bring content closer to users.

### IAM Role

Identity with permissions that can be assumed by AWS services, users, or external identities. For workloads, roles avoid long-term keys.

### Resource Policy

Policy attached to a resource, such as S3 bucket policy, KMS key policy, SQS queue policy, or Lambda resource policy.

### SCP

Service Control Policy in AWS Organizations. Sets maximum permissions boundary for accounts/OUs; it does not grant permissions by itself.

### VPC Endpoint

Private connection from a VPC to supported AWS services. Gateway endpoints are used for S3/DynamoDB; interface endpoints use ENIs and PrivateLink.

### NAT Gateway

Managed service that lets private subnet resources initiate outbound IPv4 internet access. Watch cost and AZ placement.

### ALB

Application Load Balancer for HTTP/HTTPS routing, host/path rules, and Layer 7 features.

### NLB

Network Load Balancer for high-performance TCP/UDP/TLS Layer 4 traffic.

### RTO

Recovery Time Objective: how long recovery may take.

### RPO

Recovery Point Objective: how much data loss is acceptable.

### Read Replica

Database replica used to offload reads and sometimes support DR patterns. It is not the same as Multi-AZ failover.

### Multi-AZ

Design spanning multiple Availability Zones in one Region. Usually improves availability, not global latency.

### Multi-Region

Design spanning multiple AWS Regions. Used for regional DR or global latency needs, with higher complexity/cost.

### DLQ

Dead-letter queue that stores messages that could not be processed successfully after retries.

## Final Question Checklist

Before choosing an answer, ask:

1. Is the workload public or private?
2. Is the dominant issue security, resilience, performance, or cost?
3. Is the workload synchronous, asynchronous, streaming, batch, or event-driven?
4. Is the data object, block, file, relational, key-value, graph, document, cache, or stream?
5. What failure must be survived: instance, AZ, Region, network, application, or data loss?
6. What is the operational-overhead requirement?
7. What answer violates a hard word such as "must," "private," "least," "ordered," or "shared"?
