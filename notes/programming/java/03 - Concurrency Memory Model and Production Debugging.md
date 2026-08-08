# 03 - Concurrency, Memory Model, and Production Debugging

## Why This Chapter Matters

Java made threads mainstream in enterprise programming, but concurrency is where "works on my machine" becomes dangerous.

The hard part is not creating a thread. The hard part is making shared state correct and visible across threads.

Cause -> Mechanism -> Immediate Result -> Long-Term Impact -> Next Connected Topic:

```text
servers must handle many requests at once
-> Java provides threads, locks, volatile, executors, concurrent collections, and memory model rules
-> applications can do concurrent work
-> correctness depends on synchronization, visibility, atomicity, lifecycle, and backpressure
-> production debugging, performance tuning, and reliable backend design
```

Official source baseline:

- Java Language Specification, memory model chapter: <https://docs.oracle.com/javase/specs/jls/se21/html/jls-17.html>
- Java SE API docs, concurrency package: <https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/concurrent/package-summary.html>
- Java Thread docs: <https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Thread.html>

Version assumption: examples use Java 21-compatible APIs. Virtual threads and structured concurrency details are version-sensitive; verify exact production JDK behavior before designing around newer concurrency features.

## The Big Picture

```mermaid
flowchart LR
    Work[Concurrent work] --> Threads[Threads]
    Threads --> Shared[Shared state]
    Shared --> Problems[Race visibility deadlock]
    Problems --> Tools[synchronized volatile locks atomics executors queues]
    Tools --> Design[Safe concurrent design]
```

Concurrency questions:

```text
What state is shared?
Who can mutate it?
How is visibility guaranteed?
What operation must be atomic?
How is work queued?
How is shutdown handled?
What happens under overload?
```

## First-Principles Explanation

### Race Condition

A race condition happens when correctness depends on timing between threads.

Example:

```java
counter++;
```

This looks like one operation but conceptually includes:

```text
read counter
add one
write counter
```

Two threads can interleave and lose updates.

### Visibility

Even if one thread writes a value, another thread may not see it immediately without a happens-before relationship.

This is why Java has:

- `synchronized`
- `volatile`
- locks
- concurrent collections
- atomics
- thread start/join rules

### Atomicity

Atomicity means an operation appears indivisible.

`volatile` gives visibility for reads/writes of the variable, but it does not make compound operations like increment atomic.

## Core Vocabulary

| Term | Meaning | Why it matters |
| --- | --- | --- |
| Thread | Independent execution path. | Handles concurrent work. |
| Race condition | Timing-dependent correctness bug. | Hard to reproduce. |
| Visibility | Whether one thread sees another's writes. | Memory model issue. |
| Atomicity | Operation appears indivisible. | Needed for counters and state transitions. |
| `synchronized` | Lock-based mutual exclusion plus visibility. | Simple correctness tool. |
| `volatile` | Visibility and ordering for a variable. | Not enough for compound actions. |
| Executor | Manages task execution with worker threads. | Better than manual thread creation. |
| Future | Represents pending result. | Coordinates async completion. |
| Deadlock | Threads wait forever on each other. | Production stall. |
| Backpressure | Limiting intake when processing cannot keep up. | Prevents overload collapse. |

## Mental Model

Correct concurrency needs both:

```text
mutual exclusion when shared state must not be changed concurrently
visibility so threads see each other's changes
```

Design preference:

```text
avoid shared mutable state
-> use immutable objects
-> use thread-safe queues
-> use executors
-> use concurrent collections
-> synchronize only clear critical sections
```

## Step-by-Step Explanation

### Basic Thread

```java
Thread worker = new Thread(() -> System.out.println("work"));
worker.start();
worker.join();
```

Use threads directly for learning. In real applications, prefer executors.

### Executor

```java
ExecutorService pool = Executors.newFixedThreadPool(4);
try {
    Future<Integer> result = pool.submit(() -> compute());
    System.out.println(result.get());
} finally {
    pool.shutdown();
}
```

Why executor:

- controls thread count
- reuses threads
- gives task abstraction
- supports shutdown

### Synchronization

```java
class Counter {
    private int value;

    synchronized void increment() {
        value++;
    }

    synchronized int value() {
        return value;
    }
}
```

`synchronized` protects the critical section and establishes visibility.

### Atomic Counter

```java
AtomicInteger counter = new AtomicInteger();
counter.incrementAndGet();
```

Useful for simple atomic numeric state.

### Volatile Flag

```java
class StopSignal {
    private volatile boolean stopped;

    void stop() {
        stopped = true;
    }

    boolean stopped() {
        return stopped;
    }
}
```

Good for simple visibility flag. Not enough for compound invariants.

## Internal Mechanics

### Happens-Before

The Java Memory Model defines rules for when one action's effects are visible to another.

Examples:

- unlock happens-before later lock on same monitor
- volatile write happens-before later volatile read of same variable
- thread start has ordering effects
- thread join has ordering effects

You do not need to memorize every formal rule at first. You must know that without a rule, visibility is not guaranteed.

### Deadlock

```text
Thread A holds lock 1 and waits for lock 2
Thread B holds lock 2 and waits for lock 1
```

Mitigation:

- consistent lock ordering
- smaller critical sections
- timeouts where appropriate
- avoid nested locks when possible
- use higher-level concurrency utilities

### Thread Pools Can Fail Under Load

Unbounded queues can hide overload until memory grows. Too many threads can increase context switching and memory use.

Production question:

```text
what happens when requests arrive faster than workers finish them?
```

If the answer is "queue forever," the system may fail later and harder.

## Practical Examples

### Safe Producer Consumer

