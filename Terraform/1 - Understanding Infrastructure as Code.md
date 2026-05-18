# 1 - Understanding Infrastructure as Code

## Quick Summary

Infrastructure as Code (IaC) means managing infrastructure with files instead of manual console clicks. You describe infrastructure in code, store it in version control, review it, test it, and apply it repeatedly.

Terraform is a declarative IaC tool: you describe the desired end state, and Terraform works out the changes needed to reach it.

## Why It Matters

Manual infrastructure is hard to reproduce:

- People forget exact settings.
- Environments drift.
- Review is difficult.
- Rollback is unclear.
- Documentation becomes stale.

IaC improves this by making infrastructure:

- Version-controlled.
- Reviewable.
- Repeatable.
- Auditable.
- Easier to automate.

## What IaC Manages

Examples:

- VPCs and subnets.
- Security groups/firewall rules.
- Load balancers.
- Databases.
- IAM roles and policies.
- Kubernetes resources.
- DNS records.
- Monitoring alerts.
- CI/CD infrastructure.

## Declarative vs Imperative

| Style | Meaning | Example |
| --- | --- | --- |
| Declarative | Describe desired state. | "There should be three private subnets." |
| Imperative | Describe exact steps. | "Click here, create subnet, then attach route." |

Terraform is declarative.

Example:

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "example-app-logs"
}
```

You do not write every API call. Terraform uses the provider to compare configuration, state, and real infrastructure.

## Why Terraform

Terraform is popular because:

- It supports many providers.
- It has a clear plan/apply workflow.
- It stores state to track managed resources.
- It supports modules for reuse.
- It works with CI/CD.
- It can manage multi-cloud and SaaS resources.

## IaC Benefits

| Benefit | Explanation |
| --- | --- |
| Consistency | Same configuration can create similar environments. |
| Speed | Repeatable provisioning is faster than manual work. |
| Review | Pull requests can review infra changes. |
| Audit | Git history shows who changed what. |
| Reuse | Modules avoid repeated patterns. |
| Recovery | Infrastructure can be recreated more easily. |
| Governance | Policy checks can run before apply. |

## Drawbacks / Limitations

- IaC mistakes can break infrastructure quickly.
- State must be protected.
- Providers can have bugs or behavior changes.
- Secrets can accidentally enter state.
- Drift still happens if people change resources manually.
- Large Terraform projects can become slow and hard to reason about.

## Hidden Details / Caveats

- Terraform code is not the full truth; state and real infrastructure also matter.
- `terraform plan` is a prediction, not a guarantee that apply cannot fail.
- Some resource changes force replacement.
- Manual console changes can create drift.
- IaC does not remove the need to understand the cloud service.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Learning Terraform without learning AWS/cloud basics | Learn the resource behavior too. |
| Storing secrets in variables/state | Use secret managers and sensitive handling. |
| Running apply from multiple machines without locking | Use remote state with locking. |
| Making one huge root module | Split by lifecycle and ownership. |
| Blindly applying plans | Review changes before apply. |

## Best Practices

- Store configuration in Git.
- Use pull requests for infrastructure changes.
- Use remote state for team work.
- Enable state locking where supported.
- Keep modules focused.
- Pin provider versions with appropriate constraints.
- Run `terraform fmt` and `terraform validate`.
- Review plans carefully before apply.

## Interview Notes

- IaC manages infrastructure through code.
- Terraform is declarative.
- Providers let Terraform manage external APIs.
- State maps Terraform resources to real infrastructure.
- Plan shows proposed changes; apply executes them.
- Remote state and locking are important for teams.

## Related Topics

- [IaC with Terraform](2%20-%20IaC%20with%20Terraform.md)
- [Terraform State](4%20-%20Terraform%20State.md)

