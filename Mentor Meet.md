# Mentor Meet Notes

## Career in DevOps

Goal: Build a strong DevOps career path with focused, practical progression.

### Core Foundation Topics (Priority)

1. Compute
2. Networking
3. Storage
4. Databases
5. Linux and scripting fundamentals

## Current Progress

### AWS

- Studying compute, storage, networking, and database concepts.
- Core AWS foundation topics are mostly covered.

### Linux

- Completed basic commands.
- Practiced some advanced commands.

### Shell/Python

- Completed shell basics.
- Able to write simple shell programs.

### Terraform

- Started learning from Zeal Vora + freeCodeCamp.
- Many concepts are new; currently in early learning stage.

### Networking Concepts

- Started, but still in progress.

## Suggested Learning Sequence

Focus on the first five concepts before moving further:

1. AWS fundamentals (compute, storage, networking, database)
2. Linux
3. Shell scripting / Python basics
4. Terraform basics
5. Networking fundamentals

Then continue with:

6. Jenkins
7. Git
8. Build tools (Maven / Gradle / Ant / MSBuild)
9. Docker
10. Kubernetes (K8s)
11. Azure Pipelines
12. AWS CodeBuild

## Certification Plan

- Prepare for AWS Cloud Practitioner.
- Prepare for HashiCorp Terraform Associate.

## To-Dos Before Tuesday Meeting

1. EC2 User Data check
    - Software files are present, but app/page could not be opened using public IP initially.
    - Current status: mostly resolved; verify final service and security configuration again.
2. Create AMI - Done
3. Create snapshots and review Recycle Bin usage - Done
4. Load Balancer (ALB and NLB) - Done
5. Auto Scaling Groups - Done
6. S3 buckets - Done
7. Host static website using S3 - Done
8. Blacklisting/Whitelisting concepts (EC2/S3) - Done
9. VPC networking concepts - Done
10. Security Group rules - Done
11. Key pair + Port 22 (SSH) access - Done

## Doubts / Questions

1. Is EFS created per VPC, or is it tied separately to private/public subnets?
2. What is virtual tape used for, and when should it be used (compared with EBS/EFS)?
3. What is default tenancy in AWS?
4. When is the right time to attempt the AWS Cloud Practitioner exam?
5. AWS CloudShell issue seen earlier:
    - Error: `Timed out while opening the session`
    - It failed for around one hour, then started working again.

## Before Saturday Meeting

- Types of Load Balancer - Done
- VPC components / networking concepts - Done
- Route 53 and CDN (PoP, endpoint, edge locations) - Done
- Monitoring services overview - Done
    - CloudWatch
    - CloudTrail
    - Trusted Advisor
- Terraform practice: 30-60 minutes daily - In progress (reading docs)
- CloudFormation alongside Terraform - Read and tested (working)

Reference note:

- Mentor Meet recorded on Thursday, May 30, 2024 at 4:10 PM

## Tasks for Next 2 Weeks

1. Organize Terraform modules and files by clear folder/module structure.
2. Configure EC2 via CloudFormation while monitoring deployment events.
3. Revise Read Replica concepts and database services (RDS, DynamoDB).
4. Revisit disaster recovery mechanisms and architecture patterns.
5. Understand AWS WAF deeply.
6. Practice custom IAM policies, RBAC concepts, and roles.
7. CertyIQ practice cadence:
    - 25-question rounds multiple times
    - then 50-question rounds
    - then 100-question rounds as often as possible

## After Exam Project

Design and document a cost-optimized, highly scalable 3-tier AWS application using Terraform.

Include:

- EC2
- Load Balancer
- Auto Scaling Group
- S3
- VPC
- Database layer
- Static website hosting element (if applicable)
- Disaster recovery approach

Also create a cost estimate using AWS Pricing Calculator:

- https://calculator.aws/#/addService