```java
BlockingQueue<String> queue = new ArrayBlockingQueue<>(1000);

ExecutorService workers = Executors.newFixedThreadPool(4);
for (int i = 0; i < 4; i++) {
    workers.submit(() -> {
        while (!Thread.currentThread().isInterrupted()) {
            String item = queue.take();
            process(item);
        }
        return null;
    });
}
```

Why `BlockingQueue` matters:

- thread-safe
- can bound capacity
- provides backpressure

### Avoid Shared Mutable State

Bad:

```java
List<String> results = new ArrayList<>();
parallelTasks.forEach(task -> results.add(task.run()));
```

`ArrayList` is not thread-safe.

Better:

- collect results through futures
- use thread-safe collection if appropriate
- redesign each task to return value

## Small Details That Matter Later

- `volatile` is not a replacement for locks for compound operations.
- `ArrayList`, `HashMap`, and most ordinary collections are not thread-safe.
- `ConcurrentHashMap` does not make compound multi-step business logic automatically atomic.
- Always shut down executors.
- Blocking inside a small thread pool can starve other tasks.
- Thread locals can cause memory leaks in pooled threads if not cleared.
- Deadlocks may show as no CPU usage but stuck request threads.
- Race conditions can disappear when logging is added because timing changes.
- Immutability is one of the strongest concurrency tools.
- Timeouts are part of concurrency design, not only network design.
- Parallel streams use shared pools and can surprise application behavior.
- Production debugging often needs thread dumps.

## Common Misunderstandings

### Misunderstanding 1: "Volatile makes everything thread-safe."

It gives visibility/order for a variable. It does not make compound actions atomic.

### Misunderstanding 2: "Concurrent collection means my workflow is safe."

Each collection operation may be safe, but your sequence of operations may still race.

### Misunderstanding 3: "More threads means faster."

More threads can increase overhead, memory, lock contention, and downstream overload.

### Misunderstanding 4: "If a race did not happen in testing, it is fixed."

Concurrency bugs are timing-dependent and may appear under different CPU, load, GC, or deployment conditions.

## Failure Modes / Mistakes / Traps

### Trap 1: Lost Update

```java
value++;
```

Without synchronization/atomicity, concurrent increments can lose updates.

### Trap 2: Visibility Bug

```java
boolean running = true;
```

One thread changes it; another loops forever because it never observes the write.

### Trap 3: Executor Not Shut Down

Non-daemon worker threads keep process alive.

### Trap 4: Unbounded Queue

System accepts unlimited work and fails with memory pressure.

## Debugging / Analysis / Answer-Writing Method

Concurrency bug method:

1. Identify shared mutable state.
2. Identify all readers and writers.
3. Identify required invariants.
4. Check synchronization/volatile/atomic/concurrent collection use.
5. Check executor queue and thread count.
6. Check shutdown and cancellation.
7. Capture thread dump for deadlock/stall.
8. Add tests, but do not trust tests alone for proof.

Useful commands:

```bash
jcmd <pid> Thread.print
jstack <pid>
jcmd <pid> GC.heap_info
```

Availability and exact tool behavior depend on JDK and environment.

## Real-World or Exam Relevance

Interview questions:

- What is a race condition?
- What is the Java Memory Model?
- `synchronized` vs `volatile`?
- How does `ExecutorService` help?
- What causes deadlock?
- Why is `HashMap` unsafe under concurrent mutation?
- What is backpressure?
- How do you debug a stuck Java service?

Strong answer:

```text
Java concurrency requires atomicity and visibility. `synchronized` provides mutual exclusion and visibility for a critical section. `volatile` provides visibility for a variable but not atomic compound actions. Executors manage task execution better than manual threads, and safe design avoids shared mutable state where possible.
```

## Connected Topics

- [JVM Compilation Bytecode and Runtime Foundations](01%20-%20JVM%20Compilation%20Bytecode%20and%20Runtime%20Foundations.md)
- [OOP Generics Collections Exceptions and Streams](02%20-%20OOP%20Generics%20Collections%20Exceptions%20and%20Streams.md)
- Operating-system threads.
- Distributed systems queues and backpressure.
- Production observability and thread dumps.

## Chapter Summary

Java concurrency is not about starting threads. It is about designing correct relationships between tasks and state.

The practical rules:

```text
avoid shared mutable state
use immutable data
use executors instead of raw thread sprawl
use synchronized/locks/atomics/volatile deliberately
bound queues when overload is possible
shut down resources
debug with thread dumps and evidence
```

## Questions to Test Understanding

1. What is a race condition?
2. Why is `counter++` not safely atomic?
3. What does `volatile` provide?
4. What does `synchronized` provide?
5. Why are executors preferred over manual thread creation?
6. What is deadlock?
7. What is backpressure?
8. Why can unbounded queues be dangerous?
9. Why can logging hide a race condition?
10. How do you start debugging a stuck Java process?

## Answers and Reasoning

1. A correctness bug where outcome depends on timing/interleaving between threads.
2. It involves read, add, and write steps that can interleave with other threads.
3. Visibility and ordering for reads/writes of that variable, not compound atomicity.
4. Mutual exclusion for a critical section and memory visibility through monitor enter/exit rules.
5. They manage thread reuse, limits, task submission, futures, and shutdown.
6. Threads wait forever because each holds a resource the other needs.
7. A mechanism to slow or reject incoming work when processing cannot keep up.
8. They can accumulate work until memory pressure or latency collapse.
9. Logging changes timing and synchronization behavior enough to hide timing bugs.
10. Capture a thread dump, inspect blocked/waiting/runnable threads, locks, pools, and recent logs/metrics.

