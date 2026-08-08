# 10 - C++ Cheatsheet

## Build Commands

```bash
g++ -std=c++20 -Wall -Wextra -Werror -pedantic main.cpp -o app
g++ -std=c++20 -fsanitize=address,undefined -g main.cpp -o app
```

## Core Rules

| Topic | Rule |
| --- | --- |
| Lifetime | Never use object before lifetime begins or after it ends. |
| Ownership | Make owner obvious in type. |
| RAII | Tie cleanup to object destruction. |
| Raw pointer | Prefer as non-owning observer only. |
| `unique_ptr` | Default dynamic owner. |
| `shared_ptr` | Use only for true shared ownership. |
| `std::move` | Casts to rvalue; does not move by itself. |
| UB | Avoid; it is not catchable. |
| Vector | Default sequence container. |
| Warnings | Treat as evidence. |

## CP Setup

```cpp
std::ios::sync_with_stdio(false);
std::cin.tie(nullptr);
```

## Common Traps

- returning reference/pointer to local variable
- use-after-free
- double delete
- signed integer overflow
- out-of-bounds access
- invalidated iterators
- moved-from object assumptions
- `shared_ptr` cycles
- non-standard VLAs
- wrong binary search invariant

