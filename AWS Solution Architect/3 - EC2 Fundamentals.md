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

### Quick Summary

- **On-Demand:** No commitment; best for short, variable, or unpredictable workloads.
- **Reserved Instances (RI's):** 1-year or 3-year commitment for steady workloads.
  - `Standard RI`: Highest discount, less flexibility.
  - `Convertible RI`: More flexibility, lower discount.
- **Savings Plans:** Commit to a consistent amount of usage (`$/hour`) for 1 or 3 years.
- **Spot Instances:** Use spare AWS capacity at major discounts; can be interrupted.
- **Dedicated Hosts:** Physical host dedicated to your account.
- **Dedicated Instances:** Hardware dedicated to one customer account.
- **Capacity Reservations:** Reserve capacity in a specific AZ without a long-term commitment.

### Detailed Notes

#### On-Demand

- Pay for what you use.
- Linux/Windows billing is per second (after the first minute).
- Other operating systems may be billed per hour.
- Highest cost model, but no upfront payment and no long-term commitment.
- Best for short-term and uninterrupted workloads with unpredictable behaviour.

#### Reserved Instances (RI's)

- Up to 72% discount compared to On-Demand (depending on term/payment class).
- Commit to specific attributes (instance type, region, tenancy, OS).
- Terms: 1 year (`+` discount) or 3 years (`+++` discount).
- Payment options: No upfront (`+`), partial upfront (`++`), all upfront (`+++`).
- Scope: Regional or Zonal (Zonal also reserves capacity in an AZ).
- Good fit for steady-state workloads (for example, databases).
- You can buy/sell eligible RI's in the RI Marketplace.

`Convertible RI` lets you change instance family/type, region, scope, tenancy, and OS with more flexibility than `Standard RI`.

#### Savings Plans

- Up to 72% discount potential (similar to RI range).
- Commit to a usage spend rate (for example, `$10/hour`) for 1 or 3 years.
- Usage above commitment is billed at On-Demand rates.
- Often more flexible than RIs in practice.
- Common flexibility dimensions:
  - Instance size
  - OS
  - Tenancy (host, dedicated, default)

#### Spot Instances

- Can be up to 90% cheaper than On-Demand.
- Instances can be interrupted when capacity is reclaimed or price constraints are hit.
- Most cost-efficient option for fault-tolerant designs.
- Good for:
  - Batch jobs
  - Data analysis
  - Image processing
  - Distributed workloads
  - Workloads with flexible start/end windows

#### Dedicated Hosts

- A physical server dedicated to your use.
- Supports compliance needs and server-bound licenses (per-socket, per-core, per-VM).
- Purchase options:
  - On-Demand (pay per second for active host)
  - Reserved (1 or 3 years: no upfront, partial upfront, all upfront)
- Typically the most expensive option.
- Useful for BYOL scenarios and strict regulatory requirements.

#### Dedicated Instances

- Instances run on hardware dedicated to your account.
- May share hardware with other instances in the same account.
- You do not control host placement across start/stop cycles.

#### Capacity Reservations

- Reserve On-Demand capacity in a specific AZ for any duration.
- Ensures capacity is available when needed.
- No time commitment (create/cancel anytime) and no built-in billing discount.
- You are billed at On-Demand rates whether instances run or not.
- Can be combined with Regional RIs/Savings Plans for billing benefits.
- Best for short-term, uninterrupted workloads that must run in a specific AZ.

### Spot Instance Requests and Spot Blocks

- Can be up to 90% cheaper than On-Demand.
- Define a maximum Spot price and run instances while the current Spot price is below that maximum.
- The hourly Spot price varies based on supply and demand.
- If Spot price rises above your max price, instances can be stopped or terminated with a 2-minute warning.

Other strategy noted in course material: **Spot Blocks**

- Request Spot capacity for a specific time window (for example, 1 to 6 hours) with fewer interruptions.
- In rare cases, the instance can still be reclaimed.

Good fits:

- Batch jobs
- Data analysis
- Workloads resilient to failure

Not ideal for:

- Critical jobs
- Stateful databases

![Spot Instance Termination](Images/spot-instance-termination.png)

### Spot Fleets

- Spot Fleet = a set of Spot Instances plus optional On-Demand instances.
- The fleet attempts to meet target capacity while respecting price constraints.

Typical configuration includes:

- Launch pools (instance types, operating systems, Availability Zones)
- Multiple pool definitions for better placement flexibility
- Stopping launches when target capacity or max cost is reached

Allocation strategies:

- `lowestPrice`: Picks the lowest-priced pool (cost-focused, short workloads).
- `diversified`: Distributes across pools (availability-focused, longer workloads).
- `capacityOptimized`: Chooses pools with the best available capacity.
- `priceCapacityOptimized` (recommended): Prioritizes capacity, then picks lower-priced pools.

Spot Fleets help automate Spot requests across pools to improve both cost and availability.

### Which Purchasing Option Is Right?

- **On-Demand:** Like checking into a resort whenever you want and paying full price.
- **Reserved:** Like booking ahead for a long stay to get a discount.
- **Savings Plans:** Like committing to spend a certain amount per hour and using different room types.
- **Spot:** Like bidding on empty rooms and potentially being asked to leave anytime.
- **Dedicated Hosts:** Like booking an entire building.
- **Capacity Reservations:** Like reserving a room at full price even if you do not stay in it.

## Storage Options with EC2

### EBS (Elastic Block Store)

- Persistent block storage for one instance at a time (based on volume attachment rules).
- Data persists beyond instance stop/start.
- Snapshot support for backup and restore workflows.

### Instance Store

- High-performance local disk physically attached to the host.
- Data is temporary and can be lost when an instance stops/terminates or the host fails.

### EFS (Elastic File System)

- Managed, shared file system for Linux instances.
- Multiple instances can access it concurrently.

## Networking and Security

### Security Groups

- Virtual firewall at the instance ENI level.
- Stateful.
- Only allow rules (inbound/outbound); no explicit deny rules.
- Rules can reference CIDR ranges or other security groups.

#### Deeper Dive

- Security groups act as a firewall for EC2 instances.
- They regulate:
  - Access to ports
  - Authorized IP ranges (IPv4 and IPv6)
  - Inbound traffic
  - Outbound traffic

#### Good to Know

- A security group can be attached to multiple instances.
- Security groups are scoped to a specific Region + VPC.
- Keep a dedicated security group for SSH access where appropriate.
- If an instance is not reachable, it is often a security/network path issue.
- If you see `connection refused`, the network path is usually open but the application is not accepting connections.

#### Common Ports to Know

- `22` - SSH
- `21` - FTP (File Transfer Protocol)
- `22` - SFTP (Secure File Transfer Protocol over SSH)
- `80` - HTTP
- `443` - HTTPS
- `3389` - RDP (remote login to Windows instances)