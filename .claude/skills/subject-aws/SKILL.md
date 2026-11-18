---
name: subject-aws
description: Coverage and teaching requirements for AWS Architecture, AWS Solutions Architect Associate, AWS Solutions Architect Professional and AWS Cloud Practitioner in this vault - the service checklist, the per-service explanation checklist, and how to drill scenario-based exam questions. Load it whenever creating, upgrading, teaching or quizzing anything about AWS services, AWS architecture or AWS certifications, together with deep-notes (writing) or teach/quiz/revise (learning).
---

# AWS Architecture and Certifications

Folders: `notes/devops-cloud/aws-solutions-architect-associate/`, `notes/devops-cloud/aws-solutions-architect-professional/`, `notes/devops-cloud/aws-cloud-practitioner/`, plus `notes/devops-cloud/aws-architecture/` if a general architecture track is created.

Version assumption: AWS services, limits, prices and exam guides change often. Name the exam guide version a note follows, and mark limits, quotas, prices and feature availability as "verify against current AWS docs".

## What the notes must cover

- **Foundations:** cloud computing from first principles; regions; availability zones; edge locations.
- **Identity and governance:** IAM; Organizations; accounts; multi-account architecture; CloudTrail; Config.
- **Networking:** VPC; subnets; route tables; internet gateways; NAT gateways; VPC endpoints; security groups; NACLs; hybrid networking; Direct Connect; VPN; Transit Gateway; Route 53; CloudFront.
- **Compute:** EC2; AMI; Lambda; ECS; EKS; Auto Scaling; ELB.
- **Storage:** EBS; EFS; S3; Glacier storage classes.
- **Databases and caching:** RDS; Aurora; DynamoDB; ElastiCache.
- **Integration:** API Gateway; SQS; SNS; EventBridge; Step Functions.
- **Security:** KMS; Secrets Manager; Systems Manager; security architecture.
- **Operations:** CloudWatch; disaster recovery; backup; high availability; fault tolerance; cost optimization; migration.
- **Design judgement:** Well-Architected Framework; professional-level tradeoff scenarios.

## For every AWS service, explain

- what it does
- why it exists
- when to use it
- when not to use it
- common architecture patterns
- limits and constraints
- pricing traps
- security implications
- high availability behavior
- failure modes
- exam traps
- real-world design decisions

AWS notes must include scenario-based questions, because AWS exams love asking questions like a committee tried to hide the answer under three layers of billing anxiety.

## Teaching and quizzing AWS

- **Teach the requirement words.** Exam scenarios turn on phrases such as "least operational overhead", "most cost-effective", "highly available", "minimal code changes" and "near real-time". Before the student picks an answer, make them underline the phrase that decides it and say what it rules out.
- **Every quiz question explains every option.** The student learns as much from why the two plausible distractors are wrong as from why the answer is right. Ask the student to eliminate options before choosing.
- **Draw the request path.** For networking and architecture questions, have the student trace a packet or request: client → Route 53 → CloudFront → ELB → instance or task, and on through routes, security groups and NACLs. Most networking mistakes show up as a wrong step in that trace.
- **Use compare-and-contrast drills** for confusable pairs: SQS vs SNS vs EventBridge, EBS vs EFS vs S3, security groups vs NACLs, gateway vs interface endpoints, RDS Multi-AZ vs read replicas, Aurora vs RDS.
- **Associate vs Professional.** Associate questions test whether the student picks the right service. Professional questions test tradeoffs across accounts, migration, cost and organizational constraints, so make the student justify the second-best option too.
