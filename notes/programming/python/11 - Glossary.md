# 11 - Python Glossary

| Term | Meaning | Common trap |
| --- | --- | --- |
| Object | Runtime entity with identity, type, and value. | Thinking names contain objects. |
| Name | Binding to an object in a namespace. | Assuming assignment copies. |
| Namespace | Mapping from names to objects. | Forgetting imports bind names. |
| Scope | Region/rule for name lookup. | Local assignment shadowing outer names. |
| Mutable | Can change in place. | Shared aliases see mutation. |
| Immutable | Cannot change value in place. | Tuple can still contain mutable objects. |
| Identity | Object sameness, checked with `is`. | Using `is` for value equality. |
| Equality | Value comparison, checked with `==`. | Custom types can redefine. |
| Iterable | Can produce an iterator. | Not all iterables are reusable. |
| Iterator | Produces next values until exhausted. | One-shot exhaustion. |
| Generator | Lazy iterator made with `yield` or generator expression. | Work is delayed until iteration. |
| Decorator | Callable that transforms function/class. | Hiding metadata without `wraps`. |
| Module | Python import unit, often a `.py` file. | Top-level code runs at import. |
| Package | Collection of modules. | Circular imports from poor boundaries. |
| Exception | Structured failure object. | Catching too broadly. |
| Traceback | Stack evidence for an exception. | Ignoring the original cause. |
| Context manager | Object used with `with` for setup/cleanup. | Relying on garbage collection. |
| Type hint | Annotation for humans/tools. | Not runtime enforcement by default. |
| Coroutine | Awaitable async operation. | Creating without awaiting/scheduling. |
| Event loop | Async scheduler. | Blocking it with sync I/O. |
| Virtual environment | Isolated package environment. | Confusing it with OS isolation. |
| GIL | Global Interpreter Lock in many CPython builds. | Assuming no race conditions. |

## Questions to Test Understanding

1. What is a name?
2. What is an iterator?
3. What does a decorator do?
4. What does a virtual environment isolate?
5. What does the GIL not guarantee?

## Answers and Reasoning

1. A binding from an identifier in a namespace to an object.
2. An object that produces values one at a time until exhausted.
3. It transforms a function or class and rebinds the decorated name.
4. Python packages for a project; not OS packages or external binaries.
5. It does not guarantee application-level thread safety or eliminate race conditions.

