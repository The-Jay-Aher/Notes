# AWS Storage Extras

## Quick Summary
- Amazon EFS is a shared Linux file system that many EC2 instances can mount at the same time.
- Amazon FSx provides managed file systems for specific engines such as Windows File Server, Lustre, NetApp ONTAP, and OpenZFS.
- AWS Backup centralizes backup policies across services such as EBS, EFS, RDS, DynamoDB, FSx, Storage Gateway, and more.
- Choose storage by access style: object storage for files accessed by API, block storage for one server's disk, and file storage for shared folders.
- For the Solutions Architect exam, most storage questions are about choosing the right storage family, access pattern, availability model, and cost tier.

## The Storage Problem
Applications need storage, but not all storage behaves the same way.

Common questions:
- Is the data accessed as objects, disk blocks, or files?
- Does one server use it, or many servers at once?
- Does the application need Windows file shares, Linux file shares, or high-performance computing storage?
- Is the data hot, infrequent, archived, or only needed for backup?
- Does the solution need automatic multi-AZ availability?

AWS storage categories:

| Category | AWS examples | Think of it as | Best for |
|---|---|---|---|
| Object storage | S3, S3 Glacier classes | API-accessed objects in buckets | Backups, static assets, logs, data lakes |
| Block storage | EBS, instance store | A virtual hard disk | EC2 boot volumes, databases, low-latency disks |
| File storage | EFS, FSx | A shared file system | Shared folders, legacy apps, home directories |
| Backup service | AWS Backup | Central backup policy engine | Compliance, retention, cross-account backup |

## Amazon EFS
Amazon Elastic File System is a managed NFS file system for Linux workloads.

Think of EFS as a shared folder that many Linux EC2 instances can mount at the same time.

### What EFS Is Used For
Use EFS when:
- Multiple EC2 instances need the same files.
- You run Linux workloads that expect a POSIX file system.
- You need storage that grows and shrinks automatically.
- You want a managed service instead of maintaining your own NFS server.
- You need shared content for web servers, container workloads, or analytics jobs.

Examples:
- WordPress files shared by multiple EC2 web servers.
- Shared application uploads.
- Developer home directories.
- Container workloads needing shared persistent files.
- Lift-and-shift Linux apps that already use NFS.

### EFS Architecture
Important pieces:
- File system: the main EFS resource.
- Mount target: an ENI in a subnet that EC2 instances connect to.
- Security group: controls which clients can mount EFS.
- NFS client: Linux instances mount EFS using NFS.

Typical design:

```text
EC2 in AZ A -> EFS mount target in AZ A
EC2 in AZ B -> EFS mount target in AZ B
EC2 in AZ C -> EFS mount target in AZ C
```

Create mount targets in each Availability Zone where clients run. This keeps traffic local to the AZ and improves availability.

### EFS Storage Classes
EFS supports storage classes for different access patterns.

Common classes:

| Storage class | Use case |
|---|---|
| EFS Standard | Frequently accessed files across multiple AZs |
| EFS Standard-Infrequent Access | Less frequently accessed files with multi-AZ resilience |
| EFS One Zone | Frequently accessed files stored in one AZ |
| EFS One Zone-Infrequent Access | Lower-cost infrequent access in one AZ |
| EFS Archive | Rarely accessed files with lower storage cost and higher retrieval cost |

Use lifecycle policies to move files automatically into lower-cost classes based on access.

### EFS Performance Modes
EFS has performance choices.

Common concepts:
- Bursting throughput: throughput scales with stored data size and burst credits.
- Provisioned throughput: you pay for a fixed throughput level independent of file system size.
- Elastic throughput: EFS automatically scales throughput up and down for changing workloads.
- General Purpose performance mode: default for latency-sensitive workloads.
- Max I/O performance mode: older option for high aggregate throughput, with higher latency tradeoffs.

For most new beginner-level designs, start with General Purpose and elastic or bursting throughput unless the workload has a known throughput requirement.

### EFS Security
Security layers:
- Network access through security groups.
- NFS client permissions.
- IAM authorization for EFS API and optional client access controls.
- Encryption at rest using AWS KMS.
- Encryption in transit using TLS when mounted with the EFS mount helper.

Beginner mistake: creating EFS but forgetting the mount target security group. EC2 must be allowed to connect to EFS on NFS port 2049.

## Amazon FSx
Amazon FSx provides managed file systems using popular file system engines.

The key exam idea: choose FSx when the application needs a specific file system type, not just generic shared Linux NFS.

## FSx for Windows File Server
FSx for Windows File Server provides managed Windows file shares using SMB.

Use it when:
- Windows applications need shared file storage.
- Users need SMB file shares.
- You need integration with Microsoft Active Directory.
- You are migrating Windows file server workloads.
- You need features such as NTFS permissions, user quotas, shadow copies, and DFS namespaces.

Typical examples:
- Shared drives for Windows users.
- Windows application file shares.
- SQL Server workloads that require SMB file shares for certain patterns.
- Enterprise file shares integrated with Active Directory.

Key points:
- Uses SMB protocol.
- Integrates with AWS Managed Microsoft AD or self-managed AD.
- Supports Multi-AZ deployments for high availability.
- Supports backups.

## FSx for Lustre
FSx for Lustre is built for high-performance workloads.

Use it when:
- The workload needs very high throughput and low latency.
- Data comes from or goes back to S3.
- You run HPC, machine learning, media processing, or financial modeling.

