# 10 - Java Cheatsheet

## Runtime Chain

```text
.java -> javac -> .class bytecode -> class loader -> JVM -> heap/stack/GC/JIT
```

## Commands

```bash
java -version
javac -version
javac App.java
java App
javac --release 17 App.java
javap -c App
jcmd <pid> Thread.print
jstack <pid>
```

## Core Rules

| Topic | Rule |
| --- | --- |
| Object equality | Use `.equals`; `==` checks reference identity. |
| Hash collections | Override `hashCode` with `equals`. |
| Passing objects | Java passes reference values by value. |
| Inheritance | Use only for true substitutability. |
| Generics | Compile-time safety; runtime mostly type erasure. |
| Streams | Lazy until terminal operation. |
| GC | Collects unreachable objects, not unwanted reachable objects. |
| `volatile` | Visibility, not compound atomicity. |
| `synchronized` | Mutual exclusion plus visibility. |

## Collection Choices

| Need | Type |
| --- | --- |
| Dynamic list | `ArrayList` |
| Unique values | `HashSet` |
| Key lookup | `HashMap` |
| Sorted keys | `TreeMap` |
| Queue/deque | `ArrayDeque` |
| Blocking producer-consumer | `BlockingQueue` |
| Concurrent map | `ConcurrentHashMap` |

## Common Traps

- `String` comparison with `==`.
- `equals` without `hashCode`.
- mutable objects as hash keys.
- raw generic types.
- swallowed exceptions.
- unbounded executor queues.
- static caches that leak memory.
- classpath dependency mismatch.
- parallel streams used blindly.
- forgetting executor shutdown.

