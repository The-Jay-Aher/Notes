# 10 - Amazon S3 Introduction

## Quick Summary

Amazon S3 is AWS object storage. It stores data as objects inside buckets. S3 is commonly used for backups, archives, static websites, data lakes, logs, media, application assets, and integration events.

Beginner mental model:

```text
bucket = container
object = file/data plus metadata
key = object path/name
```

## Object Storage vs Block/File Storage

| Storage Type | AWS Example | Best For |
| --- | --- | --- |
| Object | S3 | Files, backups, media, logs, data lake objects. |
| Block | EBS | EC2 disks, databases, boot volumes. |
| File | EFS/FSx | Shared filesystem access. |

S3 is not mounted like a normal disk by default. Applications use S3 APIs.

## Buckets

A bucket is the top-level container.

Important:

- Bucket names are globally unique.
- Buckets are created in a Region.
- Bucket name becomes part of object URL patterns.
- Bucket settings control security, versioning, encryption, lifecycle, and logging.

## Objects

An object includes:

- Key.
- Value/data.
- Metadata.
- Version ID if versioning is enabled.
- Tags.
- Access control/policy context.

Example key:

```text
logs/2026/05/18/app.log
```

S3 key names can look like folders, but S3 is object storage, not a traditional directory filesystem.

## Common Use Cases

- Backup storage.
- Static website assets.
- Application file uploads.
- Data lake raw/processed zones.
- Log delivery.
- Media storage.
- Disaster recovery copies.
- Software artifacts.

## S3 Storage Classes

| Class | Use |
| --- | --- |
| S3 Standard | Frequent access. |
| S3 Intelligent-Tiering | Unknown/changing access patterns. |
| S3 Standard-IA | Infrequent access, quick retrieval. |
| S3 One Zone-IA | Infrequent access, single AZ, lower cost. |
| S3 Glacier Instant Retrieval | Archive with millisecond retrieval. |
| S3 Glacier Flexible Retrieval | Archive retrieval in minutes to hours. |
| S3 Glacier Deep Archive | Lowest-cost long-term archive, hours retrieval. |

Choose storage class based on access frequency, retrieval time, durability/availability needs, and cost.

## Versioning

Versioning keeps multiple versions of objects.

Benefits:

- Recover overwritten/deleted objects.
- Useful with replication.
- Helps protect against accidental changes.

Watch-outs:

- Deleting creates delete markers.
- Old versions still cost money.
- Lifecycle rules should manage old versions.

## Lifecycle Rules

Lifecycle rules can:

- Transition objects to cheaper storage classes.
- Expire old objects.
- Remove incomplete multipart uploads.
- Manage noncurrent versions.

Example idea:

```text
logs -> S3 Standard for 30 days -> Glacier Flexible Retrieval for 1 year -> expire
```

## S3 Event Notifications

S3 can emit events when objects are created/deleted.

Common targets:

- Lambda.
- SQS.
- SNS.
- EventBridge.

Pattern:

```text
File uploaded to S3 -> event -> Lambda processes file
```

## Benefits

- Highly durable object storage.
- Massive scale.
- Many storage classes.
- Strong AWS integrations.
- Lifecycle and event automation.
- Server-side encryption options.

## Drawbacks / Limitations

- Not a normal filesystem.
- Request costs matter at scale.
- Retrieval costs/time matter for archive classes.
- Public access misconfiguration can expose data.
- Object updates replace whole objects.

## Hidden Details / Caveats

- Bucket names are globally unique.
- Prefixes affect organization and sometimes performance design.
- S3 consistency is strong for reads after writes and list operations in modern S3, but app design should still handle distributed-system errors.
- Multipart upload is used for large objects.
- Lifecycle expiration can permanently delete data.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Treating S3 like a disk | Use object API patterns. |
| Public bucket by accident | Use Block Public Access and bucket policies carefully. |
| No lifecycle rules | Add retention/cost rules. |
| Versioning without cleanup | Manage noncurrent versions. |
| Wrong storage class | Match access and retrieval needs. |

## Interview Notes

- S3 stores objects in buckets.
- Bucket names are globally unique.
- Versioning protects against overwrite/delete mistakes.
- Lifecycle rules manage cost and retention.
- S3 events can trigger Lambda/SQS/SNS/EventBridge.
- Storage class selection is a cost/access trade-off.

## Official References

- Amazon S3 documentation: <https://docs.aws.amazon.com/s3/>
- S3 User Guide: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>
