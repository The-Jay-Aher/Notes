# 3 - Terraform Fundamentals

## Quick Summary

Terraform fundamentals include variables, values, types, locals, outputs, provisioners, validation, and formatting. These decide how reusable, safe, and understandable your Terraform code is.

## Variables

Input variables let callers customize a module.

```hcl
variable "environment" {
  description = "Environment name, such as dev, staging, or prod."
  type        = string
  default     = "dev"
}
```

Use:

```hcl
tags = {
  Environment = var.environment
}
```

## Variable Types

Primitive types:

```hcl
string
number
bool
```

Collection types:

```hcl
list(string)
set(string)
map(string)
```

Structural types:

```hcl
object({
  name = string
  port = number
})

tuple([string, number, bool])
```

Prefer explicit types for module inputs.

## Variable Validation

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```

Validation catches mistakes before resources are changed.

## Variable Values

Ways to set variables:

```bash
terraform apply -var="environment=prod"
terraform apply -var-file="prod.tfvars"
TF_VAR_environment=prod terraform plan
```

Auto-loaded files:

- `terraform.tfvars`
- `terraform.tfvars.json`
- `*.auto.tfvars`
- `*.auto.tfvars.json`

## Sensitive Values

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

Sensitive hides values in CLI output, but it does not guarantee they are absent from state. Treat state as sensitive.

## Locals

Locals define reusable expressions.

```hcl
locals {
  name_prefix = "${var.environment}-${var.app_name}"
  common_tags = {
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}
```

Use locals to reduce repeated expressions, not to hide complex logic.

## Outputs

Outputs expose values after apply or from modules.

```hcl
output "bucket_name" {
  description = "Created S3 bucket name."
  value       = aws_s3_bucket.logs.bucket
}
```

Sensitive output:

```hcl
output "password" {
  value     = random_password.db.result
  sensitive = true
}
```

## Provisioners

Provisioners run scripts or commands during resource creation/destruction.

Examples:

- `local-exec`
- `remote-exec`

Use sparingly. Prefer cloud-init/user data, image baking, configuration management, or native provider resources.

Provisioners are a last resort because they can make applies less predictable.

## Validation And Formatting Commands

```bash
terraform fmt -recursive
terraform validate
terraform plan
```

## Benefits

- Variables make modules reusable.
- Type constraints catch bad inputs.
- Validation gives helpful errors.
- Locals reduce duplication.
- Outputs connect modules and automation.

## Drawbacks / Limitations

- Overly complex variables make modules hard to use.
- Sensitive values may still exist in state.
- Provisioners can create hidden side effects.
- Locals can become confusing if used as mini-programming.

## Hidden Details / Caveats

- Terraform variable precedence matters when values come from multiple places.
- `sensitive = true` affects display, not all storage.
- Outputs from child modules must be explicitly declared.
- Environment variable form is `TF_VAR_name`.
- Avoid committing real secret values in tfvars files.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| No variable types | Add explicit `type`. |
| Magic strings repeated everywhere | Use variables/locals. |
| Secrets in committed tfvars | Use secret management. |
| Provisioners for normal setup | Use user data/images/config tools. |
| No validation for constrained inputs | Add validation blocks. |

## Interview Notes

- Variables are module inputs.
- Locals are internal named expressions.
- Outputs expose values.
- Sensitive hides display but state still needs protection.
- Provisioners should be last resort.
- Type constraints improve correctness.

## Related Topics

- [Terraform Modules](5%20-%20Terraform%20Modules.md)
- [Terraform State](4%20-%20Terraform%20State.md)

