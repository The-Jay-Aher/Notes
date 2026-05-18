# 7 - Terraform CLI

## Quick Summary

Terraform CLI is the command-line interface for formatting, validating, planning, applying, importing, inspecting, debugging, and managing state. You should know the daily workflow commands and the dangerous commands that require extra care.

## Daily Commands

```bash
terraform init
terraform fmt -recursive
terraform validate
terraform plan
terraform apply
```

Common safe CI validation:

```bash
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
```

## init

```bash
terraform init
```

Use when:

- New working directory.
- Provider changes.
- Module source changes.
- Backend changes.

Useful flags:

```bash
terraform init -upgrade
terraform init -reconfigure
terraform init -backend=false
```

## plan

```bash
terraform plan
terraform plan -out=tfplan
```

Use saved plan:

```bash
terraform apply tfplan
```

## apply

```bash
terraform apply
```

Controlled automation:

```bash
terraform apply -auto-approve
```

Only use auto-approve when review and gating happen elsewhere.

## destroy

```bash
terraform plan -destroy
terraform destroy
```

Never treat destroy as a routine cleanup command in shared environments.

## Importing Existing Infrastructure

Import attaches an existing resource to Terraform state.

```bash
terraform import aws_s3_bucket.logs existing-bucket-name
```

After import:

1. Write matching resource configuration.
2. Run plan.
3. Adjust config until changes are expected.

Some newer Terraform workflows also support import blocks. Check current docs for the version you use.

## Replacing Resources

Preferred modern pattern:

```bash
terraform apply -replace=aws_instance.web
```

This tells Terraform to replace a specific resource during apply.

Avoid older `terraform taint` patterns unless you specifically need them and understand the effect.

## Terraform Configuration Block

```hcl
terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

Use constraints to avoid accidental incompatible upgrades.

## Workspaces

CLI workspaces allow multiple state instances for one configuration/backend.

```bash
terraform workspace list
terraform workspace new dev
terraform workspace select prod
```

Important: Terraform CLI workspaces are different from HCP Terraform workspaces.

Use CLI workspaces carefully. For many production systems, separate directories/root modules per environment are clearer.

## Debugging

Set log level:

```bash
TF_LOG=INFO terraform plan
TF_LOG=DEBUG terraform plan
TF_LOG=TRACE terraform plan
```

Write logs to a file:

```bash
TF_LOG=DEBUG TF_LOG_PATH=terraform.log terraform plan
```

Do not publish debug logs without checking for sensitive data.

## Useful Inspection Commands

```bash
terraform providers
terraform output
terraform output -json
terraform state list
terraform state show <address>
terraform console
```

`terraform console` is useful for testing expressions.

## Benefits

- Clear lifecycle workflow.
- Supports validation and formatting.
- Provides state inspection tools.
- Supports import and replacement.
- Works in local and CI/CD environments.

## Drawbacks / Limitations

- CLI commands can be destructive.
- Workspace misuse can target wrong environment.
- Debug logs may contain sensitive information.
- Saved plans can go stale.
- Local execution depends on local credentials and environment.

## Hidden Details / Caveats

- `terraform validate` does not contact all remote APIs.
- `terraform plan` may refresh state unless configured otherwise.
- Saved plan files can contain sensitive data.
- `terraform force-unlock` should only be used after confirming no active run.
- Provider lock file affects selected provider versions.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Applying without checking workspace | Run `terraform workspace show` or use separate env directories. |
| Ignoring replacements in plan | Review `-/+` carefully. |
| Running debug logs in shared output | Save locally and redact. |
| Importing without writing config | Write matching resource config. |
| Overusing CLI workspaces for all envs | Consider separate root modules. |

## Interview Notes

- `fmt` formats; `validate` checks syntax/config shape.
- `init` downloads providers/modules and initializes backend.
- `plan` previews; `apply` changes.
- `import` attaches existing resources to state.
- `-replace` forces resource replacement.
- CLI workspaces are not the same as HCP Terraform workspaces.

## Related Topics

- [Terraform State](4%20-%20Terraform%20State.md)
- [Terraform Cloud and Enterprise](8%20-%20Terraform%20Cloud%20and%20Enterprise.md)

