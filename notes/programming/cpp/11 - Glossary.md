# 11 - C++ Glossary

| Term | Meaning | Common trap |
| --- | --- | --- |
| Translation unit | Source after preprocessing. | Assuming headers compile alone. |
| Declaration | Introduces name/interface. | No definition for linker. |
| Definition | Provides entity/body/storage. | Multiple definitions in headers. |
| ODR | One Definition Rule. | Subtle UB/linker errors. |
| Lifetime | Period object is valid. | Dangling references. |
| RAII | Cleanup tied to object lifetime. | Thinking only memory. |
| Undefined behavior | No required meaning. | Expecting crash. |
| Pointer | Address-like value. | Null/dangling/owning confusion. |
| Reference | Alias to object. | Can dangle. |
| `unique_ptr` | Exclusive owner. | Trying to copy it. |
| `shared_ptr` | Shared ownership. | Cycles and overhead. |
| `weak_ptr` | Non-owning observer of shared object. | Forgetting to lock/check. |
| Move semantics | Resource transfer from expiring object. | Using moved-from value. |
| Template | Compile-time generic code. | Long diagnostics. |
| Iterator | Position in range/container. | Invalidation. |
| STL | Standard containers/algorithms/utilities. | Wrong container choice. |
| Sanitizer | Instrumented bug detector. | Not enabled in normal release. |

## Questions to Test Understanding

1. What does RAII protect?
2. What is UB?
3. Which smart pointer is default for exclusive ownership?
4. What does `std::move` do?
5. Why can vector iterators become invalid?

## Answers and Reasoning

1. Any resource whose cleanup should follow object lifetime.
2. Behavior with no required meaning under the standard.
3. `std::unique_ptr`.
4. Casts expression to rvalue so move operations can be selected.
5. Vector may reallocate and move elements to new storage.

