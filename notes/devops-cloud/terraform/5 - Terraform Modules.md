# 5 - Terraform Modules

## Quick Summary

A Terraform module is a directory of Terraform configuration. Modules let you package reusable infrastructure patterns with inputs and outputs.

Every Terraform configuration has a root module. Child modules are called from the root or from other modules.

## Why Use Modules

Modules help:

- Reduce duplication.
- Standardize infrastructure patterns.
- Hide implementation details.
- Improve review and reuse.
- Enforce naming/tagging conventions.

Example:

```text
Use one VPC module for dev, staging, and prod instead of rewriting VPC resources three times.
```

## Module Structure

Common module layout:

```text
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
    README.md
```

Root module:

```text
envs/
  prod/
    main.tf
    variables.tf
    backend.tf
```

## Calling A Module

```hcl
module "vpc" {
  source = "../../modules/vpc"

  name       = "prod"
  cidr_block = "10.0.0.0/16"
}
```

## Module Sources

| Source | Example |
| --- | --- |
| Local path | `../../modules/vpc` |
| Terraform Registry | `terraform-aws-modules/vpc/aws` |
| Git | `git::https://github.com/org/terraform-modules.git//vpc?ref=v1.2.0` |
| HTTP/archive | Less common; use carefully. |

Pin remote module versions.

## Inputs

Child module variable:

```hcl
variable "cidr_block" {
  type        = string
  description = "VPC CIDR block."
}
```

Caller passes value:

```hcl
module "vpc" {
  source     = "../../modules/vpc"
  cidr_block = "10.0.0.0/16"
}
```

## Outputs

Child module:

```hcl
output "vpc_id" {
  value = aws_vpc.this.id
}
```

Caller uses:

```hcl
module.vpc.vpc_id
```

## Module Versioning

For registry modules:

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
}
```

For Git modules:

```hcl
source = "git::https://github.com/org/modules.git//vpc?ref=v1.2.3"
```

Avoid pointing production modules at a moving branch such as `main` unless your process intentionally handles that risk.

## Module Design Best Practices

- Keep modules focused.
- Use clear variable names and descriptions.
- Set useful defaults only when safe.
- Expose outputs that callers actually need.
- Avoid hiding too many unrelated resources in one module.
- Do not put provider credentials inside modules.
- Document examples.
- Add validation for constrained inputs.

## Benefits

- Reuse.
- Standardization.
- Cleaner root modules.
- Easier governance.
- Faster environment creation.

## Drawbacks / Limitations

- Over-abstracted modules are hard to use.
- Module changes can affect many environments.
- Versioning must be managed.
- Debugging nested modules can be harder.
- Generic modules can become full of flags and conditionals.

## Hidden Details / Caveats

- A module is just a Terraform directory.
- Root module is the current working directory.
- Child module state is still stored in the root module's state.
- Module `source` changes may require `terraform init`.
- Outputs are the public interface of a module.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| One module does everything | Split by responsibility. |
| No version pinning | Pin module versions. |
| Too many booleans | Consider smaller modules. |
| Missing outputs | Expose required integration values. |
| Hard-coded names/tags | Use variables and locals. |

## Interview Notes

- Root module is where Terraform runs.
- Child modules are called with `module` blocks.
- Modules use variables as inputs and outputs as outputs.
- Remote modules should be versioned.
- Modules improve reuse but can be over-abstracted.

## Related Topics

- [Terraform Fundamentals](3%20-%20Terraform%20Fundamentals.md)
- [Built-In Functions and Dynamic Blocks](6%20-%20Built-In%20Functions%20and%20Dynamic%20Blocks.md)

