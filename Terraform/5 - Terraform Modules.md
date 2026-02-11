# 5 - Terraform Modules

## What a Module Is

A module is a container for Terraform resources used together.

- Every Terraform configuration has a **root module**.
- Reusable child modules help standardize and scale infrastructure patterns.

## Why Use Modules

- Reuse common infrastructure patterns
- Improve readability by reducing duplication
- Enforce consistent architecture and guardrails

## Module Sources

Modules can be sourced from:

- Terraform Registry
- Private registry
- VCS repositories (for example Git)
- Local filesystem paths

## Declaring a Module

A module is declared with a `module` block and typically includes:

- `source`
- input variables
- optional meta-arguments (`count`, `for_each`, `depends_on`, `providers`)

## Module Inputs and Outputs

### Inputs

- Values passed into a module.
- Defined in module via `variable` blocks.

### Outputs

- Values exposed by a module via `output` blocks.
- Referenced from root module as:
  - `module.<module_name>.<output_name>`

## Module Design Best Practices

- Keep modules focused on a clear purpose.
- Define explicit variable types.
- Provide sensible defaults where appropriate.
- Document expected inputs/outputs.
- Avoid embedding environment-specific values directly.

## Quick Summary

1. Modules are Terraform's primary reuse mechanism.
2. Inputs/outputs create clean module interfaces.
3. Well-designed modules improve consistency, speed, and maintainability.
