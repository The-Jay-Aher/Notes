# 11 - Competitive Programming Glossary

| Term | Meaning | Trap |
| --- | --- | --- |
| Complexity | Growth of time/memory. | Ignoring total input. |
| Invariant | Statement kept true. | Coding without proof. |
| Monotonic predicate | Once true/false remains so over ordered domain. | Binary searching non-monotonic condition. |
| Prefix sum | Cumulative sum table. | Off-by-one. |
| Sliding window | Moving segment with maintained state. | Negative values can break sum logic. |
| DP state | Information defining subproblem. | Incomplete state. |
| Transition | Move from one state to another. | Wrong dependency order. |
| BFS | Queue traversal by levels. | Weighted graph misuse. |
| DFS | Depth traversal. | Stack overflow. |
| DSU | Merge/find components. | Deletions not supported easily. |
| Dijkstra | Non-negative shortest path. | Negative edge misuse. |
| Fenwick | Log update/prefix query structure. | Indexing bugs. |
| Segment tree | Flexible range query/update tree. | Lazy propagation mistakes. |
| Mod inverse | Division under modulus. | Requires conditions. |
| KMP | Exact pattern matching with prefix function. | Prefix function off-by-one. |

## Questions to Test Understanding

1. What enables binary search on answer?
2. What makes DP valid?
3. What does DSU not handle easily?
4. Which shortest path algorithm fits non-negative weights?
5. Which structure fits point update plus range sum?

## Answers and Reasoning

1. A monotonic predicate over an ordered search space.
2. Complete state, correct recurrence, base cases, and dependency order.
3. Arbitrary deletions/splits.
4. Dijkstra.
5. Fenwick tree.

