# 03 - Recursion, Backtracking, Greedy, and Dynamic Programming

## Why This Chapter Matters

Many hard problems are hard because the choice you make now affects the future. Recursion, backtracking, greedy algorithms, and dynamic programming are different ways to reason about choices.

Cause -> Mechanism -> Immediate Result -> Long-Term Impact -> Next Connected Topic:

```text
problem has branching choices
-> recursion explores state, backtracking searches possibilities, greedy proves local choice, DP memoizes overlapping subproblems
-> exponential brute force may become accepted
-> proof discipline becomes more important than code length
-> graph DP, tree DP, shortest paths, and optimization
```

Source baseline:

- cp-algorithms dynamic programming section: <https://cp-algorithms.com/dynamic_programming/intro-to-dp.html>
- cp-algorithms search/backtracking topics are used as conceptual references.

## Core Idea

| Pattern | When it fits | Main proof |
| --- | --- | --- |
| Recursion | Problem decomposes into smaller similar problems. | Base case and recursive correctness. |
| Backtracking | Need to enumerate/search valid configurations. | Complete exploration with pruning. |
| Greedy | Local choice can be proven safe. | Exchange argument or invariant. |
| DP | Overlapping subproblems and optimal substructure. | State definition and recurrence. |

## Recursion Template

Problem family: tree-like decomposition, DFS, divide and conquer.

Naive idea: write loops manually for every depth.

Optimized idea: define a function that solves a smaller version.

```cpp
long long factorial(int n) {
    if (n <= 1) return 1;
    return 1LL * n * factorial(n - 1);
}
```

Common bugs:

- missing base case
- no progress toward base case
- stack overflow
- recomputing too much

## Backtracking Template

Problem family: subsets, permutations, combinations, N-Queens, Sudoku-style search.

```cpp
void backtrack(int i, std::vector<int>& cur) {
    if (i == n) {
        process(cur);
        return;
    }
    backtrack(i + 1, cur);
    cur.push_back(a[i]);
    backtrack(i + 1, cur);
    cur.pop_back();
}
```

Mental model:

```text
choose
-> recurse
-> undo choice
```

Pruning:

```text
if partial state can never lead to valid answer, stop early
```

## Greedy Template

Problem family: intervals, scheduling, selecting minimum/maximum under constraints, Huffman-like merging.

Algorithm process:

1. Identify candidate local choice.
2. Prove it does not harm optimality.
3. Implement with sort/heap/data structure.

Example: minimum number of rooms for intervals.

```cpp
std::sort(events.begin(), events.end());
int cur = 0, best = 0;
for (auto [time, delta] : events) {
    cur += delta;
    best = std::max(best, cur);
}
```

Greedy danger:

```text
looks obvious but lacks proof
```

If you cannot prove local choice is safe, suspect DP.

## Dynamic Programming Template

DP fits when:

```text
same subproblem repeats
and
optimal answer can be built from smaller answers
```

Steps:

1. Define state.
2. Define transition.
3. Define base cases.
4. Define answer extraction.
5. Determine computation order.
6. Analyze complexity.

### Example: Fibonacci

Naive recursion:

```cpp
long long fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```

Why fails: repeated subproblems.

Memoization:

```cpp
std::vector<long long> memo(n + 1, -1);

long long fib(int i) {
    if (i <= 1) return i;
    if (memo[i] != -1) return memo[i];
    return memo[i] = fib(i - 1) + fib(i - 2);
}
```

Tabulation:

```cpp
std::vector<long long> dp(n + 1);
dp[0] = 0;
dp[1] = 1;
for (int i = 2; i <= n; ++i) {
    dp[i] = dp[i - 1] + dp[i - 2];
}
```

## DP State Examples

| Problem type | State idea |
| --- | --- |
| knapsack | `dp[i][w]`: best using first i items with capacity w |
| grid paths | `dp[r][c]`: ways/best to reach cell |
| LIS | `dp[i]`: best subsequence ending at i |
| interval DP | `dp[l][r]`: best answer for interval |
| bitmask DP | `dp[mask]`: answer for chosen subset |
| tree DP | `dp[u]`: answer for subtree rooted at u |

## Small Details That Matter Later

- DP fails when state omits information needed for future decisions.
- Memoization follows recursion; tabulation follows dependency order.
- Initialize impossible states carefully.
- Use large negative/positive sentinels safely.
- Modulo problems require modulo at every addition/multiplication step.
- Greedy needs proof, not confidence.
- Backtracking must undo state.
- Recursion depth can overflow stack.
- Bitmask DP often needs `1 << n`; use 64-bit if n can exceed int shift limits.

## Debugging / Answer Method

For DP:

```text
state -> transition -> base -> order -> answer -> complexity
```

For greedy:

```text
choice -> why safe -> what invariant remains true -> implementation -> counterexample search
```

For backtracking:

```text
choices -> validity -> pruning -> undo -> completeness
```

## Questions to Test Understanding

1. When does DP apply?
2. Why does incomplete state break DP?
3. What is backtracking undo?
4. Why does greedy need proof?
5. What is the difference between memoization and tabulation?

## Answers and Reasoning

1. When subproblems overlap and optimal solutions can be composed from smaller states.
2. Different future possibilities get merged into one state, causing wrong transitions.
3. Reverting the chosen change after returning from recursion so other branches see clean state.
4. A local best-looking choice can be globally wrong unless proven safe.
5. Memoization is top-down recursion with cache; tabulation fills states bottom-up in dependency order.

