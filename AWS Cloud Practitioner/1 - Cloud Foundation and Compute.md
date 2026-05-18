# 1 - Foundations of Cloud Computing and Compute

## Cloud Computing Basics

Cloud computing is the on-demand delivery of IT resources (compute, storage, networking, databases, and more) over the internet, with pay-as-you-go pricing.

### CapEx vs OpEx

- **CapEx (Capital Expenditure):** Large upfront investment in physical infrastructure.
- **OpEx (Operational Expenditure):** Pay for resources as you use them.

### Benefits of Cloud Computing

- **High availability:** Build resilient systems across multiple infrastructure locations.
- **Elasticity:** Scale resources up or down quickly based on demand.
- **Agility:** Launch resources in minutes instead of waiting for hardware procurement.
- **Durability:** Data can be replicated across multiple systems/facilities for long-term reliability.

## Cloud Service Models

- **IaaS (Infrastructure as a Service):** You manage OS, applications, and data; provider manages hardware.
  - Example: Amazon EC2
- **PaaS (Platform as a Service):** Provider manages infrastructure + platform; you focus on code/data.
  - Example: AWS Elastic Beanstalk
- **SaaS (Software as a Service):** Fully managed software delivered over the internet.
  - Example: Productivity or CRM web apps

## Cloud Deployment Models

- **Public cloud:** Infrastructure owned and operated by cloud provider.
- **Private cloud:** Cloud environment dedicated to a single organization.
- **Hybrid cloud:** Combination of on-premises/private and public cloud.

## AWS Global Infrastructure

### Regions and Availability Zones (AZs)

- **AWS Region:** A physical geographic area in the world (for example, `us-east-1`).
- **Availability Zone:** One or more physically separate data centers inside a Region, each with independent power/networking.
- A Region contains **multiple AZs** (typically at least three, though this can vary by Region).

Why this matters:

- Designing across multiple AZs improves fault tolerance and high availability.
- Choosing a Region closer to users helps reduce latency.

### Latency

Latency is the delay between a request and a response. Lower latency generally improves user experience.

### Local Zones

- Extend AWS infrastructure closer to end users in major metro areas.
- Useful for latency-sensitive workloads such as media rendering, real-time gaming, and virtual desktops.

### Edge Locations

- Primarily used by services like Amazon CloudFront.
- Cache content near users to reduce latency and improve delivery performance.

## AWS Well-Architected Framework (6 Pillars)

1. Operational Excellence
2. Security
3. Reliability
4. Performance Efficiency
5. Cost Optimization
6. Sustainability

## AWS Cloud Adoption Framework (CAF) - Common Journey Phases

1. Envision
2. Align
3. Launch
4. Scale

## AWS Account and Access Basics

### Root User

- The root user has full, unrestricted account access.
- Best practice: use root user only for tasks that specifically require it.
- Create IAM users/roles and enforce MFA for daily operations.

### AWS CLI

- **AWS Command Line Interface (CLI):** Tool to manage AWS services from the terminal.
- Useful for scripting, automation, and repeatable operational tasks.

---

## 2 - Compute Technology and Services

## Amazon EC2 Fundamentals

**Amazon EC2 (Elastic Compute Cloud)** provides virtual servers (instances) in AWS.

You can choose:

- Instance type (CPU, memory, storage, networking profile)
- Operating system (Linux/Windows, etc.)
- Networking/security settings
- Storage options (for example EBS)

## EC2 Pricing Models

### 1. On-Demand Instances

- Pay for compute capacity by usage (no long-term commitment).
- Best for short-term, unpredictable, or development/test workloads.
- Capacity Reservations can be used when you need guaranteed capacity in a specific AZ.

### 2. Spot Instances

- Use spare AWS capacity at steep discounts versus On-Demand.
- Best for fault-tolerant, interruptible workloads (batch, CI/CD, stateless processing).
- Instances can be interrupted with a short notice, so workloads must handle interruption.

