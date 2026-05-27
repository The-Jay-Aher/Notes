# 00 - Roadmap and Source Backbone

## Why This Chapter Matters

Java exists because teams needed safer, more portable application development than raw C/C++ deployment could easily provide for large business systems.

## The Big Picture

```text
C/C++ portability pain -> JVM design -> bytecode -> managed runtime -> enterprise adoption -> modern Java
```

## First-Principles Explanation

Cause: native binaries and manual memory management made cross-platform enterprise software hard.

Mechanism: Java compiles source into bytecode executed by a JVM, with managed memory, strong typing, standard libraries, and runtime services.

Immediate result: the same Java program can run across platforms with compatible JVMs.

Long-term impact: Java became a dominant language for enterprise services, Android history, backend systems, and large-scale tooling.

Next connected topic: JVM internals, class loading, garbage collection, generics, collections, and concurrency.

## Core Vocabulary

| Term | Meaning | Why it matters |
| --- | --- | --- |
| JDK | Development kit with compiler and tools. | Needed to build Java. |
| JRE | Runtime environment concept. | Needed to run Java; modern distributions package runtime differently. |
| JVM | Virtual machine executing bytecode. | Core portability layer. |
| Bytecode | JVM instruction format. | Bridge between source and runtime. |
| Class loader | Loads classes into JVM. | Explains classpath and runtime errors. |
| Heap | Object allocation area. | GC and memory issues. |
| Stack | Per-thread call frames/local variables. | Recursion and method execution. |
| GC | Garbage collection. | Automatic memory reclamation. |

## Small Details That Matter Later

- Java passes object references by value, not objects by reference.
- `==` compares references for objects; `.equals()` checks logical equality when implemented.
- Generics use type erasure, which affects runtime type checks.
- `String` is immutable; repeated concatenation in loops can be costly.
- `NullPointerException` is often a design signal, not only a crash.
- Thread safety requires memory visibility, not only "not crashing."
- Checked exceptions shape API design and interview questions.

## Source Backbone

- Java SE 21 docs: <https://docs.oracle.com/en/java/javase/21/>
- Java Language Specification SE 21: <https://docs.oracle.com/javase/specs/jls/se21/html/index.html>
- JVM Specification SE 21: <https://docs.oracle.com/javase/specs/jvms/se21/html/index.html>

## Questions to Test Understanding

1. Why does Java use bytecode?
2. Why is JVM not the same as JDK?
3. Why does GC not mean memory leaks are impossible?
4. Why can `==` be wrong for strings?
5. Why does concurrency require visibility rules?

## Answers and Reasoning

1. Bytecode lets compiled Java run on any compatible JVM instead of recompiling for each platform.
2. JVM runs bytecode; JDK includes tools to compile, package, inspect, and develop Java programs.
3. Objects can remain reachable accidentally through collections, static references, caches, or thread locals.
4. `==` compares object identity; `.equals()` compares content for `String`.
5. Threads may see stale values without proper synchronization, volatile, locks, or concurrency primitives.

