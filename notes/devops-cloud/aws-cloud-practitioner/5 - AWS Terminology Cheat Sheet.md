# 5 - AWS Terminology Cheat Sheet

## Quick Summary

This cheat sheet is for fast AWS vocabulary revision. Use it before practice tests or interviews to quickly recall what each service or term means. It is intentionally shorter than the main notes; for deeper explanation, use the related AWS Cloud Practitioner and Solutions Architect notes.

## How To Use

- Read the term.
- Say the one-line meaning out loud.
- Ask: "When would I use this, and when would I not?"
- Link the term back to a real architecture pattern.

## A

- **Access Control List (ACL):** Rule set used to allow/deny network traffic at the subnet layer (NACL in VPC context).
- **Amazon Aurora:** AWS-managed relational database engine compatible with MySQL/PostgreSQL patterns and designed for cloud performance/availability.
- **Amazon CloudWatch Logs:** Log collection and query service within CloudWatch.
- **Amazon EventBridge:** Event bus service for routing events between AWS services, SaaS apps, and custom applications.
- **Amazon Machine Image (AMI):** Template used to launch EC2 instances.
- **Amazon Resource Name (ARN):** Standard AWS identifier for resources.
- **Auto Scaling:** Automatically adjusts compute capacity based on demand and health policies.
- **Availability Zone (AZ):** Isolated infrastructure location inside an AWS Region.
- **AWS Account:** Security, billing, and resource boundary.
- **AWS Organizations:** Service for centrally managing multiple AWS accounts.
- **AWS Support Plans:** Support tiers that provide different levels of technical/account support.

## B

- **Bucket (S3):** Top-level container for objects in Amazon S3.
- **Budget:** AWS cost control feature that alerts when cost/usage crosses thresholds.

## C

- **CapEx:** Capital expenditure; upfront investment in physical infrastructure.
- **CloudFront:** AWS content delivery network (CDN) that serves content from edge locations.
- **CloudFormation:** AWS Infrastructure as Code service for provisioning resources from templates.
- **CloudTrail:** Records API activity and governance events in an AWS account.
- **CloudWatch:** Monitoring/observability service for metrics, logs, alarms, and dashboards.
- **CodeBuild:** Managed build service.
- **CodeDeploy:** Deployment automation service.
- **CodePipeline:** CI/CD orchestration service.
- **Consolidated Billing:** Centralized billing for multiple AWS accounts under AWS Organizations.

## D

- **DataSync:** Service for moving data between on-premises storage and AWS storage services.
- **DNS (Domain Name System):** Translates domain names into IP addresses.
- **DynamoDB:** Fully managed NoSQL key-value/document database.

## E

- **EC2 Auto Scaling Group (ASG):** Group that maintains and scales EC2 instance capacity.
- **EBS (Elastic Block Store):** Persistent block storage volumes for EC2.
- **EC2 (Elastic Compute Cloud):** Virtual servers in AWS.
- **EFS (Elastic File System):** Managed NFS file system for Linux workloads.
- **ELB (Elastic Load Balancing):** Distributes incoming traffic across multiple targets.
- **ElastiCache:** Managed in-memory caching service (Redis/Memcached).
- **Elastic Beanstalk:** Platform service for deploying applications without manually managing all infrastructure pieces.
- **Elastic IP (EIP):** Static public IPv4 address allocated to an AWS account.
- **Elasticity:** Ability to scale resources up and down quickly with demand.

## F

- **Fault Tolerance:** Ability to continue operating despite component failures.
- **Firewall:** Traffic filtering control to allow/block network access.
- **FSx:** Managed file systems for workloads such as Windows File Server, Lustre, NetApp ONTAP, and OpenZFS.

## H

- **High Availability:** Design approach to minimize downtime and maintain service continuity.
- **HPC:** High Performance Computing; tightly coupled workloads needing high compute/network performance.

## I

- **IAM (Identity and Access Management):** Service for users, roles, policies, and access control.
- **IAM Policy:** JSON permission document.
- **IAM Role:** Temporary-assumable identity with permissions.
- **IAM User:** Identity representing a person or workload with credentials/permissions.
- **Internet Gateway:** VPC component that allows internet-routable traffic for public subnets.

## L

- **Lambda:** Serverless compute service for event-driven functions.
- **Least Privilege:** Give only required permissions.
- **Load Balancer:** Service that distributes traffic across targets.

## O

- **Object Availability (S3):** Percentage likelihood an object can be accessed when requested.
- **Object Durability (S3):** Probability an object remains intact over time.
- **Object Lifecycle (S3):** Rules to transition/expire objects automatically.
- **Object Versioning (S3):** Keeps multiple versions of objects in a bucket.
- **OpEx:** Operational expenditure; pay-as-you-use operating cost.

## P

- **Principle of Least Privilege:** Grant only the permissions required to perform a task.
- **Publisher (SNS):** Entity that sends messages to an SNS topic.

## R

- **Region:** Geographic AWS infrastructure area containing multiple Availability Zones.
- **RDS (Relational Database Service):** Managed relational database service.
- **Redshift:** Managed data warehouse service for analytics.
- **Role (IAM):** Identity with permissions that can be assumed temporarily.
- **Route 53:** AWS DNS and domain registration service.

## S

- **Scalability:** Ability to handle increased load by adding resources efficiently.
- **Security Group:** Stateful firewall attached to ENIs/instances.
- **Shared Responsibility Model:** Defines AWS vs customer security responsibilities.
- **SNS (Simple Notification Service):** Pub/sub messaging and fan-out notifications.
- **SQS (Simple Queue Service):** Managed message queue service for decoupling applications.
- **S3 (Simple Storage Service):** Scalable object storage service.
- **Storage Class (S3):** Tier defining object cost/performance/retrieval characteristics.
- **Subnet:** Logical range of IP addresses in a VPC.
- **Subscription (SNS):** Endpoint registration that receives messages from a topic.

## T

- **Topic (SNS):** Communication channel for publishing messages to subscribers.
- **Trusted Advisor:** AWS recommendation service for best practices.
- **Transit Gateway:** Hub service for connecting VPCs and on-premises networks.

## U

- **User Credentials:** Authentication material (for example password or access keys).

## V

- **VPC (Virtual Private Cloud):** Isolated virtual network environment in AWS.

## W

- **WAF (Web Application Firewall):** Service that filters HTTP(S) requests using web ACL rules.
- **Well-Architected Framework:** AWS design framework with six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.
