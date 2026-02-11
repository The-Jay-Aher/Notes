# 3 - Terraform Fundamentals

## Variables

Variables parameterize your configuration so code is reusable.

Common usage:

- Environment-specific values
- Naming conventions
- Region/size settings

Reference syntax:

- `var.example_name`

## Variable Types

Primitive types:

- `string`
- `number`
- `bool`

Collection/structural types:

- `list(type)`
- `set(type)`
- `map(type)`
- `tuple([...])`
- `object({...})`

Dynamic type:

- `any` (use carefully; explicit types are usually clearer)

## Variable Files

Common files:

- `terraform.tfvars`
- `*.auto.tfvars`

Prefer variable files over hardcoded values in main configuration.

## Sensitive Values

Mark variables/outputs as sensitive when needed.

Example concept:

- `sensitive = true`

This helps prevent accidental display in CLI output, but does not replace proper secret management.

## Outputs

Outputs expose selected values after apply.

Use cases:

- Share IDs/endpoints with users
- Feed values into downstream automation

## Provisioners (Use Sparingly)

Provisioners can run scripts/commands during create/destroy events.

Common types:

- `local-exec`
- `remote-exec`

Important cautions:

- Provisioners are not fully declarative.
- They can reduce predictability and idempotence.
- Prefer cloud-init/user-data or configuration tooling where possible.

## Validation and Formatting Commands

- `terraform fmt` for formatting
- `terraform validate` for config validation

## Quick Summary

1. Variables and outputs make Terraform reusable and composable.
2. Strong type constraints improve safety and readability.
3. Provisioners are a last resort, not first choice.
