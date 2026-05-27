# 11 - Java Glossary

| Term | Meaning | Common trap |
| --- | --- | --- |
| JDK | Java development kit. | Confusing with JVM only. |
| JVM | Runtime virtual machine for bytecode. | Thinking it is the compiler. |
| Bytecode | Portable JVM instruction form. | Ignoring class file version. |
| Class loader | Loads class definitions. | Classpath conflicts. |
| Heap | Object allocation memory. | Reachable leaks still leak. |
| Stack | Per-thread call frames. | Deep recursion causes stack overflow. |
| GC | Garbage collector. | Does not collect reachable unused objects. |
| JIT | Runtime compiler for hot paths. | Benchmarks ignoring warmup. |
| Encapsulation | Protect state through methods. | Public mutable fields. |
| Interface | Behavior contract. | Too-broad interfaces. |
| Generics | Type parameters for safety. | Raw types and type erasure. |
| Type erasure | Generic type mostly removed at runtime. | Runtime `List<String>` checks. |
| Collection | Data structure API family. | Wrong type for access pattern. |
| Stream | Lazy data-processing pipeline. | Hidden side effects. |
| Lambda | Functional expression. | Capturing mutable state carelessly. |
| Checked exception | Must be caught/declared. | Leaking implementation details. |
| Race condition | Timing-dependent bug. | Tests not exposing it. |
| `volatile` | Visibility for variable. | Not atomic increments. |
| `synchronized` | Lock plus visibility. | Oversized critical sections. |
| Executor | Task execution manager. | Not shutting down. |
| Deadlock | Threads wait forever on each other. | Inconsistent lock ordering. |

## Questions to Test Understanding

1. What executes Java bytecode?
2. What does `==` compare for objects?
3. Why must equal objects have same hash code?
4. What does type erasure explain?
5. What does `volatile` not provide?

## Answers and Reasoning

1. The JVM.
2. Reference identity.
3. Hash collections depend on hash code to find equal objects.
4. Generic type information is mostly not available at runtime.
5. Atomicity for compound operations such as increment.

