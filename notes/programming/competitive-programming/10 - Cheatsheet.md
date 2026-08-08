# 10 - Competitive Programming Cheatsheet

## Problem Method

```text
constraints -> complexity budget -> naive idea -> bottleneck -> optimized pattern -> proof -> code -> edge cases
```

## Pattern Map

| Symptom | Pattern |
| --- | --- |
| Many static range sums | Prefix sums |
| Many range adds, final array | Difference array |
| Monotonic yes/no answer | Binary search on answer |
| Sorted pair search | Two pointers |
| Longest segment with monotonic validity | Sliding window |
| Repeated subproblems | DP |
| All configurations | Backtracking |
| Local choice provably safe | Greedy |
| Unweighted shortest path | BFS |
| Components / traversal | DFS |
| Merge connectivity | DSU |
| Non-negative weighted shortest path | Dijkstra |
| Dynamic prefix sums | Fenwick |
| General range queries/updates | Segment tree |

## C++ CP Setup

```cpp
std::ios::sync_with_stdio(false);
std::cin.tie(nullptr);
```

## Edge Cases

- empty/minimum input
- one element
- all equal
- sorted/reverse
- duplicates
- negative values
- max values/overflow
- disconnected graph
- no solution
- multiple test cases

