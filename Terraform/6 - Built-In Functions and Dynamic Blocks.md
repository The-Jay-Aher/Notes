# 6 - Built-In Functions and Dynamic Blocks

## Quick Summary

Terraform expressions transform input values into the exact configuration resources need. Built-in functions help manipulate strings, lists, maps, files, numbers, and encoded data. Dynamic blocks generate repeated nested blocks when a resource expects blocks instead of simple values.

## Terraform Expressions

Examples:

```hcl
"${var.environment}-${var.name}"
var.enabled ? 1 : 0
for subnet in var.subnets : subnet.cidr
```

Use expressions to keep configuration flexible, but avoid making Terraform code unreadable.

## Common Built-In Functions

| Function | Use |
| --- | --- |
| `length(value)` | Count items or string length. |
| `lookup(map, key, default)` | Read map key with fallback. |
| `merge(map1, map2)` | Combine maps. |
| `concat(list1, list2)` | Combine lists. |
| `flatten(list)` | Flatten nested lists. |
| `contains(list, value)` | Check if list contains value. |
| `toset(list)` | Convert list to set. |
| `file(path)` | Read file content. |
| `templatefile(path, vars)` | Render a template file. |
| `jsonencode(value)` | Convert value to JSON string. |
| `yamldecode(value)` | Parse YAML string. |
| `coalesce(a, b, ...)` | Return first non-null/non-empty string. |

## Example: Tags

```hcl
locals {
  common_tags = {
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_s3_bucket" "logs" {
  bucket = "${var.environment}-app-logs"

  tags = merge(local.common_tags, {
    Name = "${var.environment}-app-logs"
  })
}
```

## Example: templatefile

```hcl
user_data = templatefile("${path.module}/user_data.sh.tftpl", {
  app_name = var.app_name
  port     = var.port
})
```

Template:

```bash
#!/usr/bin/env bash
echo "Starting ${app_name} on port ${port}"
```

## Type Constraints Overview

Primitive:

```hcl
string
number
bool
```

Collection:

```hcl
list(string)
set(string)
map(string)
```

Object:

```hcl
object({
  name = string
  port = number
  tags = map(string)
})
```

## for Expressions

List transformation:

```hcl
[for subnet in var.subnets : subnet.cidr]
```

Map transformation:

```hcl
{ for subnet in var.subnets : subnet.name => subnet.cidr }
```

Filter:

```hcl
[for subnet in var.subnets : subnet if subnet.public]
```

## for_each vs count

| Feature | Best For |
| --- | --- |
| `count` | Simple numbered resources. |
| `for_each` | Stable named resources from map/set. |

Prefer `for_each` when resources have stable keys.

Example:

```hcl
resource "aws_security_group_rule" "ingress" {
  for_each = var.ingress_rules

  type        = "ingress"
  from_port   = each.value.from_port
  to_port     = each.value.to_port
  protocol    = each.value.protocol
  cidr_blocks = each.value.cidr_blocks
}
```

## Dynamic Blocks

Use dynamic blocks when a resource requires repeated nested blocks.

Example:

```hcl
resource "aws_security_group" "app" {
  name = "app"

  dynamic "ingress" {
    for_each = var.ingress_rules

    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }
}
```

Use dynamic blocks only for nested blocks, not normal arguments.

## Dynamic Block Best Practices

- Use only when repeated nested blocks are genuinely needed.
- Keep input object types explicit.
- Avoid deeply nested dynamic blocks unless necessary.
- Prefer readability over cleverness.
- If there are only one or two simple blocks, write them normally.

## Benefits

- Reduces repetition.
- Makes modules configurable.
- Supports structured inputs.
- Helps generate JSON/YAML safely.

## Drawbacks / Limitations

- Complex expressions are hard to read.
- Dynamic blocks can hide final generated configuration.
- Type errors can be confusing.
- Overusing functions makes plans harder to review.

## Hidden Details / Caveats

- Terraform has no user-defined functions in normal language.
- Provider-specific functions may exist and use provider-qualified syntax where supported.
- `for_each` keys affect resource addresses; changing keys can force replacement.
- `count` index changes can cause unwanted churn.
- `jsonencode` is safer than hand-writing JSON strings.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Using `count` for named objects | Prefer `for_each` with stable keys. |
| Building JSON manually | Use `jsonencode`. |
| Dynamic block for simple config | Write normal blocks. |
| No explicit object type | Add clear type constraints. |
| Clever one-liners | Use locals for readability. |

## Interview Notes

- Built-in functions transform values.
- `for_each` is better for stable keyed resources.
- Dynamic blocks generate repeated nested blocks.
- `jsonencode` avoids broken JSON syntax.
- Type constraints catch bad module inputs early.

## Related Topics

- [Terraform Modules](5%20-%20Terraform%20Modules.md)
- [Terraform CLI](7%20-%20Terraform%20CLI.md)

