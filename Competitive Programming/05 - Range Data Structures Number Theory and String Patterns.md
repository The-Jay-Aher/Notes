# 05 - Range Data Structures, Number Theory, and String Patterns

## Why This Chapter Matters

Once arrays need updates, prefix sums are not enough. Once numbers get large, direct simulation fails. Once string matching becomes repeated, naive substring checks fail.

This chapter is the bridge from beginner patterns to advanced contest tools.

## Range Data Structures

### Fenwick Tree

Problem family: point updates and prefix/range sum queries.

Naive:

```text
update O(1), range query O(n)
or
prefix query O(1), update O(n)
```

Fenwick idea:

```text
store partial prefix blocks based on binary lowbit
```

Implementation, 1-based:

```cpp
struct Fenwick {
    int n;
    std::vector<long long> bit;

    Fenwick(int n) : n(n), bit(n + 1, 0) {}

    void add(int idx, long long delta) {
        for (++idx; idx <= n; idx += idx & -idx) {
            bit[idx] += delta;
        }
    }

    long long sum_prefix(int idx) {
        long long res = 0;
        for (++idx; idx > 0; idx -= idx & -idx) {
            res += bit[idx];
        }
        return res;
    }

    long long sum_range(int l, int r) {
        return sum_prefix(r) - (l ? sum_prefix(l - 1) : 0);
    }
};
```

Complexity: O(log n) update/query.

### Segment Tree

Use when you need more general range queries/updates:

- min/max/sum/gcd
- custom merge
- lazy propagation for range updates

Fenwick is smaller and simpler for prefix-invertible operations like sums. Segment tree is more flexible.

## Heaps and Priority Queues

Use when repeatedly needing current best/min/max.

```cpp
std::priority_queue<int> max_heap;
std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
```

Common uses:

- Dijkstra
- scheduling
- k largest/smallest
- greedy merging

## Tries

Use for prefix strings or bitwise paths.

String trie:

```text
each edge is character
path from root forms prefix
```

Common tasks:

- prefix search
- dictionary matching
- maximum XOR with bit trie

## Number Theory

### GCD

```cpp
long long g = std::gcd(a, b);
```

Euclidean idea:

```text
gcd(a, b) = gcd(b, a mod b)
```

### Modular Arithmetic

For modulus `MOD`:

```cpp
ans = (ans + x) % MOD;
ans = (ans * y) % MOD;
```

Use `long long` for multiplication before modulo unless values can exceed 64-bit.

### Fast Exponentiation

```cpp
long long mod_pow(long long a, long long e, long long mod) {
    long long res = 1 % mod;
    while (e > 0) {
        if (e & 1) res = res * a % mod;
        a = a * a % mod;
        e >>= 1;
    }
    return res;
}
```

Use for modular powers and inverses under prime mod via Fermat when valid.

## String Patterns

### Prefix Function / KMP

Use when repeated pattern matching must avoid rechecking characters.

Idea:

```text
when mismatch occurs, reuse longest prefix that is also suffix
```

### Z-Function

For each position, stores longest substring starting there matching prefix.

Useful for:

- pattern matching
- string periodicity
- prefix comparisons

### Hashing

Rolling hash can compare substrings quickly but has collision risk.

For contests:

- use large mod(s) or unsigned hash carefully
- understand collisions can cause wrong answer
- do not use hashing where exact algorithms are easy enough

## Small Details That Matter Later

- Fenwick indexing is the most common bug; decide 0-based wrapper or 1-based internal.
- Segment tree size often uses `4*n`.
- Lazy propagation requires pushing pending updates before going deeper.
- Priority queue in C++ is max-heap by default.
- Modular division requires modular inverse and valid conditions.
- `a % mod` can be negative in C++; normalize if needed.
- GCD handles zero but define problem behavior.
- String hashing has collision risk; KMP/Z are exact.
- Trie memory can be large; alphabet size matters.
- Number theory problems often hide overflow.

## Debugging / Answer Method

For range query:

```text
static no updates -> prefix sparse table depending query
point update + prefix/range sum -> Fenwick
range update or custom aggregate -> segment tree
```

For number theory:

```text
factor constraints
-> primes/mod/gcd?
-> overflow?
-> modular inverse conditions?
```

For strings:

```text
single scan -> frequency/window
exact repeated pattern -> KMP/Z
many substring comparisons -> hashing with collision awareness
```

## Questions to Test Understanding

1. When is Fenwick tree useful?
2. Why use segment tree instead of prefix sums?
3. What is lazy propagation?
4. What is a min-heap in C++ priority_queue syntax?
5. Why can modular division fail?
6. What is binary exponentiation?
7. Why does KMP avoid repeated work?
8. What is rolling hash risk?
9. Why can trie memory be high?
10. Why normalize negative modulo?

## Answers and Reasoning

1. Dynamic point updates with prefix/range aggregate queries such as sums.
2. Updates or complex range operations make static prefix sums insufficient.
3. Deferring range updates at tree nodes and pushing them only when necessary.
4. `priority_queue<T, vector<T>, greater<T>>`.
5. Inverse may not exist if divisor and modulus are not coprime.
6. Repeated squaring to compute powers in O(log exponent).
7. It reuses prefix/suffix information after mismatch.
8. Different strings can hash to same value.
9. Each node can store many child pointers/arrays; large alphabets multiply memory.
10. C++ `%` can return negative result for negative input.

