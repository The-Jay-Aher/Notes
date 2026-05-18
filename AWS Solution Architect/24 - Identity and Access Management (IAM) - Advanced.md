# Identity and Access Management (IAM) - Advanced

## Quick Summary
- IAM controls who can do what in AWS.
- Advanced IAM is mostly about policy evaluation, cross-account access, permissions boundaries, STS, federation, IAM Identity Center, and Organizations SCPs.
- IAM policies are JSON documents that allow or deny actions on resources under conditions.
- Explicit deny wins over allow.
- For real companies, design identity centrally and avoid long-term access keys where possible.

## IAM Policy Evaluation
When a request is made, AWS evaluates policies to decide whether it is allowed.

Core idea:

```text
Default = deny
Explicit allow = allow
Explicit deny = deny, even if another policy allows
```

Important policy types:
- Identity-based policies.
- Resource-based policies.
- Permissions boundaries.
- Service control policies.
- Session policies.
- Access control lists in services that still support them.

## Identity-Based Policies
Attached to:
- IAM users.
- IAM groups.
- IAM roles.

They say what the identity can do.

Example:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::example-bucket"
    }
  ]
}
```

## Resource-Based Policies
Attached to resources.

Examples:
- S3 bucket policies.
- KMS key policies.
- SQS queue policies.
- SNS topic policies.
- Lambda resource policies.
- ECR repository policies.

They say who can access the resource.

Resource policies are important for cross-account access.

## IAM Roles
Roles are identities meant to be assumed.

Use roles for:
- EC2 instances.
- Lambda functions.
- ECS tasks.
- Cross-account access.
- Federated users.
- CI/CD deployments.

Do not store long-term access keys on workloads. Use roles.

## STS
AWS Security Token Service provides temporary credentials.

Common actions:
- `AssumeRole`.
- `AssumeRoleWithSAML`.
- `AssumeRoleWithWebIdentity`.
- `GetSessionToken`.

Temporary credentials include:
- Access key ID.
- Secret access key.
- Session token.
- Expiration time.

Benefits:
- Short-lived access.
- Easier rotation.
- Reduced risk compared with long-term keys.

## Cross-Account Access
To allow account A to access account B, commonly:

1. Create a role in account B.
2. Trust account A or a role/user in account A.
3. Grant permissions to the role in account B.
4. Account A assumes the role.

Trust policy controls who can assume the role.
Permissions policy controls what the role can do after assumption.

Both are needed.

### Example Trust Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/DeploymentRole"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## External ID
External ID helps protect against the confused deputy problem for third-party cross-account access.

Use it when:
- A third-party SaaS provider needs to assume a role in your account.
- You want to ensure the provider assumes the role only for your tenant/customer context.

## Permissions Boundaries
A permissions boundary sets the maximum permissions an IAM user or role can have.

It does not grant permissions by itself.

Think of it as:

```text
Effective permissions = identity policy allowed actions limited by boundary
```

Use it when:
- Developers can create roles but should not create unlimited permissions.
- Platform teams want delegation with guardrails.

## Service Control Policies
Service Control Policies are AWS Organizations guardrails.

SCPs define maximum permissions for accounts or organizational units.

Important:
- SCPs do not grant permissions.
- SCPs limit what identities in member accounts can do.
- Management account behavior has special considerations.

Example use cases:
- Deny disabling CloudTrail.
- Deny leaving the organization.
- Deny use of unapproved Regions.
- Deny deleting security logs.

## IAM Identity Center
IAM Identity Center provides centralized workforce access to AWS accounts and applications.

Use it for:
- Single sign-on to multiple AWS accounts.
- Permission sets.
- Integration with identity providers.
- Avoiding separate IAM users for every human.

Modern recommendation:
- Prefer federated access and IAM Identity Center for humans.
- Prefer IAM roles for workloads.
- Avoid long-term IAM user access keys when possible.

## Federation
Federation lets users authenticate outside AWS and receive AWS access.

Common types:
- SAML federation.
- OIDC federation.
- Web identity federation.

Examples:
- Corporate identity provider to AWS accounts.
- GitHub Actions OIDC to assume AWS deployment role.
- EKS service accounts assuming IAM roles.

## Policy Conditions
Conditions restrict when a statement applies.

Common condition keys:
- Source IP.
- MFA present.
- Requested Region.
- Resource tags.
- Principal tags.
- VPC endpoint.
- Secure transport.

Example idea:
- Allow S3 access only if request uses TLS.
- Allow EC2 actions only in approved Regions.
- Allow access to resources with matching department tag.

## Attribute-Based Access Control
ABAC uses tags and attributes to control access.

Example:
- A user tagged `Department=Finance` can access resources tagged `Department=Finance`.

ABAC helps reduce policy sprawl in large environments, but it requires strict tag governance.

## IAM Access Analyzer
IAM Access Analyzer helps find unintended access.

It can analyze:
- External access to resources.
- Unused access in some workflows.
- Policy validation findings.

Use it to review resource policies and least-privilege improvements.

## MFA and Root User
Root user:
- Has full account access.
- Should not be used for daily tasks.
- Should have MFA enabled.
- Should have no access keys unless absolutely required.

Human admin access:
- Use IAM Identity Center or federated roles.
- Require MFA.
- Log activity with CloudTrail.

## Common Policy Debugging Steps
1. Check if there is an explicit deny.
2. Check identity-based policies.
3. Check resource-based policies.
4. Check permissions boundary.
5. Check SCP.
6. Check session policy.
7. Check KMS key policy if encrypted resources are involved.
8. Check conditions such as Region, MFA, tags, and VPC endpoint.

## Common Mistakes
- Giving `AdministratorAccess` to automation because it is faster.
- Forgetting that explicit deny overrides allow.
- Creating a cross-account role but missing the trust policy.
- Creating a trust policy but forgetting permissions.
- Using IAM users and long-term keys for applications.
- Forgetting KMS key policy when S3/RDS/EBS access looks correct.
- Not enabling MFA for root and privileged access.

## Official References
- [AWS IAM documentation](https://docs.aws.amazon.com/iam/)
- [IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)
- [AWS STS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
- [IAM Identity Center documentation](https://docs.aws.amazon.com/singlesignon/)
- [AWS Organizations service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [IAM Access Analyzer documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
