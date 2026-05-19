# AWS Solution Architect

## Quick Summary

AWS Solutions Architect notes focus on designing secure, resilient, high-performing, and cost-optimized systems on AWS. This folder covers core SAA topics across identity, compute, storage, networking, databases, messaging, containers, serverless, monitoring, security, analytics, machine learning, and disaster recovery.

These notes are written for beginner-to-SAA progression: first learn the AWS building blocks, then learn how to choose between services based on requirements, tradeoffs, reliability, security, performance, and cost.

## Learning Order

| Order | Note | Focus |
| --- | --- | --- |
| 1 | [Getting Started with AWS](1%20-%20Getting%20Started%20with%20AWS.md) | Regions, AZs, edge locations, region choice, Well-Architected starter thinking. |
| 2 | [IAM and AWS CLI](2%20-%20IAM%20and%20AWS%20CLI.md) | IAM users, groups, policies, MFA, roles, CLI, credentials report, access advisor. |
| 3 | [EC2 Fundamentals](3%20-%20EC2%20Fundamentals.md) | EC2 sizing, instance types, purchasing options, storage, networking, security. |
| 4 | [EC2 Solutions Architect Associate Level](4%20-%20EC2%20Solutions%20Architect%20Associate%20Level.md) | Private/public IPs, Elastic IPs, placement groups, ENI, hibernate. |
| 5 | [EC2 Instance Storage](5%20-%20EC2%20Instance%20Storage.md) | EBS, snapshots, AMIs, instance store, EFS, EBS types, encryption, EFS vs EBS. |
| 6 | [High Availability and Scalability ELB and ASG](6%20-%20High%20Availability%20and%20Scalability%20ELB%20and%20ASG.md) | HA, scalability, ALB/NLB/GWLB, health checks, ASG, scaling policies, troubleshooting. |
| 7 | [AWS Databases: RDS, Aurora and ElastiCache](7%20-%20AWS%20Databases%20-%20RDS%2C%20Aurora%20and%20ElastiCache.md) | Relational databases, Aurora, read replicas, Multi-AZ, caching, common database patterns. |
| 8 | [Route 53](8%20-%20Route%2053.md) | DNS, hosted zones, records, routing policies, health checks, domain registration. |
| 9 | [Classic Solutions Architect Discussions](9%20-%20Classic%20Solutions%20Architect%20Discussions.md) | Common SAA architecture patterns and tradeoff discussions. |
| 10 | [Amazon S3 Introduction](10%20-%20Amazon%20S3%20Introduction.md) | Buckets, objects, prefixes, storage classes, static hosting, lifecycle basics. |
| 11 | [Advanced - Amazon S3](11%20-%20Advanced%20-%20Amazon%20S3.md) | Versioning, replication, lifecycle, events, performance, Object Lock, Glacier restore. |
| 12 | [Amazon S3 Security](12%20-%20Amazon%20S3%20Security.md) | Block Public Access, bucket policies, IAM, ACLs, encryption, access points, logs. |
| 13 | [CloudFront and AWS Global Accelerator](13%20-%20CloudFront%20and%20AWS%20Global%20Accelerator.md) | CDN, edge caching, origins, OAC/OAI, invalidations, anycast acceleration. |
| 14 | [AWS Storage Extras](14%20-%20AWS%20Storage%20Extras.md) | EFS, FSx variants, AWS Backup, shared file storage decisions. |
| 15 | [AWS Storage Transfer and Migration](15%20-%20AWS%20Storage%20Transfer%20and%20Migration.md) | DataSync, Transfer Family, Snow Family, Storage Gateway, migration planning. |
| 16 | [Decoupling Applications: SQS, SNS, Kinesis and Amazon MQ](16%20-%20Decoupling%20Applications%20-%20SQS%2C%20SNS%2C%20Kinesis%20and%20Amazon%20MQ.md) | Queues, pub/sub, streams, brokers, DLQs, fanout, idempotency. |
| 17 | [Containers on AWS: ECS, Fargate, ECR, EKS](17%20-%20Containers%20on%20AWS%20-%20ECS%2C%20Fargate%2C%20ECR%2C%20EKS.md) | Image registry, ECS, Fargate, EKS, IAM roles, networking, deployments. |
| 18 | [Serverless Overview from Solutions Architect Perspective](18%20-%20Serverless%20Overview%20from%20Solutions%20Architect%20Perspective.md) | Lambda, API Gateway, DynamoDB, EventBridge, Step Functions, serverless tradeoffs. |
| 19 | [Serverless Solutions Architect Discussions](19%20-%20Serverless%20Solutions%20Architect%20Discussions.md) | Serverless patterns, workflows, retries, idempotency, errors, observability. |
| 20 | [Databases in AWS](20%20-%20Databases%20in%20AWS.md) | Purpose-built database selection across RDS, Aurora, DynamoDB, Redshift, OpenSearch, and specialized databases. |
| 21 | [Data and Analytics](21%20-%20Data%20%26%20Analytics.md) | S3 data lakes, Glue, Athena, Redshift, EMR, Kinesis, QuickSight, Lake Formation. |
| 22 | [Machine Learning](22%20-%20Machine%20Learning.md) | SageMaker, AI services, Bedrock, batch vs real-time inference, ML service selection. |
| 23 | [AWS Monitoring and Audit: CloudWatch, CloudTrail and Config](23%20-%20AWS%20Monitoring%20and%20Audit%20-%20CloudWatch%2C%20CloudTrail%20and%20Config.md) | Metrics, logs, alarms, API audit, configuration compliance, flow logs. |
| 24 | [Identity and Access Management (IAM) - Advanced](24%20-%20Identity%20and%20Access%20Management%20%28IAM%29%20-%20Advanced.md) | Policy evaluation, roles, STS, cross-account access, boundaries, SCPs, federation. |
| 25 | [AWS Security and Encryption: KMS, SSM Parameter Store, Shield and WAF](25%20-%20AWS%20Security%20and%20Encryption%20-%20KMS%2C%20SSM%20Parameter%20Store%2C%20Shield%20and%20WAF.md) | KMS, Parameter Store, Secrets Manager, WAF, Shield, GuardDuty, Inspector, Security Hub. |
| 26 | [Networking VPC](26%20-%20Networking%20VPC.md) | VPCs, CIDR, subnets, route tables, NAT, endpoints, peering, Transit Gateway, VPN, Direct Connect. |
| 27 | [Disaster Recovery and Management](27%20-%20Disaster%20Recovery%20%26%20Management.md) | RTO/RPO, backup/restore, pilot light, warm standby, active/active, DR testing. |

## Study Tips

- After each service note, ask: when should I choose this service, and when should I not choose it?
- Keep a personal table of "requirement clues" such as shared Linux files -> EFS, ordered queue -> FIFO SQS, full-text search -> OpenSearch, regional DR -> cross-Region replication.
- For architecture questions, identify the bottleneck or risk first: availability, performance, security, cost, migration effort, or operations.
- Re-check official docs before exam booking because AWS service features and exam guides change.

## Exam Orientation

Checked against the AWS SAA-C03 official exam guide on 2026-05-18. Re-check before booking because AWS updates exam guides and services over time.

High-level SAA themes:

- Secure architectures.
- Resilient architectures.
- High-performing architectures.
- Cost-optimized architectures.

## Official References

- AWS Certified Solutions Architect Associate guide: <https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html>
- SAA-C03 official exam guide PDF: <https://d1.awsstatic.com/training-and-certification/docs-sa-assoc/AWS-Certified-Solutions-Architect-Associate_Exam-Guide.pdf>
- AWS Global Infrastructure: <https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html>
- AWS Well-Architected Framework: <https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html>
