# 29 - SAA-C03 Practice Questions and Rationales

## Why This Chapter Matters

Practice questions are useful only when the reasoning is explicit. The goal is not to memorize "S3 plus CloudFront" or "ALB plus ASG." The goal is to recognize the requirement chain that makes one option better than the others.

Source snapshot: 2026-05-27. Verify service details against current AWS docs before exam booking.

## How to Use These Questions

For each question:

1. Identify the dominant requirement.
2. Eliminate answers that violate a hard constraint.
3. Choose the simplest architecture that satisfies the requirement.
4. Read the rationale even if you got the answer right.

## Questions

### Question 1: Private S3 Access

A company runs EC2 instances in private subnets. The instances must download large files from Amazon S3 without traversing the public internet. The company also wants to reduce NAT Gateway data processing costs. What should a solutions architect recommend?

A. Add an internet gateway and assign public IPs to the instances.

B. Use an S3 gateway VPC endpoint and update route tables.

C. Use an Application Load Balancer in front of S3.

D. Move the instances to a public subnet and restrict security groups.

Answer: B.

Reasoning:

The hard clues are private S3 access and NAT cost reduction. An S3 gateway endpoint provides private connectivity to S3 from the VPC and avoids sending S3 traffic through NAT. Public IPs and public subnets violate the private-access requirement. ALB is not a proxy for S3 access from private instances.

### Question 2: Shared Linux File Storage

An application runs on multiple EC2 instances across two Availability Zones. All instances must read and write to the same shared Linux file system. Which storage service best fits?

A. Amazon EBS volume attached to all instances.

B. Amazon EFS file system mounted by the instances.

C. EC2 instance store replicated with a cron job.

D. Amazon S3 mounted as a POSIX file system for writes.

Answer: B.

Reasoning:

The hard clues are shared Linux file system and multiple AZs. EFS is the common managed NFS-style file system for Linux workloads across AZs. EBS is block storage and AZ-scoped. Instance store is ephemeral. S3 is object storage, not a general POSIX write filesystem.

### Question 3: High Availability Web Tier

A web application currently runs on one EC2 instance and is unavailable during instance failure. The company wants automatic recovery and high availability across Availability Zones. Which design is best?

A. Create an AMI and manually launch a replacement during failure.

B. Place instances in an Auto Scaling group across multiple AZs behind an Application Load Balancer.

C. Use one larger EC2 instance with more CPU and memory.

D. Use an Elastic IP address and remap it manually during failure.

Answer: B.

Reasoning:

The requirement is automatic recovery and HA across AZs. ALB + ASG across AZs provides health checks, replacement, and traffic distribution. A larger instance improves vertical capacity but not high availability. Manual replacement/remap does not meet automatic recovery.

### Question 4: Ordered Message Processing

A financial application must process payment events exactly in the order they are submitted for each payment group. Which service should be considered first?

A. Amazon SQS FIFO queue.

B. Amazon SQS standard queue.

C. Amazon SNS topic with multiple subscribers.

D. Amazon EventBridge default bus.

Answer: A.

Reasoning:

The dominant clue is ordering. SQS FIFO supports ordering within message groups and deduplication features. Standard SQS gives high throughput but not strict ordering. SNS and EventBridge are event-routing services, not the primary answer for ordered queue processing.

### Question 5: Static Website With Global Low Latency

A company hosts static assets in S3. Users are global and complain about latency. The company wants low operational overhead. What should be added?

A. CloudFront distribution with S3 as origin.

B. EC2 instances in every Region.

C. RDS read replicas.

D. Site-to-Site VPN.

Answer: A.

Reasoning:

Static assets + global latency + low overhead points to CDN. CloudFront caches content at edge locations and reduces origin load. EC2 in every Region increases operations. RDS and VPN do not solve static asset latency.

### Question 6: Database Read Scaling

An application uses Amazon RDS for a relational database. The primary database is healthy but read queries are overwhelming it. The application can tolerate slightly stale reads for reporting pages. What should be recommended?

A. Add RDS read replicas and send reporting reads to replicas.

B. Enable Multi-AZ only.

C. Move all data to EBS.

D. Put the database in a public subnet.

Answer: A.

Reasoning:

The problem is read scaling with tolerance for replica lag. Read replicas offload reads. Multi-AZ improves availability/failover, not read scale in the normal SAA pattern. EBS and public subnet do not solve query pressure.

### Question 7: Lowest Operational Overhead for Event Image Processing

Users upload images to S3. Each upload must trigger a resize operation and store a thumbnail. Traffic is spiky. The company wants minimal server management. Which architecture fits?

A. S3 event notification to Lambda, storing thumbnails back in S3.

B. EC2 instance polling S3 every minute.

C. On-premises server with VPN to S3.

D. Manually run a script once per day.

Answer: A.

Reasoning:

