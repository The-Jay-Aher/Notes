# 12 - Amazon S3 Security

## Quick Summary

S3 security controls who can access buckets/objects, how data is encrypted, whether public access is blocked, how actions are logged, and how accidental or malicious deletion is prevented. Most S3 incidents come from overly broad permissions, public access mistakes, or weak data governance.

## Main Security Layers

| Layer | Purpose |
| --- | --- |
| IAM policies | Control AWS principal permissions. |
| Bucket policies | Resource-based policies on buckets. |
| Access Control Lists | Older object/bucket permission mechanism; avoid unless needed. |
| Block Public Access | Guardrail against public exposure. |
| Encryption | Protect data at rest. |
| Versioning/Object Lock | Protect against overwrite/delete. |
| Logging/CloudTrail | Audit activity. |

## IAM Policy vs Bucket Policy

IAM policy:

```text
Attached to user/role/group
Says what that principal can do
```

Bucket policy:

```text
Attached to bucket
Says who can access that bucket and under what conditions
```

Use both carefully. Access is granted only when policy evaluation allows it and no explicit deny blocks it.

## Block Public Access

S3 Block Public Access is a safety feature that can block public bucket/object access even if a policy or ACL would allow it.

Best practice:

- Keep Block Public Access enabled unless public access is intentionally required.
- For public websites, prefer CloudFront with private S3 origin where possible.

## Bucket Policy Example

Allow read only through a specific CloudFront origin access control pattern is usually configured with AWS-generated policy. For beginner understanding:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::example-bucket",
        "arn:aws:s3:::example-bucket/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

This denies non-HTTPS access.

## Encryption Options

| Option | Meaning |
| --- | --- |
| SSE-S3 | Server-side encryption with S3-managed keys. |
| SSE-KMS | Server-side encryption with AWS KMS keys. |
| SSE-C | Server-side encryption with customer-provided keys. |
| Client-side encryption | App encrypts before uploading. |

Most AWS architectures use SSE-S3 or SSE-KMS.

## SSE-S3 vs SSE-KMS

| Feature | SSE-S3 | SSE-KMS |
| --- | --- | --- |
| Key management | S3-managed. | KMS-managed. |
| Audit key usage | Less detailed. | KMS CloudTrail events. |
| Access control | S3 permissions. | S3 plus KMS key permissions. |
| Use case | Simple default encryption. | Stronger key control/audit/compliance. |

## Bucket Keys

S3 Bucket Keys can reduce KMS request costs for SSE-KMS encrypted objects by reducing calls to KMS.

Use when:

- Large number of SSE-KMS S3 requests.
- Cost optimization is needed.

## Pre-Signed URLs

Pre-signed URLs grant temporary access to an S3 object using the permissions of the signer.

Use cases:

- Temporary download link.
- Direct client upload without exposing AWS credentials.

Warning:

- Anyone with the URL can use it until expiry unless other controls block access.
- Keep expiry short.

## Access Points

S3 Access Points provide named network/policy entry points to buckets.

Use for:

- Large shared data buckets.
- Different teams/apps needing different access policies.
- VPC-restricted access patterns.

## Logging And Audit

Options:

- AWS CloudTrail data events for object-level API activity.
- S3 server access logs.
- S3 Storage Lens for storage usage insights.
- AWS Config rules for compliance checks.

## Protecting Against Deletion

Controls:

- Versioning.
- MFA Delete, where applicable and operationally suitable.
- Object Lock.
- Replication.
- Least-privilege delete permissions.
- Backup copies in another account/Region.

## Benefits

- Strong policy controls.
- Encryption options from simple to advanced.
- Public access guardrails.
- Temporary access with pre-signed URLs.
- Compliance retention with Object Lock.

## Drawbacks / Limitations

- S3 policy evaluation can be confusing.
- KMS permissions can block S3 reads even if S3 policy allows.
- Public access settings can override expected bucket policy behavior.
- Pre-signed URLs are bearer tokens.

## Hidden Details / Caveats

- Explicit deny wins over allow.
- Bucket owner enforced object ownership can disable ACL usage.
- Cross-account access often needs both bucket policy and IAM permissions.
- SSE-KMS requires KMS key permissions for decrypt.
- CloudTrail object-level data events may need explicit configuration and can add cost.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Public bucket by accident | Keep Block Public Access on. |
| S3 allow but KMS deny | Check KMS key policy/IAM permissions. |
| Long-lived pre-signed URLs | Use short expiry. |
| Using ACLs unnecessarily | Prefer IAM/bucket policies and object ownership controls. |
| No audit of object access | Enable CloudTrail data events where needed. |

## Troubleshooting

| Problem | Check |
| --- | --- |
| AccessDenied | IAM policy, bucket policy, explicit deny, KMS key policy, Block Public Access. |
| Public website not working | Bucket policy, website endpoint, Block Public Access, CloudFront config. |
| KMS-encrypted object unreadable | KMS decrypt permission and key policy. |
| Pre-signed URL fails | Expiry, signer permissions, object key, method mismatch. |

## Interview Notes

- Block Public Access is a guardrail against public exposure.
- Bucket policy is resource-based; IAM policy is identity-based.
- SSE-S3 is S3-managed encryption; SSE-KMS uses KMS keys.
- Pre-signed URLs provide temporary access.
- Explicit deny overrides allow.
- Versioning/Object Lock help protect against delete/overwrite risks.

## Official References

- S3 security: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html>
- S3 encryption: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html>
- S3 Block Public Access: <https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html>
