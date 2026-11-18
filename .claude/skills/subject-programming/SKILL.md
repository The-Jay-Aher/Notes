---
name: subject-programming
description: Coverage and teaching requirements for Competitive Programming, Java, Python, C++ and low-level design in this vault - the topic checklists, the per-algorithm explanation checklist, and how to coach problem solving without handing over solutions. Load it whenever creating, upgrading, teaching or quizzing anything about algorithms, data structures, problem solving, or the Java, Python or C++ languages, together with deep-notes (writing) or teach/quiz/revise (learning).
---

# Programming: Competitive Programming, Java, Python, C++

Folders: `notes/programming/competitive-programming/`, `java/`, `python/`, `cpp/`, and `low-level-design/` (no dedicated checklist yet; use the general rules in deep-notes).

Teach using both conceptual understanding and problem-solving ability. State the language version a note assumes (for example Java 21, Python 3.12, C++17/20) wherever behavior differs between versions.

## Competitive Programming

Cover:

- problem-solving mindset
- complexity analysis
- Big O
- input/output optimization
- arrays
- strings
- hashing
- sorting
- binary search
- two pointers
- sliding window
- prefix sums
- difference arrays
- recursion
- backtracking
- bit manipulation
- greedy algorithms
- dynamic programming
- graph algorithms
- BFS
- DFS
- Dijkstra
- Bellman-Ford
- Floyd-Warshall
- DSU
- trees
- segment trees
- Fenwick trees
- tries
- heaps
- priority queues
- number theory
- combinatorics
- modular arithmetic
- game theory basics
- common patterns
- debugging wrong answers
- avoiding TLE
- avoiding MLE
- practice problems with explanations

For each algorithm:

- explain the naive idea
- explain why it fails or becomes slow
- explain the optimized idea
- explain the proof or intuition
- explain complexity
- show implementation
- show dry run
- show edge cases
- show common bugs
- provide practice problems

## Java

- JVM
- JDK vs JRE
- compilation and bytecode
- class loading
- memory model
- stack vs heap
- garbage collection
- object-oriented programming
- classes and objects
- inheritance
- polymorphism
- abstraction
- encapsulation
- interfaces
- generics
- collections
- exceptions
- streams
- lambdas
- concurrency
- threads
- synchronization
- executors
- file handling
- networking basics
- Spring overview where useful
- interview questions
- coding examples

## Python

- interpreter model
- variables and references
- data types
- lists
- tuples
- dictionaries
- sets
- functions
- decorators
- generators
- iterators
- comprehensions
- modules
- packages
- virtual environments
- error handling
- file handling
- OOP
- typing
- async basics
- memory model
- GIL
- standard library
- scripting for DevOps
- automation examples
- interview and coding examples

## C++

- compilation model
- headers
- linking
- memory layout
- stack vs heap
- pointers
- references
- RAII
- constructors
- destructors
- copy semantics
- move semantics
- classes
- inheritance
- polymorphism
- templates
- STL
- vectors
- maps
- sets
- unordered containers
- iterators
- algorithms
- lambdas
- smart pointers
- concurrency basics
- undefined behavior
- performance
- competitive programming patterns

For C++, always explain dangerous details carefully. C++ is less a language and more a chainsaw with templates.

## Teaching and quizzing programming

- **The student writes the code.** Don't open with a full solution. Give the problem, then a hint ladder, and stop at the first rung that unblocks them:
  1. an observation about the input or constraints,
  2. the pattern or technique family,
  3. the key insight or invariant,
  4. pseudocode,
  5. the full solution, with a dry run.
- **Read the constraints first.** Before any approach, ask: "n is up to 2·10^5. Which complexities are allowed?" Turning constraints into a complexity budget is the most reusable skill in competitive programming.
- **Dry runs by hand.** For every new algorithm, the student traces a small input step by step, including the state of the data structure. Ask them to find an input that breaks a buggy version.
- **Predict the output** for language questions: what this Python snippet prints (mutable default arguments, late-binding closures), what this Java code does (`==` vs `equals`, integer caching), what is undefined behavior in this C++.
- **Review the student's own solutions** when they share them: correctness, complexity, edge cases (empty input, n = 1, duplicates, overflow, negative numbers), then style. Point to the bug and why it happens; don't rewrite the solution wholesale.
- **Spaced practice** works per pattern, not per problem. Log the technique the student missed ("didn't see monotonic stack") in the Learning Tracker, then revise it with a different problem that needs the same technique.
