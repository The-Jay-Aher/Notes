# EC2 Instance Storage

## EBS Overview

### What Is an EBS Volume?

- An EBS volume is a network drive you can attach to an EC2 instance while it runs.
- It allows your instance to persist data, even after termination (depending on settings).
- At the CCP level, EBS volumes can be mounted to one instance at a time.
- EBS volumes are bound to a specific Availability Zone (AZ).
- Analogy: think of EBS as a "network USB stick."

### EBS Volume

- It is a network drive (not a physical drive).
  - It uses the network to communicate with the instance, so there may be some latency.
  - It can be detached from one EC2 instance and attached to another quickly.
- It is locked to an Availability Zone (AZ).
  - An EBS volume in `us-east-1a` cannot be attached to `us-east-1b`.
  - To move a volume across AZs, first create a snapshot.
- It has provisioned capacity (size in GB and IOPS).
  - You are billed for all provisioned capacity.
  - You can increase the size of the drive over time.

![EBS Volume Example](<Images/EBS Volume.png>)

### EBS Delete on Termination Attribute

- Controls EBS behavior when an EC2 instance is terminated.
  - By default, the root EBS volume is deleted (attribute enabled).
  - By default, non-root attached EBS volumes are not deleted (attribute disabled).
- This behavior can be controlled from the AWS Console or AWS CLI.

Use case:
- Preserve root volumes when an instance is terminated.

## EBS Snapshot

### EBS Snapshot

- A snapshot is a backup of your EBS volume at a point in time.
- It is not necessary to detach a volume to take a snapshot (though it may be recommended).
- Snapshots can be copied across AZs or regions.

### EBS Snapshot Features

- EBS Snapshot Archive:
  - Move snapshots to an archive tier that is up to 75% cheaper.
  - Restoring an archived snapshot can take 24 to 72 hours.
- Recycle Bin for EBS Snapshots:
  - Configure rules to retain deleted snapshots for recovery after accidental deletion.
  - Retention can be set from 1 day to 1 year.
- Fast Snapshot Restore (FSR):
  - Forces full initialization of snapshots to remove first-use latency (higher cost).

## AMI Overview

### AMI Overview

- AMI = Amazon Machine Image.
- AMIs are customized templates of EC2 instances.
  - You can include software, configuration, operating system, monitoring, etc.
  - They provide faster boot and configuration time because software is pre-packaged.
- AMIs are built for a specific region (and can be copied to other regions).
- You can launch EC2 instances from:
  - Public AMIs (AWS-provided).
  - Your own AMIs.
  - AWS Marketplace AMIs.

### AMI Process (From an EC2 Instance)

1. Start an EC2 instance and customize it.
2. Stop the instance (for data integrity).
3. Build an AMI (this also creates an EBS snapshot).
4. Launch new instances from the AMI.

## EC2 Instance Store

### EC2 Instance Store

- EBS volumes are network drives with good but limited performance.
- If you need very high-performance disk, use EC2 Instance Store.
- EC2 Instance Store provides better I/O performance.
- EC2 Instance Store is ephemeral (data is lost when the instance is stopped/terminated).
- Good for buffer, cache, scratch data, and temporary content.
- Risk of data loss exists if hardware fails.
- Backups and replication are your responsibility.

## EBS Volume Types

### EBS Volume Types

EBS volumes come in 6 types:
- `gp2` / `gp3` (SSD): General-purpose SSD volumes balancing price and performance for many workloads.
- `io1` / `io2 Block Express` (SSD): Highest-performance SSD volumes for mission-critical, low-latency, or high-throughput workloads.
- `st1` (HDD): Low-cost HDD volumes for frequently accessed, throughput-intensive workloads.
- `sc1` (HDD): Lowest-cost HDD volumes for less frequently accessed workloads.

### EBS Volume Type Use Cases

**General Purpose SSD**

- Cost-effective, low-latency storage.
- Common for system boot volumes, virtual desktops, and dev/test environments.
- Size range: 1 GB to 16 TB.
- `gp3`:
  - Baseline: 3,000 IOPS and 125 MB/s throughput.
  - Can increase up to 16,000 IOPS and 1,000 MB/s throughput independently.
- `gp2`:
  - Small volumes can burst up to 3,000 IOPS.
  - Size and IOPS are linked.
  - Max IOPS is 16,000.
  - Baseline is 3 IOPS/GB (around 5,334 GB to reach 16,000 IOPS).

**Provisioned IOPS (PIOPS) SSD**

