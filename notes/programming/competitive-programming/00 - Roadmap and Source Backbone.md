# 00 - Roadmap and Source Backbone

## Why This Chapter Matters

Competitive programming is not a bag of tricks. It is a disciplined way to convert constraints into algorithms.

## The Big Picture

```text
problem statement -> constraints -> naive idea -> bottleneck -> optimized pattern -> proof -> implementation -> edge cases
```

## First-Principles Explanation

Cause: brute force often matches the story of the problem but not its constraints.

Mechanism: identify repeated work, structure, monotonicity, graph shape, state transitions, or algebraic properties.

Immediate result: the solution moves from too slow to accepted.

Long-term impact: the same pattern becomes recognizable in future problems.

Next connected topic: complexity analysis, data structures, graph algorithms, and dynamic programming.

## Core Vocabulary

| Term | Meaning | Why it matters |
| --- | --- | --- |
| Complexity | Growth of time/memory with input size. | Determines feasibility. |
| Invariant | Statement that remains true during algorithm execution. | Proof tool. |
| State | Information needed to decide future steps. | DP and graph search foundation. |
| Transition | Move from one state to another. | Drives DP and BFS. |
| Monotonicity | One-direction property. | Enables binary search/two pointers. |
| Prefix sum | Precomputed cumulative value. | Removes repeated range sums. |
| DSU | Disjoint Set Union. | Maintains components efficiently. |
| Fenwick tree | Prefix aggregate data structure. | Logarithmic updates/queries. |

## Required Algorithm Template

Every algorithm chapter must include:

1. Problem family.
2. Naive approach.
3. Why naive fails.
4. Optimized idea.
5. Proof or intuition.
6. Complexity.
7. Dry run.
8. Implementation.
9. Edge cases.
10. Common bugs.
11. Practice questions with answers.

## Small Details That Matter Later

- Big O ignores constants only after you know the input size and time limit.
- `O(n log n)` may be too slow if nested inside test cases with large total input.
- Off-by-one errors are algorithm bugs, not formatting mistakes.
- Binary search is about monotonic predicates, not only sorted arrays.
- DP requires defining state before writing recurrence.
- Graph problems often hide direction, weights, indexing, and disconnected components.
- Wrong answer debugging begins with smallest counterexamples.

## Source Backbone

- cp-algorithms: <https://cp-algorithms.com/>
- Fenwick tree reference: <https://cp-algorithms.com/data_structures/fenwick.html>

## Questions to Test Understanding

1. Why should constraints be read before choosing an algorithm?
2. Why is binary search more general than searching a sorted array?
3. Why does DP fail when state is incomplete?
4. Why are dry runs necessary?
5. Why is a proof intuition part of coding?

## Answers and Reasoning

1. Constraints decide whether brute force, sorting, graph traversal, or advanced data structures are feasible.
2. Any monotonic yes/no predicate can be binary searched over an ordered answer space.
3. If state omits information needed for future decisions, transitions merge different cases incorrectly.
4. Dry runs expose index errors and wrong invariants before submission.
5. Without proof intuition, the code may pass samples but fail hidden cases.

