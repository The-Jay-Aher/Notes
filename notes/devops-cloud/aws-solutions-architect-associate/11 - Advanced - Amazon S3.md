# 11 - Advanced - Amazon S3

## Quick Summary

Advanced S3 topics focus on performance, replication, multipart uploads, transfer acceleration, object locking, select/query features, inventory, batch operations, and cost controls. These features matter when S3 is used at large scale or for compliance-heavy workloads.

## Multipart Upload

Multipart upload splits a large object into parts, uploads parts independently, then completes the object.

Use for:

- Large files.
- More reliable uploads.
- Parallel upload performance.

Important:

- Incomplete multipart uploads can cost money.
- Lifecycle rules can abort incomplete multipart uploads.

## S3 Transfer Acceleration

Transfer Acceleration uses AWS edge locations to speed long-distance uploads/downloads to S3.

Use when:

- Users upload from far away.
- Cross-continent upload latency is high.
- Testing shows improvement justifies cost.

Do not assume it is always faster; test for your geography.

## S3 Replication

Types:

- Same-Region Replication (SRR).
- Cross-Region Replication (CRR).

Use cases:

- Compliance.
- Disaster recovery.
- Low-latency access in another Region.
- Account-level data copy.
- Log aggregation.

Requirements/notes:

- Versioning must be enabled.
- IAM role is required for replication.
- Existing objects may need batch replication.
- Deletes and delete markers need careful configuration.

## S3 Object Lock

Object Lock helps prevent object deletion or overwrite for a retention period.

Modes:

| Mode | Meaning |
| --- | --- |
| Governance | Users with special permissions can bypass retention. |
| Compliance | Retention cannot be bypassed by normal users, including root, until expiry. |

Use for:

- WORM requirements.
- Compliance retention.
- Ransomware protection patterns.

Be careful: compliance mode is intentionally hard to bypass.

## S3 Glacier Vault Lock vs S3 Object Lock

For modern S3 object-level retention, know S3 Object Lock. Glacier Vault Lock applies policies to Glacier vaults in older/archive-specific patterns.

Exam questions may test immutability and retention concepts.

## S3 Select

S3 Select retrieves only part of an object using SQL-like expressions.

Use when:

- Large CSV/JSON/Parquet object.
- You need only selected rows/columns.
- You want to reduce data transferred.

It is not a full database replacement.

## S3 Inventory

S3 Inventory produces reports about bucket objects and metadata.

Use for:

- Auditing.
- Compliance.
- Replication checks.
- Lifecycle analysis.
- Large bucket reporting.

## S3 Batch Operations

Batch Operations applies actions to many objects.

Examples:

- Copy objects.
- Invoke Lambda for each object.
- Restore Glacier objects.
- Replace tags.
- Apply Object Lock retention.

Useful when a bucket has millions/billions of objects.

## Performance Design

S3 automatically scales request performance, but design still matters.

Good practices:

- Use multipart upload for large objects.
- Use CloudFront for repeated public/global reads.
- Use S3 byte-range fetches where useful.
- Monitor 4xx/5xx errors and latency.
- Use retries with exponential backoff in applications.

## Cost Controls

Watch:

- Storage class.
- Request count.
- Data transfer.
- Replication.
- Lifecycle transitions.
- Retrieval charges.
- Old versions.
- Incomplete multipart uploads.

## Benefits

- Advanced lifecycle and compliance controls.
- Cross-Region replication for DR/compliance.
- Large-scale object operations.
- Performance options for large objects/global users.

## Drawbacks / Limitations

- Advanced features can increase cost.
- Replication is asynchronous.
- Object Lock compliance mode is strict.
- S3 Select supports limited query patterns.
- Archive retrieval classes can delay access.

## Hidden Details / Caveats

- Replication does not automatically apply retroactively unless configured with batch replication.
- Replication needs versioning.
- Lifecycle rules can delete data permanently.
- Object Lock requires correct bucket/object setup.
- Incomplete multipart uploads remain until aborted.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Replication without versioning | Enable versioning first. |
| No cleanup for multipart uploads | Add lifecycle abort rule. |
| Compliance Object Lock by accident | Test governance mode and understand retention. |
| Using Transfer Acceleration without testing | Benchmark from user locations. |
| Ignoring old versions cost | Add lifecycle for noncurrent versions. |

## Interview Notes

- Multipart upload improves large object upload reliability/performance.
- CRR copies objects to another Region asynchronously.
- S3 Object Lock supports WORM retention.
- S3 Inventory reports object metadata at scale.
- Batch Operations performs actions on many objects.
- S3 Select queries part of an object, not a full database.

## Official References

- S3 replication: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html>
- S3 Object Lock: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html>
- S3 Batch Operations: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html>
