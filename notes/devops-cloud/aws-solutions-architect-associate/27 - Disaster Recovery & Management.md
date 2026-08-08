# Disaster Recovery and Management

## Quick Summary
- Disaster recovery is about restoring business service after failure.
- The two core metrics are RTO and RPO.
- AWS DR strategies include backup and restore, pilot light, warm standby, and multi-site active/active.
- Higher availability and lower recovery time usually cost more.
- A DR plan is not real until it is tested.

## Disaster Recovery Basics
Disaster recovery prepares for events such as:
- Accidental deletion.
- Application bug corrupting data.
- Hardware failure.
- Availability Zone failure.
- Regional outage.
- Security incident.
- Human operational mistake.

DR is not only technology. It also includes:
- Runbooks.
- Ownership.
- Communication.
- Testing.
- Compliance.
- Recovery priorities.

## RTO and RPO
### RTO: Recovery Time Objective
RTO means how long the service can be down.

Example:
- RTO = 1 hour means the business expects service restored within 1 hour.

### RPO: Recovery Point Objective
RPO means how much data loss is acceptable measured in time.

Example:
- RPO = 15 minutes means the business can lose at most 15 minutes of data.

Simple memory:

```text
RTO = time to recover
RPO = data you can lose
```

## DR Strategy 1: Backup and Restore
Simplest and usually cheapest.

Architecture:

```text
Primary Region -> backups copied to DR Region -> restore when needed
```

Use when:
- Longer downtime is acceptable.
- Cost must be low.
- Workload is not mission-critical.

Pros:
- Low cost.
- Simple to understand.

Cons:
- Recovery can be slow.
- Restore process must be tested.
- Infrastructure may need to be recreated.

AWS services:
- AWS Backup.
- EBS snapshots.
- RDS snapshots.
- DynamoDB PITR/backups.
- S3 versioning and replication.
- CloudFormation/Terraform for infrastructure recreation.

## DR Strategy 2: Pilot Light
Pilot light keeps the most critical core running in the DR Region.

Architecture:

```text
Primary Region: full application
DR Region: minimal core infrastructure and replicated data
```

During disaster:
- Scale up app servers.
- Restore or activate additional components.
- Redirect traffic.

Use when:
- You need faster recovery than backup/restore.
- You cannot afford a full duplicate environment.

Example:
- Database replica exists in DR Region.
- AMIs/templates are ready.
- App servers are not fully running until failover.

## DR Strategy 3: Warm Standby
Warm standby keeps a scaled-down but functional environment in the DR Region.

Architecture:

```text
Primary Region: full size
DR Region: smaller working copy
```

During disaster:
- Scale up DR environment.
- Redirect traffic.

Use when:
- RTO is relatively low.
- You can pay for a smaller always-on environment.

Pros:
- Faster than pilot light.
- Environment is already running.

Cons:
- More expensive than backup/restore and pilot light.
- Requires keeping environments synchronized.

## DR Strategy 4: Multi-Site Active/Active
Active/active runs production traffic in multiple Regions.

Architecture:

```text
Users -> Route 53/Global Accelerator -> Region A
                                  -> Region B
```

Use when:
- Very low RTO and RPO are required.
- Application is designed for multi-Region operation.
- Business can justify higher cost and complexity.

Pros:
- Fastest recovery.
- Can improve global latency.

Cons:
- Highest complexity.
- Data consistency is difficult.
- Costs more.
- Requires careful conflict handling.

## DR Strategy Comparison
| Strategy | Cost | RTO/RPO | Complexity |
|---|---|---|---|
| Backup and restore | Lowest | Highest RTO/RPO | Lower |
| Pilot light | Low-medium | Better than backup/restore | Medium |
| Warm standby | Medium-high | Lower RTO/RPO | Higher |
| Multi-site active/active | Highest | Lowest RTO/RPO | Highest |

## Multi-AZ vs Multi-Region
Multi-AZ protects against Availability Zone failure within a Region.

Multi-Region protects against larger regional problems.

Examples:
- RDS Multi-AZ helps when one AZ fails.
- Aurora Global Database helps with cross-Region database recovery/read locality.
- S3 Cross-Region Replication copies objects to another Region.

Do not call Multi-AZ a complete disaster recovery strategy for regional failure.

## Data Protection Services
Common options:
- AWS Backup for centralized backup.
- S3 Versioning for object recovery.
- S3 Replication for cross-Region/account object copies.
- EBS snapshots.
- RDS automated backups and snapshots.
- Aurora Global Database.
- DynamoDB global tables.
- EFS replication.
- FSx backups and replication features depending on file system type.

## Infrastructure as Code
DR needs repeatable infrastructure.

Use:
- CloudFormation.
- CDK.
- Terraform.

Benefits:
- Recreate environments consistently.
- Review changes.
- Store architecture as code.
- Reduce manual recovery errors.

## Route 53 and Traffic Failover
Route 53 can help route users during failure.

Useful routing policies:
- Failover routing.
- Latency-based routing.
- Weighted routing.
- Geolocation/geoproximity in some designs.

Health checks can detect endpoint failure and route away from unhealthy targets.

Global Accelerator can also route traffic across healthy regional endpoints using anycast IPs.

## Backup Design Principles
Good backup design includes:
- Defined backup frequency.
- Defined retention.
- Cross-Region copy when regional resilience is needed.
- Cross-account copy for stronger protection.
- Encryption.
- Access controls.
- Deletion protection or backup vault lock when required.
- Restore testing.

Backups you have never restored are only assumptions.

## Incident Management
DR also needs process.

Runbook should include:
- Who declares disaster.
- Who owns each recovery step.
- How to communicate status.
- How to access emergency credentials.
- How to restore data.
- How to validate service.
- How to fail back after primary Region recovers.

## Testing DR
Test types:
- Tabletop exercise.
- Backup restore test.
- Single component failover test.
- Regional failover simulation.
- Game day exercise.

Measure:
- Actual RTO.
- Actual RPO.
- Manual steps.
- Failed assumptions.
- Missing permissions.

## Common DR Architectures
### Low-Cost Backup Restore
```text
Region A production -> AWS Backup copy -> Region B vault
IaC templates stored in version control
```

### Warm Standby Web App
```text
Region A: ALB + app ASG + database writer
Region B: smaller ALB + app ASG + replicated database
Route 53 failover routing
```

### Active/Active Serverless
```text
Route 53 latency routing -> API in Region A
                         -> API in Region B
DynamoDB global tables for replicated data
```

## Common Mistakes
- Not defining RTO and RPO before choosing architecture.
- Building expensive active/active when the business does not need it.
- Keeping backups in the same account and Region only.
- Not testing restores.
- Forgetting DNS TTL and failover behavior.
- Ignoring application-level data consistency.
- Assuming infrastructure can be recreated manually during a crisis.
- Not documenting failback to the primary Region.

## Official References
- [AWS disaster recovery whitepaper](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
- [AWS Backup documentation](https://docs.aws.amazon.com/aws-backup/)
- [Amazon Route 53 documentation](https://docs.aws.amazon.com/route53/)
- [AWS Global Accelerator documentation](https://docs.aws.amazon.com/global-accelerator/)
- [Amazon S3 replication documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
- [Amazon Aurora Global Database documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)
- [DynamoDB global tables documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)
