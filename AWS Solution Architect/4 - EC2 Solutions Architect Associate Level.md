# 4 - EC2 Solutions Architect Associate Level

## Private IP vs Public IP vs Elastic IP

EC2 networking commonly uses IPv4 and IPv6:

- `IPv4` example: `1.160.10.240`
- `IPv6` example: `2001:db8:1234:1a00:abcd:ef12:3456:7890`

Key points:

- IPv4 is still widely used, but public IPv4 space is limited.
- IPv6 provides a much larger address space and supports modern large-scale networking.
- IPv4 format: `[0-255].[0-255].[0-255].[0-255]` (32-bit, about 4.3 billion total addresses).

### Private and Public IP behavior on EC2

- **Private IP** (from your VPC subnet) stays with the instance/ENI.
- **Auto-assigned public IP** can change after stop/start.
- If you need a fixed public IPv4 address, use an **Elastic IP (EIP)**.

### Elastic IP (EIP)

- Static public IPv4 address allocated to your AWS account.
- Can be remapped quickly to another instance/ENI for failover.
- Can be attached to one resource at a time.
- Default account quota is typically `5` EIPs per Region (quota increase possible).

Design guidance:

- Prefer DNS (`Route 53`) + load balancers over direct EIP usage.
- Use EIP when you specifically need a stable public IPv4 endpoint.

## EC2 Placement Groups

Placement groups let you influence how instances are physically placed on AWS hardware.

Placement strategies:

- **Cluster:** Pack instances close together in one AZ for very low latency/high throughput.
- **Spread:** Place instances on distinct hardware to reduce correlated failure risk.
- **Partition:** Group instances into isolated partitions (separate racks) for large distributed systems.

### Cluster placement group

Pros:

- Very high network performance between instances.

Cons:

- Single AZ scope; AZ failure can impact all grouped instances.

Use cases:

- HPC workloads
- tightly coupled low-latency applications

### Spread placement group

Pros:

- Strong instance-level fault isolation.
- Can span multiple AZs in a Region.

Cons:

- Limited scale (up to 7 running instances per AZ per spread placement group).

Use cases:

- Critical applications where each node should be isolated.

### Partition placement group

Pros:

- Scales to large fleets.
- Failure impact is typically limited to a partition.
- Partition awareness is available to the instance via metadata.

Cons:

- More planning needed for partition-aware applications.

Use cases:

- HDFS
- HBase
- Cassandra
- Kafka

## Elastic Network Interfaces (ENI) Overview

An ENI is a virtual network card in a VPC.

An ENI includes:

- One primary private IPv4 and optional secondary private IPv4 addresses
- Optional public IPv4 / Elastic IP association
- One or more security groups
- A MAC address

Important behavior:

- ENIs are AZ-scoped.
- You can create and attach/detach ENIs independently.
- Useful for failover patterns (move ENI to standby instance).

Reference: [ENI announcement](https://aws.amazon.com/blogs/aws/new-elastic-network-interfaces-in-the-virtual-private-cloud/)

## EC2 Hibernate

State options:

- **Stop:** OS shuts down, EBS data persists, RAM is lost.
- **Terminate:** Instance is deleted; root volume is deleted if `DeleteOnTermination=true`.
- **Hibernate:** Instance state (RAM) is saved to encrypted root EBS, then instance stops.

Why hibernate:

- Faster return to service for memory-heavy apps.
- Keeps in-memory state for long startup workloads.

### Hibernate requirements and limits

- Supported only on hibernation-capable instance types and AMIs.
- Root volume must be EBS and encrypted.
- Not supported for bare metal instances.
- RAM size limit is up to 150 GB.
- Available with On-Demand, Reserved, and Spot (if the instance type supports hibernation).
- Recommended maximum hibernation duration: 60 days.
