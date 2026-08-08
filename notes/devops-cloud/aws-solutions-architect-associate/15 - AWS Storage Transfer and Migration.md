# AWS Storage Transfer and Migration

## Quick Summary
- AWS DataSync moves large amounts of data between on-premises storage, AWS storage services, and other cloud locations.
- AWS Transfer Family provides managed SFTP, FTPS, FTP, and AS2 access to S3 or EFS.
- AWS Snow Family moves very large datasets when network transfer is too slow, expensive, or unreliable.
- AWS Storage Gateway connects on-premises applications to AWS storage using file, volume, or tape interfaces.
- Storage migration design is mostly about data size, available bandwidth, downtime tolerance, protocol needs, and ongoing synchronization.

## The Storage Migration Problem
Moving data sounds simple until scale and business constraints appear.

Questions to ask:
- How much data must move?
- How fast is the network?
- Can the application be offline during migration?
- Does data need one-time migration or continuous sync?
- Which protocol does the existing application use?
- Is the data file-based, block-based, backup/tape-based, or object-based?
- Is the source on-premises, another AWS account, another Region, or another cloud?

## AWS DataSync
AWS DataSync is a managed data transfer service.

Use DataSync when you need to move data at scale between:
- On-premises NFS or SMB file shares and AWS.
- On-premises object storage and AWS.
- Amazon S3.
- Amazon EFS.
- Amazon FSx file systems.
- Some other cloud storage locations, depending on supported location types.

### DataSync Mental Model
DataSync is like a managed copy engine that understands enterprise storage, retries failures, validates data, and runs on schedules.

```text
Source storage -> DataSync task -> Destination storage
```

For on-premises sources, you usually deploy a DataSync agent.

```text
On-premises NFS/SMB -> DataSync agent -> AWS DataSync service -> S3/EFS/FSx
```

### DataSync Use Cases
- Migrate on-premises file shares to Amazon EFS or FSx.
- Move analytics data into S3.
- Replicate data to AWS for processing.
- Transfer data between AWS storage services.
- Periodically sync data for disaster recovery or hybrid workloads.

### DataSync vs Normal Copy Scripts
Normal scripts can work for small data. DataSync is better when you need:
- Parallel transfer.
- Scheduling.
- Verification.
- Logging.
- Bandwidth controls.
- Incremental transfers.
- Integration with AWS monitoring.

## AWS Transfer Family
AWS Transfer Family provides managed file transfer endpoints.

Supported protocols include:
- SFTP.
- FTPS.
- FTP.
- AS2.

The backend storage can be:
- Amazon S3.
- Amazon EFS.

### Transfer Family Mental Model
Transfer Family is not primarily a migration engine. It is a managed endpoint for partners, users, or applications that already speak file-transfer protocols.

```text
Partner SFTP client -> AWS Transfer Family endpoint -> S3 bucket
```

### Use Cases
- A vendor uploads files using SFTP, and your app processes them from S3.
- A legacy application only supports FTP-style delivery.
- A business partner uses AS2 for B2B document exchange.
- Users need managed SFTP access without running EC2 SFTP servers.

### Identity Options
Transfer Family can integrate with:
- Service-managed users.
- Custom identity providers.
- AWS Directory Service.
- Lambda-backed authentication flows.

### Security Notes
- Prefer SFTP or FTPS over plain FTP.
- Use IAM policies to restrict S3 or EFS access.
- Use VPC-hosted endpoints when the endpoint should not be public.
- Log transfers to CloudWatch.

## AWS Snow Family
AWS Snow Family is for physical data transfer and edge computing.

Services/devices:
- AWS Snowcone.
- AWS Snowball Edge.
- AWS Snowmobile for extremely large transfers.

### When Snow Family Makes Sense
Use Snow Family when:
- Data is too large for practical network transfer.
- Network bandwidth is limited.
- Transfer time over the network would exceed the business deadline.
- The environment is remote, disconnected, or bandwidth-constrained.
- You need rugged edge compute and storage.

### Simple Transfer Time Thinking
If you have 100 TB to migrate and a slow network, online migration may take weeks or months. A physical device can be faster.

Rough idea:

```text
Transfer time = data size / effective bandwidth
```

Remember that effective bandwidth is lower than theoretical bandwidth because of overhead, congestion, and throttling.

### Snowball Edge
Snowball Edge can provide:
- Storage.
- Local compute.
- Secure physical transport.
- Data import to S3.
- Data export from S3 in supported workflows.

