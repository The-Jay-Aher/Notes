# 4 - Terraform State

## Quick Summary

Terraform state maps Terraform resource addresses to real infrastructure objects. Without state, Terraform cannot reliably know which real resource corresponds to which configuration block.

State is critical and sensitive. Protect it.

## What State Stores

State can include:

- Resource IDs.
- Resource attributes.
- Dependencies.
- Outputs.
- Provider metadata.
- Sensitive values depending on resource/provider.

Default local state file:

```text
terraform.tfstate
```

## Why State Exists

Terraform uses state to:

- Track managed objects.
- Compare desired config with real infrastructure.
- Plan changes.
- Store dependencies.
- Improve performance by caching attributes.

Mental model:

```text
configuration + state + provider refresh = plan
```

## Local vs Remote State

### Local State

State stored on your machine.

Good for:

- Learning.
- Small solo experiments.

Problems:

- Easy to lose.
- Hard for teams.
- No shared locking.
- Sensitive values stored locally.

### Remote State

State stored in a backend or HCP Terraform.

Good for:

- Teams.
- CI/CD.
- State locking.
- Centralized access control.
- Better backup/versioning depending on backend.

## State Locking

State locking prevents concurrent writes.

Problem without locking:

```text
Engineer A applies changes
Engineer B applies changes at same time
State can become inconsistent
```

Use a backend that supports locking or use HCP Terraform/Terraform Enterprise run coordination.

## Backend Example

Example S3-style backend shape:

```hcl
terraform {
  backend "s3" {
    bucket = "example-terraform-state"
    key    = "network/prod.tfstate"
    region = "ap-south-1"
  }
}
```

Backend details vary. Check the official backend documentation for locking support and required settings.

## Common State Commands

```bash
terraform state list
terraform state show <address>
terraform state mv <source> <destination>
terraform state rm <address>
terraform refresh
terraform import <address> <id>
terraform force-unlock <lock-id>
```

Use state commands carefully. They change Terraform's understanding of infrastructure.

## Import

Import connects an existing real resource to a Terraform resource address.

```bash
terraform import aws_s3_bucket.logs my-existing-bucket
```

After import:

- Write matching configuration.
- Run plan.
- Adjust config until plan is clean or expected.

## Drift

Drift means real infrastructure differs from Terraform configuration/state.

Causes:

- Manual console changes.
- External automation.
- Provider/API default changes.
- Failed partial applies.

Detect:

```bash
terraform plan
```

## Benefits

- Enables accurate planning.
- Tracks real resources.
- Supports dependencies and outputs.
- Remote state improves team workflows.

## Drawbacks / Limitations

- State can contain secrets.
- State corruption or loss is serious.
- Manual state edits are risky.
- Backend migration requires care.
- Drift still needs detection and correction.

## Hidden Details / Caveats

- Do not commit `terraform.tfstate` to Git.
- State locking only works if backend supports it and is configured correctly.
- `force-unlock` can be dangerous if another run is actually active.
- Terraform state is not a general-purpose configuration database.
- `terraform state rm` does not delete real infrastructure; it only forgets it.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Committing state to Git | Use remote backend and `.gitignore`. |
| Sharing local state by copying files | Use remote state. |
| Force-unlocking active runs | Confirm no active apply first. |
| Editing state manually | Use Terraform state commands and backups. |
| Ignoring drift | Run plan regularly. |

## Best Practices

- Use remote state for team projects.
- Enable locking.
- Restrict state access.
- Enable encryption/versioning where backend supports it.
- Back up state.
- Treat state as sensitive.
- Keep state split by lifecycle/ownership to reduce blast radius.

## Interview Notes

- State maps Terraform resources to real infrastructure.
- Local state is default, remote state is better for teams.
- State locking prevents concurrent writes.
- State may contain secrets.
- `state rm` removes from state only, not from cloud.
- Import attaches existing infrastructure to Terraform state.

## Related Topics

- [IaC with Terraform](2%20-%20IaC%20with%20Terraform.md)
- [Terraform CLI](7%20-%20Terraform%20CLI.md)