### 3. Reserved Instances (RIs)

- 1-year or 3-year commitment for predictable usage.
- Can lower cost compared with On-Demand for steady-state workloads.
- Two common forms:
  - **Standard RI:** Highest discount, less flexibility.
  - **Convertible RI:** Lower discount, more flexibility to change attributes.

### 4. Savings Plans

- Commit to a consistent amount of compute usage (`$/hour`) for 1 or 3 years.
- Typically easier and more flexible than RIs.
- Applies across eligible services (for example EC2, Fargate, Lambda) depending on plan type.

### 5. Dedicated Hosts

- Physical servers dedicated to your account.
- Useful for licensing requirements (BYOL) and strict compliance/tenancy needs.

## Key EC2 Features

### Elastic Load Balancing (ELB)

Main load balancer types:

- Application Load Balancer (Layer 7, HTTP/HTTPS)
- Network Load Balancer (Layer 4, ultra-high performance)
- Gateway Load Balancer (for virtual network/security appliances)
- Classic Load Balancer (legacy)

### Auto Scaling

- EC2 Auto Scaling primarily performs **horizontal scaling** (add/remove instances).
- Helps maintain performance and availability while optimizing cost.
- Integrates with CloudWatch metrics and scaling policies.

### AWS Compute Optimizer

- Provides right-sizing recommendations using usage telemetry.
- Helps reduce cost and improve performance for supported compute resources.

## Ways to Connect to EC2

- AWS Management Console
- EC2 Instance Connect
- SSH (Linux)
- RDP (Windows)
- AWS Systems Manager Session Manager

## Containers on AWS

Containers package an application and its dependencies so it runs consistently across environments.

### Benefits

- Portability
- Operational consistency
- Efficient resource usage
- Faster application delivery
- Lower overhead than full virtual machines for many workloads

### Common Use Cases

- Lift-and-shift modernization steps
- Refactoring monoliths toward microservices
- CI/CD-based deployments
- Repetitive task execution and job workers

### Core AWS Container Services

- **Amazon ECR:** Managed container image registry.
- **Amazon ECS:** AWS-native container orchestration service.
- **Amazon EKS:** Managed Kubernetes service.

## Serverless Compute

Serverless lets you run code without managing underlying servers. You focus on application logic while AWS handles provisioning, scaling, and much of the operations overhead.

### AWS Lambda

- Event-driven serverless compute service.
- You deploy code as functions.
- Scales automatically based on invocation volume.
- Maximum execution time per invocation is 15 minutes.

Common uses:

- Real-time file/image processing
- Event-driven automation
- API backends and business logic

Lambda pricing is primarily based on:

- Number of requests
- Compute duration and configured resources

### AWS Fargate

- Serverless compute engine for containers with ECS/EKS.
- You define CPU and memory per task/pod; AWS manages infrastructure.
- Useful when you want container benefits without managing EC2 worker nodes.

Common uses:

- Event-driven container workloads
- Scheduled jobs
- Long-running containerized services

Fargate pricing is based on provisioned vCPU, memory, and storage usage duration.

## Additional Compute Services

### AWS Outposts

- Brings AWS infrastructure and services on premises.
- Supports low-latency, local data processing, and hybrid cloud architectures.
- Offered as Outposts racks and Outposts servers.

### Amazon Lightsail

- Simplified cloud platform for small projects and simple workloads.
- Predictable monthly pricing bundles (compute, storage, networking).
- Good for quick deployments like blogs, small web apps, and dev/test environments.

### AWS Batch

- Managed batch processing service for large-scale job execution.
- Dynamically provisions compute resources based on queued jobs.
- Good for data processing, simulations, and large asynchronous workloads.

### AWS Wavelength

- Deploy applications at the edge of 5G networks for ultra-low latency mobile experiences.
- Useful for latency-sensitive mobile and IoT applications.
