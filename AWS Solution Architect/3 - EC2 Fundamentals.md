# 3 - EC2 Fundamentals

## Amazon EC2 Overview

Amazon EC2 (**Elastic Compute Cloud**) is a core AWS compute service that provides resizable virtual servers called **instances**.

EC2 is part of the Infrastructure as a Service (IaaS) model. You manage the OS and applications while AWS manages the physical infrastructure.

EC2-related building blocks you commonly use together:

- **EC2 Instances:** Virtual machines for running workloads.
- **EBS (Elastic Block Store):** Persistent block storage for instances.
- **EFS (Elastic File System):** Shared file storage for Linux workloads.
- **ELB (Elastic Load Balancing):** Distributes traffic across instances.
- **Auto Scaling:** Automatically adds/removes instances based on demand.

## Why EC2 Matters

EC2 gives you strong control over compute environments:

- Choose OS, instance size, and networking model.
- Scale quickly without buying physical servers.
- Combine with managed AWS services as architecture evolves.

## EC2 Sizing and Configuration Options

When launching an EC2 instance, common decisions include:

1. **Amazon Machine Image (AMI):** Base image (OS + optional software).
2. **Instance type:** vCPU, memory, networking, and hardware profile.
3. **Storage:**
   - **EBS volumes** (persistent)
   - **Instance store** (ephemeral, tied to host)
4. **Network settings:** VPC, subnet, private/public IP, ENI behavior.
5. **Firewall rules:** Security groups (stateful, allow rules only).
6. **Bootstrap automation:** EC2 User Data script for first boot tasks.
7. **IAM role:** Temporary credentials for AWS API access from instance.
8. **Monitoring:** CloudWatch metrics and optional detailed monitoring.

## EC2 Instance Types Basics

Reference: [AWS EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)

### Common EC2 Family Categories

1. **General Purpose** (balanced CPU/memory/network)
2. **Compute Optimized** (high-performance processors)
3. **Memory Optimized** (large in-memory datasets)
4. **Accelerated Computing** (GPU/FPGA/inference acceleration)
5. **Storage Optimized** (high, low-latency local storage)

### Instance Naming Convention Example

`m5.2xlarge`

- `m`: Family (general purpose)
- `5`: Generation
- `2xlarge`: Size in that family

Newer generations usually improve price/performance and efficiency.

## EC2 Purchasing Options

### On-Demand

- No commitment.
- Good for short-term, variable, or unpredictable workloads.

### Reserved Instances (RIs)

- 1-year or 3-year commitment for steady workloads.
- `Standard RI`: highest discount, less flexibility.
- `Convertible RI`: more flexibility, lower discount.

### Savings Plans

- Commit to a consistent amount of usage (`$/hour`) for 1 or 3 years.
- More flexible than many RI scenarios.

### Spot Instances

- Use spare AWS capacity at major discounts.
- Best for interruptible, fault-tolerant workloads.

### Dedicated Hosts

- Physical host dedicated to your account.
- Useful for BYOL licensing/compliance requirements.

## Storage Options with EC2

### EBS (Elastic Block Store)

- Persistent block storage for one instance at a time (per volume attachment rules).
- Data persists beyond instance stop/start.
- Snapshot support for backup and restore workflows.

### Instance Store

- High-performance local disk physically attached to host.
- Data is temporary and can be lost when instance stops/terminates or host fails.

### EFS (Elastic File System)

- Managed, shared file system for Linux instances.
- Multiple instances can access concurrently.

## Networking and Security

### Security Groups

- Virtual firewall at instance ENI level.
- Stateful.
- Only allow rules (inbound/outbound), no explicit deny rules.

### Network ACLs (NACLs)

- Subnet-level stateless filtering.
- Supports allow and deny rules.

### Elastic IP

- Static public IPv4 address that you can re-map between instances.
- Useful when public endpoint must remain consistent.

## Load Balancing and Auto Scaling

### Elastic Load Balancing (ELB)

Main types:

- **Application Load Balancer (ALB):** Layer 7, HTTP/HTTPS routing features.
- **Network Load Balancer (NLB):** Layer 4, very high throughput/low latency.
- **Gateway Load Balancer (GWLB):** For network/security virtual appliances.
- **Classic Load Balancer (CLB):** Legacy option.

### EC2 Auto Scaling

- Primarily horizontal scaling (add/remove instances).
- Maintains desired capacity and improves availability.
- Integrates with CloudWatch alarms and scaling policies.

## Accessing EC2 Instances

- AWS Management Console
- EC2 Instance Connect
- SSH for Linux
- RDP for Windows
- AWS Systems Manager Session Manager (agent + IAM-based access model)

## High Availability and Resilience Best Practices

- Run instances across multiple Availability Zones.
- Place instances behind a load balancer.
- Use Auto Scaling groups for self-healing and demand-based scaling.
- Use EBS snapshots/AMIs for backup and disaster recovery strategy.
- Enforce least privilege with IAM roles and security groups.

## Operational Tips

- Start with right-sized instances; optimize later with CloudWatch + Compute Optimizer.
- Prefer newer generation instances when possible.
- Use Spot for batch/stateless jobs to lower cost.
- Stop non-production instances when not needed.
- Tag resources (`Environment`, `Owner`, `Application`, `CostCenter`) for governance and cost tracking.
