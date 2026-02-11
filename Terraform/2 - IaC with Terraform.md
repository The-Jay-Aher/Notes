# 2 - IaC with Terraform

## Terraform Workflow

Terraform's core workflow is iterative:

1. **Write**
   - Define resources in `.tf` files.
2. **Init**
   - Initialize working directory and dependencies.
3. **Plan**
   - Preview proposed changes.
4. **Apply**
   - Create/update infrastructure.
5. **Review and Repeat**
   - Update code as requirements evolve.

## `terraform init`

Initializes a working directory.

What it does:

- Downloads required providers/modules.
- Configures backend (if declared).
- Prepares local metadata for execution.

Run `init` when:

- Starting a new project
- Pulling new code
- Changing provider/backend/module definitions

## `terraform plan`

Generates an execution plan without changing infrastructure.

Why it matters:

- Shows create/update/destroy actions.
- Helps catch mistakes before apply.
- Supports review in team workflows.

## `terraform apply`

Executes the approved plan and updates state.

Best practice:

- Review plan output carefully.
- Use non-production testing before production changes.

## `terraform destroy`

Destroys resources managed by current configuration/state.

Use carefully:

- Destructive and often irreversible.
- Validate scope and environment before running.

## Terraform Building Blocks (High Level)

- `terraform` block
- `provider` blocks
- `resource` blocks
- `data` blocks
- `variable` blocks
- `output` blocks
- `module` blocks

## Quick Summary

1. Terraform workflow centers on `init`, `plan`, and `apply`.
2. `plan` is your primary safety checkpoint.
3. Reliable IaC depends on repeatable workflow + version control.
