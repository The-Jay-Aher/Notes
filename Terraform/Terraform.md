# Terraform Notes (Basic → Advanced)

These are personal learning notes for Terraform (HCL), ordered from fundamentals → advanced workflows. Examples use AWS, but the concepts apply to any provider.

## Table of Contents
- [0. Quick CLI Cheatsheet](#0-quick-cli-cheatsheet)
- [1. Terraform Fundamentals](#1-terraform-fundamentals)
- [2. Core Workflow & Common Commands](#2-core-workflow--common-commands)
- [3. Project Layout & Load Semantics](#3-project-layout--load-semantics)
- [4. Terraform Settings (`terraform` block)](#4-terraform-settings-terraform-block)
- [5. Variables (Inputs) and Values](#5-variables-inputs-and-values)
- [6. Types, Expressions, and Functions](#6-types-expressions-and-functions)
- [7. Locals and Outputs](#7-locals-and-outputs)
- [8. Data Sources](#8-data-sources)
- [9. Resources, Dependencies, and Meta-Arguments](#9-resources-dependencies-and-meta-arguments)
- [10. Dynamic Blocks](#10-dynamic-blocks)
- [11. Modules](#11-modules)
- [12. State & Collaboration (Remote Backends)](#12-state--collaboration-remote-backends)
- [13. Workspaces](#13-workspaces)
- [14. Import, Refactors, and Break-Glass Operations](#14-import-refactors-and-break-glass-operations)
- [15. Provisioners (Last Resort)](#15-provisioners-last-resort)
- [16. Security Notes](#16-security-notes)
- [17. Terraform Cloud & Enterprise](#17-terraform-cloud--enterprise)

## 0. Quick CLI Cheatsheet

```bash
terraform version
terraform init
terraform fmt -recursive
terraform validate
terraform plan
terraform apply
terraform destroy
```

Useful “day to day” commands:

- Save a plan to a file (binary): `terraform plan -out=tfplan`
- Apply exactly that plan: `terraform apply tfplan`
- Inspect a plan/state: `terraform show tfplan` or `terraform show`
- Query outputs: `terraform output` (or `terraform output <name>`)
- Test expressions/functions: `terraform console`

## 1. Terraform Fundamentals

### Mental model

- Terraform is *declarative*: you declare the desired end state.
- Providers translate Terraform resources into API calls (AWS, Azure, Kubernetes, etc.).
- Terraform uses a state file to remember what it created and how it maps to real infrastructure objects.

### Key terms

- **Configuration**: the `.tf` files in a directory (written in HCL).
- **Module**: a directory of `.tf` files. Your working directory is the **root module**.
- **Resource**: a `resource` block (creates/manages something).
- **Data source**: a `data` block (reads something that already exists).
- **Plan**: a preview of changes.
- **Apply**: executes the plan (creates/updates/destroys).
- **State**: Terraform’s record of managed objects and attributes (treat it as sensitive).

## 2. Core Workflow & Common Commands

### Init → Plan → Apply

- `terraform init`
  - Downloads provider plugins and modules.
  - Initializes the backend (where state is stored).
- `terraform plan`
  - Shows what Terraform *would* do.
  - Great for review/approval gates.
- `terraform apply`
  - Performs the changes.
  - Use `terraform apply tfplan` to apply a previously saved plan.

### Apply from a plan file (approval-friendly)

Saving a plan file is useful when you want a review/approval step and then apply *exactly* what was reviewed.

```bash
# Create a binary plan file
terraform plan -out=ec2.plan

# Apply exactly that plan
terraform apply ec2.plan

# Read the binary plan in human-friendly form
terraform show ec2.plan
```

### Formatting and validation

- `terraform fmt` / `terraform fmt -recursive`
  - Formats HCL consistently (run this before committing).
- `terraform validate`
  - Syntactic + basic semantic validation (undeclared variables, unsupported arguments, etc.).

### CI-friendly usage (optional)

- `terraform fmt -check -recursive`
  - Fails if formatting changes would be made (useful in CI).
- `terraform plan -detailed-exitcode`
  - Exit codes: `0` = no changes, `2` = changes present, `1` = error.
- `terraform show -json tfplan`
  - Converts a plan file into JSON (useful for tooling/automation).

### Inspecting and debugging

- `terraform show`
  - Shows current state (or a plan file if you pass one).
  - Plan files are binary; use `terraform show tfplan` to read them.
- `terraform output`
  - Prints output values from state.
- `terraform graph`
  - Emits a dependency graph (DOT format). Example usage:

    ```bash
    terraform graph | dot -Tsvg > graph.svg
    ```

- Debug logs (use sparingly; can be noisy):
  - `TF_LOG=TRACE|DEBUG|INFO|WARN|ERROR`
  - `TF_LOG_PATH=./terraform.log`

## 3. Project Layout & Load Semantics

### Typical file layout (convention)

Terraform doesn’t require specific filenames, but this split keeps projects readable:

- `versions.tf` — `terraform { required_version / required_providers }`
- `providers.tf` — provider configuration(s)
- `main.tf` — resources + data sources
- `variables.tf` — input variables
- `locals.tf` — locals
- `outputs.tf` — outputs

### Load order and merging

- Terraform loads all `.tf` and `.tf.json` files in the working directory.
- Files are read in alphabetical order, but the resulting configuration is merged; don’t rely on filename ordering to “control” behavior.

### Comments in HCL

- `#` or `//` for single-line comments
- `/* ... */` for multi-line comments

## 4. Terraform Settings (`terraform` block)

Use the `terraform` block to pin versions and configure providers/backends.

```hcl
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

Notes:

- `required_version` helps teams avoid “works on my machine” drift.
- `required_providers` pins provider major versions and selects the provider source.
- `terraform init` creates/updates `.terraform.lock.hcl` (provider dependency lock file).
- If you need to update provider selections, use `terraform init -upgrade` (this can change `.terraform.lock.hcl`).
- The dependency lock file tracks **provider** selections only (not remote module versions).
  - Pin remote modules explicitly via `version = "..."` (registry) or `?ref=...` (VCS sources).

## 5. Variables (Inputs) and Values

### Defining variables

```hcl
variable "environment" {
  description = "Deployment environment (e.g., dev/stage/prod)"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"

  validation {
    condition     = can(regex("^t(2|3)\\.", var.instance_type))
    error_message = "instance_type must be a t2.* or t3.* instance type."
  }
}
```

### Assigning variable values

Common ways to set input values:

- Defaults inside `variable` blocks (lowest priority).
- `terraform.tfvars` / `terraform.tfvars.json` (auto-loaded if present).
- `*.auto.tfvars` / `*.auto.tfvars.json` (auto-loaded in lexical order).
- CLI flags (highest priority):
  - `-var="name=value"`
  - `-var-file="prod.tfvars"`
- Environment variables: `TF_VAR_<name>`

Examples:

```bash
# Pass a single value
terraform plan -var="instance_type=t3.small"

# Use a named tfvars file (not auto-loaded)
terraform plan -var-file="prod.tfvars"

# Environment variable form
export TF_VAR_environment=dev
terraform plan
```

### Variable precedence (high → low)

Terraform resolves values using the *highest* source that provides a value:

1. CLI flags: `-var`, `-var-file`
2. `*.auto.tfvars`, `*.auto.tfvars.json` (in filename order)
3. `terraform.tfvars`, `terraform.tfvars.json`
4. Environment variables: `TF_VAR_*`
5. `default` values in `variable` blocks

### Sensitive values

- Marking a variable or output as `sensitive = true` hides it from normal CLI output.
- Sensitive values are **still stored in state** (state must be protected).

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

## 6. Types, Expressions, and Functions

### Terraform types (quick reference)

- Primitive:
  - `string`, `number`, `bool`
- Collection:
  - `list(T)` (ordered, allows duplicates)
  - `set(T)` (unordered, unique values)
  - `map(T)` (key/value map, keys are strings)
- Structural:
  - `object({ name = string, port = number })`
  - `tuple([string, number, bool])`
- Special:
  - `any` (avoid unless you truly need it)
  - `null` (represents “unset” / “unknown here”)

Examples:

```hcl
variable "tags" {
  type    = map(string)
  default = { Owner = "jay", ManagedBy = "terraform" }
}

variable "iam_usernames" {
  type    = list(string)
  default = ["user-01", "user-02", "user-03"]
}
```

### Conditional expressions

Syntax:

```hcl
condition ? true_val : false_val
```

Important:

- `condition` must be a boolean expression (strings like `""` are not truthy/falsey in Terraform).

Example:

```hcl
instance_type = var.environment == "production" ? "t3.medium" : "t3.micro"
```

Example (multiple conditions):

```hcl
instance_type = (
  var.environment == "production" && var.region == "us-east-1"
  ? "t3.medium"
  : "t3.micro"
)
```

### For expressions (list/map comprehensions)

Use `for` expressions to transform collections into new lists or maps.

```hcl
locals {
  # List comprehension
  upper_usernames = [for u in var.iam_usernames : upper(u)]

  # Map comprehension (key => value)
  username_to_upper = { for u in var.iam_usernames : u => upper(u) }
}
```

### Splat expressions

Splat expressions help you collect an attribute from many instances into a list.

```hcl
# With count-based resources
instance_ids = aws_instance.web[*].id

# With for_each-based resources (values(...) turns the map into a list)
user_arns = values(aws_iam_user.this)[*].arn
```

### Helpful “defaults” and safe access functions

- `coalesce(a, b, ...)` — first non-null, non-empty-string (common for defaults).
- `lookup(map, key, default)` — safe map access.
- `try(a, b, ...)` — first expression that doesn’t error.
- `can(expr)` — returns true/false based on whether `expr` would succeed.

### Functions + Terraform Console

Use `terraform console` to experiment with expressions and functions interactively:

```bash
terraform console
```

Common function categories (not exhaustive):

| Category | Examples |
| --- | --- |
| Numeric | `abs`, `ceil`, `floor`, `max`, `min` |
| String | `replace`, `split`, `tolower`, `toupper`, `trimspace` |
| Collection | `concat`, `distinct`, `element`, `keys`, `length`, `merge`, `sort`, `toset` |
| Filesystem | `file`, `filebase64`, `dirname`, `pathexpand` |

Notes:

- `file()` is useful for large templates/certificates/user-data to keep HCL readable.
- `zipmap(keys, values)` is handy when you have parallel lists you want as a map.

Example (`zipmap`):

```hcl
locals {
  usernames = ["user-01", "user-02"]
  arns      = ["arn:...:user-01", "arn:...:user-02"]
  user_map  = zipmap(local.usernames, local.arns)
}
```

## 7. Locals and Outputs

### Local values

Locals are computed values you define once and reuse (great for avoiding repeated expressions).

```hcl
locals {
  name_prefix = "${var.environment}-app"
}

resource "aws_s3_bucket" "logs" {
  bucket = "${local.name_prefix}-logs"
}
```

Locals vs variables:

- Variables are inputs; values come from tfvars/CLI/env.
- Locals are internal; you change them by changing the code.
- Locals are defined in a `locals {}` block (plural) and referenced via `local.<name>` (singular).

### Output values

Outputs expose values from state on the CLI and to other tooling.

```hcl
output "bucket_name" {
  value = aws_s3_bucket.logs.bucket
}
```

Module output access:

- `module.<module_name>.<output_name>`

Sensitive outputs:

```hcl
output "db_password" {
  value     = var.db_password
  sensitive = true
}
```

## 8. Data Sources

Data sources read information from outside Terraform (existing infrastructure, provider lookups, etc.).

```hcl
data "aws_caller_identity" "current" {}
```

Tips:

- `${path.module}` is the filesystem path of the current module.
- Useful path values include `path.module`, `path.root`, and `path.cwd`.
- A data source is declared with a `data` block and exported under a local name (example above exports `data.aws_caller_identity.current`).
- Many data sources support filters (query constraints) inside the block body. Example filter structure:

  ```hcl
  data "aws_ami" "al2023" {
    most_recent = true

    filter {
      name   = "name"
      values = ["al2023-ami-*-x86_64"]
    }
  }
  ```

## 9. Resources, Dependencies, and Meta-Arguments

### How Terraform applies a configuration

- Create resources that are in configuration but not in state.
- Destroy resources that are in state but no longer in configuration.
- Update in-place when possible.
- Replace (destroy + recreate) when the provider API can’t update a field in-place.

### Common meta-arguments

| Meta-argument | Purpose |
| --- | --- |
| `depends_on` | Force ordering when Terraform can’t infer a dependency |
| `count` | Create N copies of a resource |
| `for_each` | Create one resource per item in a set/map |
| `lifecycle` | Customize create/update/destroy behavior |
| `provider` | Select a specific provider configuration (aliases, regions) |

### `depends_on`

Use when you have a “hidden dependency” (e.g., a resource depends on a module output, but not via a direct reference).

```hcl
resource "aws_instance" "web" {
  ami           = "ami-1234567890abcdef0"
  instance_type = var.instance_type

  depends_on = [aws_security_group.allow_ssh]
}
```

### `count` + `count.index`

Use `count` when instances are close to identical and stable ordering is acceptable.

```hcl
resource "aws_instance" "web" {
  count         = 3
  ami           = "ami-1234567890abcdef0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-${count.index}"
  }
}
```

Pitfalls with `count`:

- Index-based identity means insertions/removals can cause “resource address shifting”.
- Prefer `for_each` when you care about stable identity by key.

### `for_each` + `each.key` / `each.value`

Use `for_each` with a set of strings or a map.

```hcl
resource "aws_iam_user" "this" {
  for_each = toset(["user-01", "user-02", "user-03"])
  name     = each.key
}
```

The `each` object:

| Attribute | Meaning |
| --- | --- |
| `each.key` | The set element (or map key) for this instance |
| `each.value` | The map value for this instance (for sets, `each.value == each.key`) |

Why `for_each` is often safer than `count`:

- Adding/removing an item in a set/map usually doesn’t force unrelated instances to “shift addresses”.
- Identity is tied to a stable key (`each.key`) rather than a numeric index.

### `lifecycle`

Lifecycle lets you customize resource behavior when Terraform would otherwise replace/destroy/update.

| Argument | Use case |
| --- | --- |
| `create_before_destroy` | Avoid downtime by creating replacement first |
| `prevent_destroy` | Safety guard against accidental deletes |
| `ignore_changes` | Ignore drift for specific attributes |
| `replace_triggered_by` | Force replacement when related objects change |

Examples:

```hcl
resource "aws_security_group" "example" {
  name = "example"

  lifecycle {
    prevent_destroy = true
  }
}
```

```hcl
resource "aws_instance" "example" {
  ami           = "ami-1234567890abcdef0"
  instance_type = "t3.micro"

  lifecycle {
    ignore_changes = [tags["LastPatchedAt"]]
  }
}
```

### Multiple provider configurations (aliases)

Use provider aliases when you need multiple regions/accounts in the same configuration.

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

resource "aws_s3_bucket" "east" {
  bucket = "my-east-bucket"
}

resource "aws_s3_bucket" "west" {
  provider = aws.west
  bucket   = "my-west-bucket"
}
```

## 10. Dynamic Blocks

Dynamic blocks generate repeatable nested blocks (supported in `resource`, `data`, `provider`, and `provisioner` blocks).

```hcl
resource "aws_security_group" "web" {
  name = "web"

  dynamic "ingress" {
    for_each = var.ingress_rules
    iterator = rule

    content {
      from_port   = rule.value.from_port
      to_port     = rule.value.to_port
      protocol    = rule.value.protocol
      cidr_blocks = rule.value.cidr_blocks
    }
  }
}
```

Notes:

- `iterator` is optional. If omitted, the iterator name defaults to the block label (e.g., `ingress`).

## 11. Modules

### Why modules

Modules help you:

- Reduce repetition (DRY).
- Standardize infrastructure patterns across teams.
- Version and review infrastructure building blocks.

### Using a registry module

```hcl
module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "~> 5.0"
}
```

### Points to note (common gotchas)

- Not every module works with “copy/paste and apply”: many require mandatory inputs before they can create resources.
- Some repos contain multiple modules (submodules). In that case, you must reference the correct subdirectory/module source.

### Module sources

Common module source locations:

1. Terraform Registry
2. Local paths (`./modules/vpc`)
3. Git repositories (`git::...`)
4. HTTP URLs
5. S3 buckets (or other artifact stores)

Example: Git source

```hcl
module "vpc" {
  source = "git::https://example.com/network/vpc.git?ref=v1.2.0"
}
```

### Variables and outputs in modules

- Modules should expose customization via variables (avoid hardcoding region/instance types).
- Consumers use module outputs to connect dependencies:
  - `module.<name>.<output>`

### Improving custom modules (maintainability)

Common improvements when you move from a “quick module” to something reusable:

- Replace hardcoded values with variables (and good defaults/validation).
- Avoid hardcoding regions/accounts in module code; let the root module configure providers.
- Include a `required_providers` block (and version constraints) so module behavior is predictable.

### Root module vs child module

- **Root module**: the directory where you run `terraform` commands.
- **Child module**: a module called by another module.

### Standard module structure (recommended)

Minimal:

- `main.tf`
- `variables.tf`
- `outputs.tf`
- `README.md`

Common “complete” extras:

- `versions.tf`
- `LICENSE`
- `examples/`
- `modules/` (submodules)

### Publishing modules (Terraform Registry)

For the public registry, a module repo typically needs:

- A repo name like `terraform-<PROVIDER>-<NAME>` (example: `terraform-aws-vpc`)
- Semantic version tags (often `v1.2.3`)
- A `README.md` with clear inputs/outputs and usage examples
- A standard module structure (`main.tf`, `variables.tf`, `outputs.tf`, etc.)

### Creating a base module structure (internal)

Many orgs keep an internal “module library” and separate “consumer” projects. One practical layout:

```text
modules/
  ec2-instance/
    main.tf
    variables.tf
    outputs.tf
teams/
  payments/
    main.tf
  security/
    main.tf
```

- `modules/` contains reusable building blocks.
- `teams/` (or `envs/`) contains root modules that call those building blocks.

### Choosing a safe module (practical checklist)

- Prefer well-maintained modules with healthy release history.
- Review documentation: inputs/outputs, examples, and upgrade notes.
- Review code for suspicious behavior (shell calls, external lookups, unexpected providers).
- Prefer modules maintained by organizations/partners over single-use personal repos.

## 12. State & Collaboration (Remote Backends)

### What state is (and why it matters)

- State is the mapping between Terraform resource addresses and real objects (plus attributes).
- Treat state as sensitive: it can include resource IDs, IPs, and sometimes secrets.

### What to commit vs ignore (typical Terraform project)

Recommended `.gitignore` entries:

```gitignore
.terraform/
*.tfstate
*.tfstate.*
crash.log
terraform.tfvars
.terraform.tfstate.lock.info
```

Notes:

- Commit `.terraform.lock.hcl` (it is a dependency lock file for providers).
- Avoid committing `terraform.tfvars` if it contains secrets; prefer `terraform.tfvars.example`.

### Backends

Backends determine where Terraform stores state.

- Default is `local` (state file on disk).
- Common remote backends:
  - S3
  - Consul
  - AzureRM
  - Kubernetes
  - HTTP
  - etcd

### State locking

- Locking prevents multiple writers from corrupting state.
- Not all backends support locking.
- If locking gets stuck, Terraform supports manual unlock:
  - `terraform force-unlock <LOCK_ID>` (use only when you’re sure no one else holds the lock).

### S3 backend + DynamoDB locking (common AWS pattern)

```hcl
terraform {
  backend "s3" {
    bucket         = "my-tfstate-bucket"
    key            = "env/dev/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "my-tfstate-locks"
    encrypt        = true
  }
}
```

### State management subcommands

Terraform state editing should be done via `terraform state ...` rather than manually editing `terraform.tfstate`.

| Subcommand | Purpose |
| --- | --- |
| `list` | List resources tracked in state |
| `show` | Show attributes for one resource |
| `mv` | Move/rename resources in state (avoids recreate) |
| `rm` | Stop managing a resource (does not delete it) |
| `pull` | Download remote state to stdout |
| `push` | Upload a local state to remote (rare; use with care) |

### Remote state data source

Use `terraform_remote_state` when one project needs outputs from another.

```hcl
data "terraform_remote_state" "network" {
  backend = "s3"
  config = {
    bucket = "my-tfstate-bucket"
    key    = "env/dev/network.tfstate"
    region = "us-east-1"
  }
}

resource "aws_security_group_rule" "allow_from_vpc" {
  # Example: read VPC CIDR blocks exported by the network project
  cidr_blocks = data.terraform_remote_state.network.outputs.vpc_cidr_blocks
  # ...
}
```

## 13. Workspaces

Workspaces allow multiple state files for the same configuration directory.

Common commands:

```bash
terraform workspace list
terraform workspace new dev
terraform workspace select dev
terraform workspace show
```

Practical guidance:

- Workspaces are convenient for lightweight separation, but they are not a full environment isolation strategy.
- For production-grade separation, many teams prefer separate directories (or separate backends) per environment.

## 14. Import, Refactors, and Break-Glass Operations

### Importing existing resources

Classic workflow:

1. Write the resource block (even a minimal one).
2. Import the real object into state:

```bash
terraform import aws_s3_bucket.logs my-existing-bucket-name
```

Terraform 1.5+ (configuration-driven import) introduced `import` blocks:

```hcl
import {
  to = aws_s3_bucket.logs
  id = "my-existing-bucket-name"
}
```

If you don’t have a matching resource block yet, you can generate starter config during planning:

```bash
terraform plan -generate-config-out=generated_import.tf
```

### Replacing resources (taint vs `-replace`)

- `terraform taint` is deprecated.
- Preferred approach: force replacement during apply:

```bash
terraform apply -replace=aws_instance.web
```

### Targeting and refresh flags (use carefully)

These are “break-glass” flags and can produce partial, confusing states if overused:

- `-target=...` applies changes only for a subset of resources.
- `-refresh=false` skips state refresh during planning.
- `-refresh-only` (safer alternative) updates state to match real infrastructure and shows drift without proposing config-driven changes:

  ```bash
  terraform plan -refresh-only
  terraform apply -refresh-only
  ```

Better long-term fixes for “large infra pain”:

- Split very large configurations into smaller root modules.
- Prefer module boundaries that can be planned/applied independently.

Notes for large infrastructures:

- You can hit provider API rate limits in large plans/applies. Limiting concurrency can help:

  ```bash
  terraform plan -parallelism=10
  terraform apply -parallelism=10
  ```

- Plan symbols to recognize quickly:
  - `+` create
  - `~` update in-place
  - `-` destroy
  - `-/+` replace (destroy and then create)

### Refactoring resource addresses safely (`moved` blocks)

Instead of `terraform state mv`, you can declare refactors in code:

```hcl
moved {
  from = aws_instance.web
  to   = aws_instance.app
}
```

## 15. Provisioners (Last Resort)

Provisioners run scripts on local or remote machines during create/destroy.

Types:

1. `local-exec` (run on the machine where Terraform is running)
2. `remote-exec` (run on the remote resource, via SSH/WinRM)
3. `file` (copy a file to the remote resource)

Provisioners are generally discouraged because:

- They can be brittle and hard to retry safely.
- Failures can leave resources “half configured”.

Preferred alternatives:

- Cloud-init / `user_data`
- AMI/image baking (Packer)
- Configuration management (Ansible, Chef, etc.)

Provisioner timing:

- Creation-time provisioners run only during create (not update).
- Destroy-time provisioners run before the resource is destroyed (set `when = destroy`).

Provisioners are defined *inside* a resource block, and a resource can have multiple provisioners. Example shape:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-1234567890abcdef0"
  instance_type = "t3.micro"

  connection {
    type        = "ssh"
    user        = "ec2-user"
    host        = self.public_ip
    private_key = file(var.ssh_private_key_path)
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum install -y httpd",
      "sudo systemctl enable --now httpd",
    ]
  }

  provisioner "local-exec" {
    command = "echo ${self.public_ip} > server_ip.txt"
  }
}
```

Failure behavior:

| `on_failure` | Meaning |
| --- | --- |
| `fail` | Stop apply (default). Creation-time failures taint/replace the resource. |
| `continue` | Ignore the error and continue |

## 16. Security Notes

- Never commit secrets (AWS keys, database passwords, private tokens) into `.tf` or `.tfvars`.
- “Sensitive” values are hidden in CLI output but still stored in state; protect state storage.
- Vault integration is powerful, but secrets read/written via Terraform can end up persisted in state.
- Use version constraints (`required_version`, provider version pins) and commit `.terraform.lock.hcl`.
- Treat module selection as a supply-chain decision: prefer reputable sources, pin versions, and review code.

Provider note:

- Mature providers (like AWS) often mark certain attributes (e.g., database passwords) as sensitive automatically, but that still does **not** remove them from state.

## 17. Terraform Cloud & Enterprise

### Terraform Cloud (TFC) overview

Terraform Cloud provides:

- Centralized state and collaboration features
- Remote runs (consistent execution environment)
- Private module registry
- Access controls and auditability

### Remote backend (TFC)

- The remote backend stores Terraform state in Terraform Cloud.
- You can use it in two main modes:
  - **Local operations + remote state**: you run `terraform plan/apply` locally, but state is stored remotely.
  - **Full remote operations**: Terraform Cloud runs `plan/apply` in its run environment and streams logs back to you.

### Sentinel (policy as code)

Sentinel is HashiCorp’s policy-as-code framework (typically a paid/enterprise feature).

Typical pipeline:

1. `terraform plan`
2. Sentinel policy checks
3. `terraform apply` (only if policies pass)

### Air-gapped environments

An air-gapped environment is physically isolated from the public internet.

- Terraform Enterprise supports online and air-gapped installation methods.
- Air-gapped setups are common in high-security environments (government, finance, critical infrastructure).
