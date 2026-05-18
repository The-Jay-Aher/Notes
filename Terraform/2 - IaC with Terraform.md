# 2 - IaC with Terraform

## Quick Summary

Terraform workflow is built around `init`, `plan`, `apply`, and `destroy`. You write configuration, initialize providers/backends, preview changes, apply changes, and manage the resulting state.

## Terraform Workflow

```text
write .tf files -> terraform init -> terraform fmt/validate -> terraform plan -> terraform apply
```

For destruction:

```text
terraform plan -destroy -> review -> terraform destroy
```

## Terraform Files

Common files:

| File | Purpose |
| --- | --- |
| `main.tf` | Main resources/modules. |
| `variables.tf` | Input variable declarations. |
| `outputs.tf` | Output values. |
| `providers.tf` | Required providers and provider config. |
| `versions.tf` | Terraform/provider version constraints. |
| `terraform.tfvars` | Variable values, often not for secrets. |

Terraform loads `.tf` files in the directory as one configuration, regardless of filename order.

## terraform init

`terraform init` prepares the working directory.

It:

- Downloads providers.
- Initializes backend.
- Downloads modules.
- Creates `.terraform/`.
- Creates or updates `.terraform.lock.hcl`.

Command:

```bash
terraform init
```

Run init when:

- Starting a new configuration.
- Changing provider requirements.
- Changing backend config.
- Adding/changing modules.

## terraform fmt

Formats Terraform code consistently.

```bash
terraform fmt
terraform fmt -recursive
```

Use in CI to prevent formatting drift:

```bash
terraform fmt -check -recursive
```

## terraform validate

Checks syntax and basic configuration validity.

```bash
terraform validate
```

It does not prove the cloud credentials, quotas, or runtime behavior are correct.

## terraform plan

Creates an execution plan.

```bash
terraform plan
```

Plan shows actions:

| Symbol | Meaning |
| --- | --- |
| `+` | Create. |
| `~` | Update in place. |
| `-/+` | Replace. |
| `-` | Destroy. |

Save a plan:

```bash
terraform plan -out=tfplan
terraform apply tfplan
```

Saved plans are useful for approval because apply runs exactly what was planned.

## terraform apply

Applies planned changes.

```bash
terraform apply
```

Auto-approve only in controlled automation:

```bash
terraform apply -auto-approve
```

Do not use `-auto-approve` casually on a laptop for production.

## terraform destroy

Destroys managed infrastructure.

```bash
terraform destroy
```

Safer preview:

```bash
terraform plan -destroy
```

Be careful with shared environments, databases, stateful resources, and resources with deletion protection.

## Providers

Providers let Terraform talk to APIs.

Example:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}
```

## Resources And Data Sources

Resource: Terraform manages lifecycle.

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "example-logs"
}
```

Data source: Terraform reads existing information.

```hcl
data "aws_caller_identity" "current" {}
```

## Benefits

- Clear workflow.
- Plan review before change.
- Provider ecosystem.
- State-based management.
- CI/CD friendly.

## Drawbacks / Limitations

- Plan can become stale if infrastructure changes before apply.
- Provider/API errors still happen during apply.
- Destroy is powerful and dangerous.
- Credentials and permissions must be correct.
- Parallelism can hit service limits.

## Hidden Details / Caveats

- `.terraform.lock.hcl` should usually be committed.
- `.terraform/` should not be committed.
- Terraform compares configuration, state, and provider-read remote objects.
- A saved plan can contain sensitive values.
- Plan output can hide sensitive values but state may still contain them.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Skipping plan review | Review create/update/replace/destroy actions. |
| Not committing lock file | Commit `.terraform.lock.hcl`. |
| Running apply from many places | Use remote state and locking. |
| Using destroy without preview | Run `plan -destroy` first. |
| Assuming validate checks cloud permissions | Use plan/apply in a safe environment. |

## Interview Notes

- `init` downloads providers/modules and configures backend.
- `plan` previews changes.
- `apply` executes changes.
- `destroy` removes managed resources.
- Resources manage objects; data sources read objects.
- Lock file pins provider selections.

## Related Topics

- [Terraform Fundamentals](3%20-%20Terraform%20Fundamentals.md)
- [Terraform State](4%20-%20Terraform%20State.md)

