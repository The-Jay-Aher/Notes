# 10 - Python Cheatsheet

## Mental Model

```text
names bind to objects
assignment does not copy
mutation changes objects
scopes resolve names through LEGB
functions are objects
imports execute top-level code once and cache modules
type hints help tools but do not enforce by default
```

## Core Types

| Need | Use |
| --- | --- |
| Ordered mutable data | `list` |
| Fixed grouping | `tuple` |
| Key-value lookup | `dict` |
| Unique membership | `set` |
| Text | `str` |
| Lazy sequence | generator / iterator |

## Common Commands

```bash
python --version
python -m venv .venv
source .venv/bin/activate
python -m pip install <package>
python -m pip list
python -m json.tool file.json
python script.py
```

## Common Patterns

```python
if value is None:
    ...

with open(path, encoding="utf-8") as f:
    for line in f:
        ...

def main() -> int:
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

## Traps

| Trap | Fix |
| --- | --- |
| Mutable default argument | Use `None` sentinel. |
| `[[0] * cols] * rows` | Use list comprehension. |
| `is` for equality | Use `==` except identity checks like `None`. |
| Exhausted generator | Recreate it or materialize intentionally. |
| Broad `except Exception` | Catch specific exceptions. |
| Blocking async event loop | Use async library or executor. |
| Shell string in subprocess | Use argument list. |
| Import-time side effects | Move work into `main` or functions. |

## Interview Lines

- Python variables are names bound to objects.
- Passing arguments binds local parameter names to the same objects.
- Mutating a shared object is visible; rebinding a local name is not.
- `list` is mutable; `tuple` structure is immutable.
- Dict keys must be hashable.
- A generator is lazy and one-shot.
- Decorators transform functions/classes at definition time.
- The GIL affects CPython thread execution but does not remove race conditions.

