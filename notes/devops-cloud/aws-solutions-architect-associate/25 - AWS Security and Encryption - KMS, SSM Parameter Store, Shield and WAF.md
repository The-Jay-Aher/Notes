# AWS Security and Encryption: KMS, SSM Parameter Store, Shield and WAF

## Quick Summary
- KMS manages encryption keys used by many AWS services.
- SSM Parameter Store stores configuration values and can store encrypted secure strings.
- Secrets Manager stores and rotates secrets such as database passwords and API keys.
- WAF protects web applications from common HTTP-layer attacks.
- Shield protects against DDoS attacks, with Shield Standard included automatically and Shield Advanced available for stronger protection.
- Security Hub, GuardDuty, Inspector, Macie, and Firewall Manager are important supporting security services.

## Security Layers
AWS security is layered.

```text
Identity -> Network -> Data encryption -> Detection -> Response -> Governance
```

Common services:
- IAM for identity and permissions.
- VPC security groups and NACLs for network controls.
- KMS for encryption keys.
- WAF and Shield for edge/web protection.
- GuardDuty, Inspector, Security Hub, and Macie for detection and findings.
- CloudTrail, Config, and CloudWatch for audit and monitoring.

## AWS KMS
AWS Key Management Service manages cryptographic keys.

KMS is used by many services:
- S3.
- EBS.
- RDS.
- DynamoDB.
- Lambda environment variables.
- CloudWatch Logs.
- EFS.
- Secrets Manager.
- SSM Parameter Store SecureString.

## KMS Key Types
Common categories:
- AWS owned keys.
- AWS managed keys.
- Customer managed keys.

### AWS Owned Keys
Managed entirely by AWS. You usually do not see or control them directly.

### AWS Managed Keys
Created and managed by AWS for a specific service in your account.

Examples:
- `aws/s3`.
- `aws/ebs`.

Simple to use, but with less control.

### Customer Managed Keys
Created and managed by you.

Use them when you need:
- Custom key policy.
- Rotation control.
- Grants.
- Cross-account usage.
- CloudTrail tracking at key level.
- Deletion scheduling control.

## KMS Key Policy
KMS key policy is critical.

For many services, IAM permission alone is not always enough. The KMS key policy must also allow usage or delegate permission to IAM.

Common debugging issue:
- User can read S3 object, but object is encrypted with a KMS key the user cannot decrypt.

Then S3 access succeeds at the bucket policy level but KMS denies decrypt.

## Envelope Encryption
KMS commonly uses envelope encryption.

Simplified:
1. KMS protects a data key.
2. Data key encrypts the actual data.
3. Encrypted data key is stored with the encrypted data.
4. To decrypt, the data key is decrypted through KMS permissions.

This avoids sending large data directly to KMS.

## SSM Parameter Store
AWS Systems Manager Parameter Store stores configuration values.

Parameter types:
- String.
- StringList.
- SecureString.

Use Parameter Store for:
- Non-secret configuration.
- Environment-specific settings.
- Simple encrypted values.
- Values referenced by EC2, Lambda, ECS, and automation.

SecureString uses KMS for encryption.

## Secrets Manager
Secrets Manager is designed for secrets.

Use it for:
- Database credentials.
- API keys.
- OAuth credentials.
- Automatic secret rotation.

Parameter Store vs Secrets Manager:

| Requirement | Better fit |
|---|---|
| Non-secret config | Parameter Store |
| Simple encrypted config | Parameter Store SecureString |
| Secret rotation needed | Secrets Manager |
| Managed database password rotation | Secrets Manager |

## AWS WAF
AWS WAF is a web application firewall.

It protects HTTP/HTTPS applications.

Can be associated with:
- CloudFront distributions.
- Application Load Balancers.
- API Gateway.
- AppSync.
- Cognito user pools in supported scenarios.

WAF can block or allow requests based on:
- IP addresses.
- HTTP headers.
- URI paths.
- Query strings.
- Request body patterns.
- Rate-based rules.
- Managed rule groups.

Use WAF for:
- SQL injection protection.
- Cross-site scripting protection.
- Bot/rate controls.
- Geo match rules.
- Application-specific blocking.

## AWS Shield
AWS Shield protects against DDoS attacks.

### Shield Standard
Included automatically for AWS customers.

Provides protection against common network and transport layer DDoS attacks.

### Shield Advanced
Paid service with enhanced protections.

Use it when:
- You have important public applications.
- You need stronger DDoS response support.
- You need cost protection for scaling charges in covered DDoS events.
- You need advanced detection and response features.

Often used with:
- CloudFront.
- Route 53.
- Global Accelerator.
- Elastic IP.
- ALB.

## AWS Firewall Manager
Firewall Manager centrally manages security policies across accounts in AWS Organizations.

Use it for:
- WAF policies.
- Shield Advanced policies.
- Security group policies.
- Network Firewall policies.
- Route 53 Resolver DNS Firewall policies.

It is useful when many accounts must follow the same protection standards.

## Amazon GuardDuty
GuardDuty is a threat detection service.

It analyzes data sources such as:
- CloudTrail events.
- VPC Flow Logs.
- DNS logs.
- EKS audit logs and other supported sources.

Findings can indicate:
- Compromised credentials.
- Suspicious network activity.
- Crypto-mining behavior.
- Unusual API calls.

## Amazon Inspector
Inspector scans workloads for vulnerabilities and exposure.

It can scan:
- EC2 instances.
- ECR container images.
- Lambda functions in supported configurations.

Use it for vulnerability management.

## AWS Security Hub
Security Hub aggregates security findings and checks against standards.

Use it to:
- Centralize findings from GuardDuty, Inspector, Macie, IAM Access Analyzer, and partner tools.
- Track compliance posture.
- Prioritize security issues.

## Amazon Macie
Macie discovers and helps protect sensitive data in S3.

Use it to find:
- Personally identifiable information.
- Sensitive data patterns.
- Buckets with risky exposure.

## Network Firewall and DNS Firewall
AWS Network Firewall provides managed network firewall capabilities for VPC traffic.

Route 53 Resolver DNS Firewall filters outbound DNS queries from VPCs.

Use these when you need deeper network controls than security groups and NACLs alone.

## Security Architecture Examples
### Public Web Application
```text
Users -> CloudFront -> WAF -> ALB -> application
                 |
              Shield
```

Add:
- ACM TLS certificates.
- KMS encryption for data stores.
- CloudTrail and Config.
- GuardDuty and Security Hub.

### Secret Storage
```text
Application role -> Secrets Manager -> KMS decrypt -> database password
```

Do not store secrets in code, AMIs, images, or public repositories.

## Common Mistakes
- Assuming S3 encryption works without KMS permissions.
- Using Parameter Store for secrets that require rotation.
- Storing passwords in Lambda environment variables without encryption and access controls.
- Thinking WAF protects non-HTTP database traffic.
- Thinking Shield replaces secure application design.
- Enabling security tools but not routing findings to anyone.
- Leaving KMS key policies overly broad.

## Official References
- [AWS KMS documentation](https://docs.aws.amazon.com/kms/)
- [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [AWS Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/)
- [AWS WAF documentation](https://docs.aws.amazon.com/waf/)
- [AWS Shield documentation](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)
- [AWS Firewall Manager documentation](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)
- [Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/)
- [Amazon Inspector documentation](https://docs.aws.amazon.com/inspector/)
- [AWS Security Hub documentation](https://docs.aws.amazon.com/securityhub/)
- [Amazon Macie documentation](https://docs.aws.amazon.com/macie/)
