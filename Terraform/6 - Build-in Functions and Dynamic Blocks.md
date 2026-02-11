# 6 - Built-In Functions and Dynamic Blocks

## Terraform Built-In Functions

Terraform includes many built-in functions for transforming values.

General form:

- `function_name(arg1, arg2, ...)`

Common examples:

- `file(path)` - read file contents
- `max(a, b, ...)` - maximum numeric value
- `flatten(list)` - flatten nested lists
- `lookup(map, key, default)` - safe map lookup
- `merge(map1, map2, ...)` - combine maps

Notes:

- User-defined functions are not supported in Terraform language.
- Prefer clear expressions over overly complex one-liners.

## Type Constraints Overview

Terraform type constraints improve correctness and readability.

Primitive:

- `string`
- `number`
- `bool`

Collection types:

- `list(type)`
- `set(type)`
- `map(type)`

Structural types:

- `object({...})`
- `tuple([...])`

Dynamic placeholder:

- `any` (use sparingly)

## Dynamic Blocks

Dynamic blocks generate repeatable nested blocks inside resources/data/providers/provisioners.

Why use them:

- Reduce repetition in nested configurations.
- Build cleaner reusable module interfaces for variable-length nested inputs.

How they work:

- Iterate over a collection.
- Emit one nested block per element.

## Dynamic Block Best Practices

- Use only when repeated nested blocks are truly needed.
- Avoid overuse; dynamic blocks can hurt readability.
- Favor explicit configuration when repetition is small and static.

## Quick Summary

1. Built-in functions help transform and compose data.
2. Strong type constraints make modules safer.
3. Dynamic blocks are useful, but readability should remain a priority.
