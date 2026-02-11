# 7 - Terraform CLI

## Code Quality and Validation Commands

### `terraform fmt`

- Formats Terraform code for consistency.
- Safe to run anytime.

### `terraform validate`

- Validates syntax and internal configuration consistency.
- Useful before `plan` in CI pipelines.

## Importing Existing Infrastructure

### `terraform import`

Maps an existing infrastructure object to a Terraform resource address.

Pattern:

- `terraform import <resource_address> <provider_id>`

Important:

- Import does not generate full configuration automatically.
- After import, configuration must match the real resource to avoid drift.

## Replacing Resources

### Recommended: `terraform apply -replace=<address>`

Use `-replace` to force recreation of a resource in a controlled plan/apply flow.

Note:

- Older `terraform taint` workflows are largely superseded by `-replace` in modern Terraform usage.

## Terraform Configuration Block

The `terraform` block controls Terraform behavior.

Common uses:

- Required Terraform version
- Required provider constraints
- Backend configuration
- Experimental feature flags (when applicable)

## Workspaces (CLI)

CLI workspaces let you keep multiple state snapshots for same configuration directory.

Key points:

- Default workspace is `default`.
- Useful for isolated environment variants, but not a full replacement for strong environment separation strategies.

Reference variable:

- `terraform.workspace`

## Debugging Terraform

### `TF_LOG`

Environment variable to enable verbose logging.

Common levels:

- `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`

### `TF_LOG_PATH`

- Writes logs to a file for troubleshooting.

Linux example:

```bash
export TF_LOG=TRACE
export TF_LOG_PATH=./terraform.log
```

## Quick Summary

1. `fmt` and `validate` improve quality before execution.
2. `import` helps adopt unmanaged existing infrastructure.
3. Prefer `-replace` over legacy taint workflows.
4. Logging environment variables help diagnose hard failures.
