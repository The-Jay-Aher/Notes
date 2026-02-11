# 4 - Terraform State

## What Terraform State Is

Terraform state maps real infrastructure objects to configuration.

Default local state file:

- `terraform.tfstate`

Why state matters:

- Tracks resource identities
- Enables diff/plan calculations
- Stores dependency metadata and outputs

## Local vs Remote State

### Local State

- Stored on local filesystem.
- Simple for learning/single-user workflows.

### Remote State

- Stored in shared backend (for example S3, Terraform Cloud, Azure Blob, GCS).
- Better for team workflows.
- Supports centralized access controls and recovery practices.

## State Locking

Locking prevents concurrent updates to the same state.

Benefits:

- Avoids race conditions
- Reduces risk of corruption

## Common State Commands

- `terraform state list` - list tracked resources
- `terraform state show <address>` - show details for one resource
- `terraform state rm <address>` - remove resource from state without destroying real infrastructure
- `terraform state mv <src> <dst>` - move/rename resource addresses in state

Use state manipulation commands carefully and preferably with backups.

## Best Practices

- Use remote backend for team projects.
- Enable locking where supported.
- Protect state because it may contain sensitive values.
- Back up state and control access.
- Avoid manual file edits unless absolutely necessary.

## Quick Summary

1. State is core to Terraform correctness.
2. Remote state + locking is the common production pattern.
3. Manual state operations are powerful and risky; use intentionally.
