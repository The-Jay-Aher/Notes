# 00 - Roadmap and Source Backbone

## Why This Chapter Matters

C++ gives control over memory, layout, lifetime, and performance. That power is useful precisely because it is dangerous. Good C++ notes must explain not only what code does, but what assumptions make it legal.

## The Big Picture

```text
C performance and systems access -> abstraction without mandatory runtime -> object lifetime control -> templates and STL -> modern ownership patterns -> undefined behavior traps
```

## First-Principles Explanation

Cause: programmers needed high-level abstractions without giving up low-level control.

Mechanism: C++ adds classes, constructors/destructors, templates, RAII, generic libraries, and modern move semantics while preserving native compilation and manual control.

Immediate result: efficient abstractions are possible.

Long-term impact: C++ powers systems, games, trading, embedded, browsers, databases, and competitive programming.

Next connected topic: compilation, linking, object lifetime, ownership, RAII, STL, templates, and undefined behavior.

## Core Vocabulary

| Term | Meaning | Why it matters |
| --- | --- | --- |
| Translation unit | Source file after preprocessing. | Explains compilation model. |
| Header | Declarations shared across files. | Affects linking and ODR. |
| RAII | Resource lifetime bound to object lifetime. | Core safety pattern. |
| Pointer | Object address-like value. | Can dangle or be null. |
| Reference | Alias to object. | Must refer to valid object. |
| Move semantics | Transfer resources from temporary/expiring objects. | Performance and ownership. |
| Template | Compile-time generic code. | Powers STL and metaprogramming. |
| Undefined behavior | Program has no required meaning. | Compiler can optimize unpredictably. |

## Small Details That Matter Later

- Undefined behavior is not an exception; the program has no guaranteed meaning.
- RAII is about all resources, not only memory.
- `std::move` does not move by itself; it casts to an rvalue expression.
- A moved-from standard library object is valid but often unspecified.
- References can dangle just like pointers can.
- Header mistakes can become linker errors or ODR bugs.
- Iterator invalidation rules differ by container.
- Signed integer overflow is undefined behavior in C++.

## Source Backbone

- cppreference C++ language: <https://en.cppreference.com/w/cpp/language>
- cppreference RAII: <https://en.cppreference.com/w/cpp/language/raii>
- cppreference undefined behavior: <https://en.cppreference.com/w/cpp/language/ub>
- cppreference `std::move`: <https://en.cppreference.com/w/cpp/utility/move>

## Questions to Test Understanding

1. Why is RAII central to C++?
2. Why is undefined behavior worse than a normal runtime error?
3. Why does `std::move` not guarantee a physical move?
4. Why do headers exist?
5. Why can C++ be fast and dangerous at the same time?

## Answers and Reasoning

1. It ties cleanup to object lifetime, making resource release deterministic.
2. The compiler may assume it never happens and optimize in surprising ways.
3. It only changes value category; the selected move operation determines what happens.
4. They share declarations so separately compiled translation units agree on interfaces.
5. Native compilation and low-level control avoid overhead, but invalid lifetime, aliasing, and bounds assumptions can break correctness.

