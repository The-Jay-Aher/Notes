# Terraform

## Quick Summary

Terraform is an Infrastructure as Code tool used to define, preview, create, modify, and destroy infrastructure through configuration files. This folder contains short course notes plus a longer reference note.

## Learning Order

| Order | Note | Focus |
| --- | --- | --- |
| 1 | [Understanding Infrastructure as Code](1%20-%20Understanding%20Infrastructure%20as%20Code.md) | IaC concepts, benefits, declarative vs imperative thinking. |
| 2 | [IaC with Terraform](2%20-%20IaC%20with%20Terraform.md) | Terraform workflow: init, plan, apply, destroy. |
| 3 | [Terraform Fundamentals](3%20-%20Terraform%20Fundamentals.md) | Variables, types, tfvars, sensitive values, outputs, provisioners. |
| 4 | [Terraform State](4%20-%20Terraform%20State.md) | State purpose, local/remote state, locking, commands, safety. |
| 5 | [Terraform Modules](5%20-%20Terraform%20Modules.md) | Module structure, sources, inputs, outputs, design practices. |
| 6 | [Built-In Functions and Dynamic Blocks](6%20-%20Built-In%20Functions%20and%20Dynamic%20Blocks.md) | Expressions, functions, type constraints, dynamic nested blocks. |
| 7 | [Terraform CLI](7%20-%20Terraform%20CLI.md) | Formatting, validation, import, replace, workspaces, debugging. |
| 8 | [Terraform Cloud and Enterprise](8%20-%20Terraform%20Cloud%20and%20Enterprise.md) | HCP Terraform, Terraform Enterprise, workspaces, remote runs, policy, registry. |
| 9 | [Terraform Deep Notes](Terraform.md) | Long-form Terraform reference. |

## Core Workflow

```text
write configuration -> terraform init -> terraform plan -> review -> terraform apply -> manage state
```

## Official References

- Terraform documentation: <https://developer.hashicorp.com/terraform/docs>
- Terraform CLI: <https://developer.hashicorp.com/terraform/cli>
- Terraform language: <https://developer.hashicorp.com/terraform/language>
- Terraform state: <https://developer.hashicorp.com/terraform/language/state>
- Terraform modules: <https://developer.hashicorp.com/terraform/language/modules>
- HCP Terraform and Terraform Enterprise workspaces: <https://developer.hashicorp.com/terraform/enterprise/workspaces>