### Security
Snow devices use:
- Encryption.
- Tamper-resistant design.
- AWS-managed chain-of-custody processes.
- Job tracking through AWS.

## AWS Storage Gateway
AWS Storage Gateway connects on-premises applications to AWS storage.

It is useful when applications cannot be moved immediately but you still want AWS-backed storage.

### Gateway Types
| Gateway type | Main idea | Use case |
|---|---|---|
| File Gateway | Presents file shares backed by S3 | On-prem apps write files, AWS stores objects |
| Volume Gateway | Presents block storage volumes backed by AWS | Hybrid block storage and snapshots |
| Tape Gateway | Presents virtual tapes backed by AWS | Replace physical tape backup libraries |

### File Gateway
File Gateway provides NFS or SMB access while storing data as objects in S3.

Use it for:
- Hybrid file workflows.
- On-prem applications that write to file shares.
- Moving backup files to S3.
- Gradual migration from on-prem file systems to object storage.

### Volume Gateway
Volume Gateway provides iSCSI block storage.

Modes:
- Cached volumes: primary data is in S3, frequently accessed data cached locally.
- Stored volumes: primary data remains local, with asynchronous backup to AWS.

### Tape Gateway
Tape Gateway replaces physical tape infrastructure with virtual tapes.

Use it when:
- Existing backup software expects a tape library.
- You want to store virtual tapes in S3 and archive them in lower-cost classes.

## AWS Backup for Migration and Protection
AWS Backup is not a transfer service, but it is part of a complete storage plan.

Use AWS Backup to:
- Protect migrated workloads.
- Apply retention rules.
- Copy recovery points across Regions/accounts.
- Centralize compliance reporting.

Migration without backup is incomplete. After data is moved, verify that restore works.

## Choosing the Right Service
| Requirement | Best fit |
|---|---|
| Move NFS/SMB data into EFS, FSx, or S3 | DataSync |
| Recurring scheduled sync | DataSync |
| Partners upload files by SFTP | Transfer Family |
| Existing app requires FTP/FTPS/SFTP endpoint | Transfer Family |
| Huge dataset cannot move over network in time | Snow Family |
| Remote/edge site with limited network | Snowball Edge or Snowcone |
| On-prem apps need a local file share backed by S3 | File Gateway |
| Backup software expects virtual tape | Tape Gateway |
| On-prem servers need iSCSI volumes backed by AWS | Volume Gateway |

## Migration Planning Checklist
1. Inventory data size, file count, and change rate.
2. Identify source and destination storage types.
3. Measure real available bandwidth.
4. Decide whether migration is one-time or continuous.
5. Define cutover window and rollback plan.
6. Choose the transfer service.
7. Test with a small representative dataset.
8. Validate permissions, ownership, metadata, and checksums where needed.
9. Monitor transfer progress and failures.
10. Run post-migration verification.
11. Enable backup and lifecycle policies.

## Common Mistakes
- Using Transfer Family when the real need is bulk migration.
- Using DataSync when the requirement is continuous external SFTP access.
- Underestimating the impact of millions of tiny files on transfer speed.
- Forgetting DNS, firewall, and allowlist changes for migration tools.
- Migrating data but not permissions or metadata required by the application.
- Skipping a test restore after backup setup.
- Assuming network bandwidth equals usable migration throughput.

## Beginner Example
Requirement:
- A company has 40 TB on an on-premises NFS file server.
- It wants to move the data to Amazon EFS.
- The file server changes daily.
- Downtime must be small.

Good design:
- Deploy a DataSync agent near the source file server.
- Create a DataSync task from NFS to EFS.
- Run initial sync while the application stays online.
- Run incremental syncs until cutover.
- Stop writes during final cutover.
- Run final sync.
- Point applications to EFS.
- Enable AWS Backup for EFS.

Why not Snowball?
- Snowball can move huge data, but it does not solve ongoing daily changes as cleanly as DataSync for this specific case.

## Official References
- [AWS DataSync documentation](https://docs.aws.amazon.com/datasync/)
- [AWS Transfer Family documentation](https://docs.aws.amazon.com/transfer/)
- [AWS Snow Family documentation](https://docs.aws.amazon.com/snowball/)
- [AWS Storage Gateway documentation](https://docs.aws.amazon.com/storagegateway/)
- [AWS Backup documentation](https://docs.aws.amazon.com/aws-backup/)