The clues are event-driven, spiky traffic, and minimal server management. S3 events plus Lambda is the standard serverless pattern. Polling EC2 adds operations and delay. On-premises and manual scripts violate the requirement.

### Question 8: Disaster Recovery With Low Cost and Higher RTO

A rarely used internal system must be recoverable in another Region. The company can tolerate several hours of downtime and some restore time, but wants low ongoing cost. Which DR strategy fits best?

A. Backup and restore.

B. Active/active multi-Region.

C. Warm standby with full duplicate capacity.

D. Global Accelerator active routing to both Regions.

Answer: A.

Reasoning:

Several hours of downtime and low cost point to backup and restore. Active/active and warm standby reduce RTO but increase cost. Global Accelerator does not replace data/application recovery planning.

### Question 9: Protecting S3 From Accidental Public Access

A company stores confidential reports in S3. They want to prevent accidental public exposure across buckets. Which control should be enabled?

A. S3 Block Public Access.

B. EC2 security group.

C. Auto Scaling group.

D. NAT Gateway.

Answer: A.

Reasoning:

The resource is S3 and the risk is public exposure. S3 Block Public Access is specifically designed to block public access settings at account/bucket levels. EC2 security groups do not protect S3 bucket policy exposure.

### Question 10: Hybrid Connectivity With Consistent Private Bandwidth

A company needs consistent private network connectivity from an on-premises data center to AWS for steady high-volume traffic. Which option is most appropriate?

A. AWS Direct Connect.

B. Public internet with no VPN.

C. S3 Transfer Acceleration.

D. CloudFront.

Answer: A.

Reasoning:

Consistent private hybrid connectivity points to Direct Connect. VPN can be useful, but the question emphasizes consistent private bandwidth for steady high-volume traffic. CloudFront and Transfer Acceleration solve different edge/data-transfer patterns.

### Question 11: Asynchronous Backend Protection

A checkout service receives bursts of requests. Inventory updates can be processed asynchronously. The backend occasionally fails on malformed messages, and failed messages must be retained for analysis. Which design is best?

A. Put SQS between checkout and inventory workers, configure a DLQ, and scale workers.

B. Call inventory synchronously from checkout and retry forever.

C. Store failed messages only in application logs.

D. Replace the database with a larger instance.

Answer: A.

Reasoning:

The clues are burst absorption, asynchronous processing, and failed-message retention. SQS decouples, consumers scale independently, and DLQ captures poison messages. Synchronous retries can amplify failure.

### Question 12: Reducing Repeated Database Reads

A read-heavy application repeatedly queries the same user profile data from a relational database. The data can be cached briefly. What should be added?

A. ElastiCache.

B. NAT Gateway.

C. AWS Snowball.

D. IAM Identity Center.

Answer: A.

Reasoning:

Repeated read-heavy access with cacheable data points to a cache. ElastiCache can reduce database load and latency. The other services solve unrelated problems.

## Small Details That Matter Later

- Read the word "must." It often marks the hard requirement.
- "Least operational overhead" usually rejects self-managed EC2-heavy designs.
- "Private" usually rejects public subnet or public internet answers.
- "Ordered" usually rejects standard SQS.
- "Shared file system" usually rejects EBS.
- "Static global content" usually points to CloudFront.
- "Read scaling" is not the same as failover.
- "Low cost DR with hours of downtime" is not active/active.
- "Strict RPO/RTO" usually requires replication and tested failover.

## Answers and Reasoning Summary

| Question | Answer | Dominant clue |
| --- | --- | --- |
| 1 | S3 gateway endpoint | Private S3 access and NAT cost |
| 2 | EFS | Shared Linux file system across AZs |
| 3 | ALB + ASG | Automatic HA across AZs |
| 4 | SQS FIFO | Ordered processing |
| 5 | CloudFront | Global static content latency |
| 6 | Read replicas | Read scaling |
| 7 | S3 event + Lambda | Event-driven low ops |
| 8 | Backup and restore | Low cost, higher RTO |
| 9 | S3 Block Public Access | Prevent public S3 exposure |
| 10 | Direct Connect | Consistent private hybrid connectivity |
| 11 | SQS + DLQ | Async burst absorption and failed-message retention |
| 12 | ElastiCache | Cache repeated reads |

## Connected Topics

- [28 - SAA-C03 Alignment Audit and Scenario Playbook](28%20-%20SAA-C03%20Alignment%20Audit%20and%20Scenario%20Playbook.md)
- [30 - SAA-C03 Rapid Revision Cheatsheet and Glossary](30%20-%20SAA-C03%20Rapid%20Revision%20Cheatsheet%20and%20Glossary.md)

## Chapter Summary

SAA practice is useful when every answer is tied to a requirement. The best answer is not the flashiest service; it is the service combination that satisfies the exact security, resilience, performance, cost, and operational constraints in the question.