- Designed for critical business applications with sustained high IOPS.
- Suitable for workloads requiring more than 16,000 IOPS.
- Great for database workloads sensitive to storage performance and consistency.
- `io1`:
  - Size: 4 GB to 16 TB.
  - Max PIOPS: 64,000 (Nitro instances), 32,000 (non-Nitro).
  - PIOPS can be updated independently from storage size.
- `io2 Block Express`:
  - Size: 4 GB to 64 TB.
  - Sub-millisecond latency.
  - Up to 256,000 IOPS with an IOPS/GB ratio up to 1,000:1.
  - Supports EBS Multi-Attach.

## EBS Multi-Attach

### EBS Multi-Attach (io1/io2 Family)

- Attach the same EBS volume to multiple EC2 instances in the same AZ.
- Each instance has full read/write permissions to the high-performance volume.

Use case:
- Achieve higher application availability in clustered Linux applications (for example, Teradata).
- Applications must manage concurrent write operations.

- Supports up to 16 EC2 instances at the same time.
- Requires a cluster-aware file system.

## EBS Encryption

### EBS Encryption

When you create an encrypted EBS volume:
- Data at rest is encrypted inside the volume.
- Data in flight between the instance and volume is encrypted.
- Snapshots are encrypted.
- Volumes created from encrypted snapshots are also encrypted.

- Encryption and decryption are handled transparently.
- Encryption has minimal impact on latency/performance.
- EBS encryption uses KMS keys (`AES-256`).
- Copying an unencrypted snapshot can be used to encrypt it.
- Snapshots of encrypted volumes remain encrypted.

### Encrypt an Unencrypted EBS Volume

1. Create a snapshot of the unencrypted EBS volume.
2. Copy the snapshot and enable encryption on the copy.
3. Create a new EBS volume from the encrypted snapshot.
4. Attach the encrypted volume to the original instance.

## Amazon EFS

### Amazon EFS (Elastic File System)

- Managed NFS file system that can be mounted by many EC2 instances.
- Works across multiple AZs.
- Highly available, scalable, and pay-per-use (typically more expensive than EBS).

Use cases:
- Content management
- Web serving
- Data sharing
- WordPress

- Uses NFSv4.1 protocol.
- Uses security groups to control access.
- Compatible with Linux-based AMIs (not Windows).
- Supports encryption at rest with KMS.
- POSIX-compliant file system with a standard file API.
- Scales automatically (no capacity planning).

### EFS Performance and Throughput

EFS scale:
- Thousands of concurrent NFS clients.
- 10 GB+/s throughput.
- Automatically grows to petabyte scale.

Performance mode (set at EFS creation time):
- General Purpose (default): latency-sensitive workloads (for example, web servers, CMS).
- Max I/O: higher latency, higher throughput, highly parallel workloads (for example, big data, media processing).

Throughput mode:
- Bursting: 1 TB = 50 MB/s baseline, with bursting.
- Provisioned: set throughput regardless of storage size (for example, 1 GB/s on 1 TB).
- Elastic: scales throughput up/down automatically based on workload.
  - Up to 3 GB/s reads and 1 GB/s writes.
  - Useful for unpredictable workloads.

### EFS Storage Classes

Storage tiers (lifecycle management can move files after N days):
- Standard: frequently accessed files.
- Infrequent Access (`EFS-IA`): lower storage cost, retrieval cost applies.
- Archive: rarely accessed data, lower storage cost.
- Lifecycle policies can move files between tiers automatically.

Availability and durability:
- Standard: multi-AZ, good for production.
- One Zone: single AZ, good for dev/backup, compatible with `EFS One Zone-IA`.

Potential savings can exceed 80% when using lower-cost storage classes.

## EFS vs EBS

### EBS (Elastic Block Storage)

EBS volumes:
- Attach to one instance (except Multi-Attach on `io1`/`io2`).
- Are locked to a single AZ.
- `gp2`: IOPS increases as disk size increases.
- `gp3` and `io1`: IOPS can be increased independently.

To migrate an EBS volume across AZs:
1. Take a snapshot.
2. Restore the snapshot in another AZ.
3. Attach the restored volume.

Note:
- EBS backups use I/O, so avoid heavy backup operations during peak traffic.
- Root EBS volumes are deleted by default when the instance is terminated (configurable).

### EFS (Elastic File System)

- Can mount across hundreds of instances in multiple AZs.
- Useful for shared website files (for example, WordPress).
- Linux-only (POSIX).
- Typically costs more than EBS.
- Can reduce cost using storage tiers and lifecycle policies.

Remember: compare EFS vs EBS vs Instance Store based on durability, performance, and sharing needs.