Common pattern:

```text
S3 data lake -> FSx for Lustre high-performance processing -> results back to S3
```

Why not use EFS for this? EFS is a general shared file system. FSx for Lustre is specialized for high-performance parallel file access.

Key points:
- Can integrate with S3 repositories.
- Suitable for compute-heavy workloads.
- Not the default for normal web app shared files.

## FSx for NetApp ONTAP
FSx for NetApp ONTAP provides NetApp ONTAP features as a managed AWS service.

Use it when:
- An organization already uses NetApp and wants familiar capabilities in AWS.
- You need ONTAP features such as snapshots, clones, replication, and multi-protocol access.
- You need NFS, SMB, and iSCSI access patterns.

Exam idea:
- If the question mentions NetApp ONTAP, multi-protocol storage, or ONTAP data management features, FSx for NetApp ONTAP is usually the targeted answer.

## FSx for OpenZFS
FSx for OpenZFS provides a managed OpenZFS file system.

Use it when:
- You need OpenZFS features such as snapshots and cloning.
- You are migrating ZFS-based Linux workloads.
- You need low-latency file access with NFS.

Exam idea:
- If the question mentions ZFS semantics, OpenZFS, snapshots, and Linux NFS, FSx for OpenZFS is likely the fit.

## AWS Backup
AWS Backup is a centralized backup service.

Without AWS Backup, each service has its own backup settings. With AWS Backup, you can define backup plans and apply them across resources.

### What AWS Backup Helps With
AWS Backup helps answer:
- Which resources should be backed up?
- How often should backups run?
- How long should backups be retained?
- Should backups be copied to another Region or account?
- Who can delete or change backups?
- Are backups compliant with company policies?

### Core Concepts
| Concept | Meaning |
|---|---|
| Backup plan | Policy that defines frequency, retention, and lifecycle |
| Backup rule | Specific schedule and retention rule inside a plan |
| Backup vault | Container for recovery points |
| Recovery point | A backup copy |
| Resource assignment | Which resources the plan applies to |
| Backup Vault Lock | Helps enforce write-once-read-many style retention controls |

### Cross-Region and Cross-Account Backup
Important for disaster recovery:
- Cross-Region backup protects against regional failure.
- Cross-account backup protects against accidental or malicious deletion in the source account.
- Backup vault access policies control who can manage recovery points.

## Storage Decision Table
| Requirement | Good choice | Why |
|---|---|---|
| Static website assets | S3 | Object storage, cheap, integrates with CloudFront |
| EC2 boot disk | EBS | Block storage attached to EC2 |
| Temporary high-speed scratch disk | Instance store | Physically attached ephemeral storage |
| Shared Linux files across EC2 | EFS | Managed NFS, multi-client access |
| Windows SMB file share | FSx for Windows File Server | Native SMB and Active Directory integration |
| HPC file processing | FSx for Lustre | High-performance parallel file system |
| NetApp migration | FSx for NetApp ONTAP | Managed ONTAP features |
| ZFS workload migration | FSx for OpenZFS | Managed OpenZFS |
| Central backup policy | AWS Backup | Service-wide backup management |

## Beginner Mental Models
### EBS Is a Disk
EBS is like the disk attached to one server. Most EBS volumes attach to one EC2 instance at a time.

### EFS Is a Shared Linux Folder
EFS is like a shared network folder for Linux machines.

### FSx Is a Managed Specialized File Server
FSx is chosen when the application expects a specific file system type or enterprise file feature.

### S3 Is an Object Store
S3 is not a mounted disk in the normal architecture. Applications use APIs to put and get objects.

## Common Exam Clues
| Clue in question | Likely answer |
|---|---|
| "shared file system for Linux EC2 instances" | EFS |
| "NFS" | EFS or FSx for OpenZFS/ONTAP depending on details |
| "SMB" or "Windows file shares" | FSx for Windows File Server |
| "Active Directory file shares" | FSx for Windows File Server |
| "HPC" or "high throughput file processing" | FSx for Lustre |
| "S3 data needs high-speed processing" | FSx for Lustre |
| "NetApp" | FSx for NetApp ONTAP |
| "ZFS" | FSx for OpenZFS |
| "centralized backup policy" | AWS Backup |

## Common Mistakes
- Choosing EBS when many instances need to share the same files.
- Choosing EFS for a Windows SMB requirement.
- Choosing FSx for Lustre for normal shared web files.
- Forgetting EFS mount targets in each AZ.
- Forgetting security group rules for NFS port 2049.
- Treating backups as disaster recovery without testing restore.
- Keeping all backups in the same account and Region as the production workload.

## Troubleshooting Checklist
- Can the client resolve the EFS or FSx DNS name?
- Does the subnet route table allow the path to the mount target?
- Does the security group allow the correct protocol and port?
- Does the file system policy or IAM policy deny access?
- Is encryption in transit required by policy?
- Is the client using the correct mount helper or protocol?
- Are POSIX permissions or Windows ACLs blocking access?
- Are lifecycle policies moving files to a class with different retrieval cost or latency?

## Official References
- [Amazon EFS documentation](https://docs.aws.amazon.com/efs/)
- [Amazon FSx documentation](https://docs.aws.amazon.com/fsx/)
- [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)
- [Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html)
- [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)
- [Amazon FSx for OpenZFS](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/what-is-fsx.html)
- [AWS Backup documentation](https://docs.aws.amazon.com/aws-backup/)
