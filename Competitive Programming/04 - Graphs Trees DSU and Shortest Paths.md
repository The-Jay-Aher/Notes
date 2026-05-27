# 04 - Graphs, Trees, DSU, and Shortest Paths

## Why This Chapter Matters

Graph problems hide relationships. Once you model the relationship correctly, the algorithm often becomes standard.

Cause -> Mechanism -> Immediate Result -> Long-Term Impact -> Next Connected Topic:

```text
entities have connections
-> model as graph nodes and edges
-> traversal, components, shortest paths, and tree structure become available
-> BFS/DFS/DSU/Dijkstra solve many problem families
-> advanced graph DP, MST, flows, and tree data structures
```

Source baseline:

- cp-algorithms graph section: <https://cp-algorithms.com/graph/>
- cp-algorithms 0-1 BFS: <https://cp-algorithms.com/graph/01_bfs.html>
- cp-algorithms DSU: <https://cp-algorithms.com/data_structures/disjoint_set_union.html>
- cp-algorithms Dijkstra: <https://cp-algorithms.com/graph/dijkstra.html>

## Core Vocabulary

| Term | Meaning | Trap |
| --- | --- | --- |
| Vertex/node | Entity in graph. | 0-based vs 1-based indexing. |
| Edge | Connection. | Directed vs undirected. |
| Weight | Cost of edge. | Negative weights change algorithm. |
| Component | Connected group. | Disconnected graph ignored. |
| Tree | Connected acyclic graph. | Rooting changes parent/child view. |
| BFS | Level-order traversal. | Works for unweighted shortest path. |
| DFS | Depth traversal. | Recursion depth risk. |
| DSU | Maintains disjoint components. | Needs path compression/rank/size. |
| Dijkstra | Non-negative weighted shortest path. | Fails with negative edges. |

## BFS

Problem family: shortest path in unweighted graph, levels, minimum moves.

```cpp
std::vector<int> dist(n, -1);
std::queue<int> q;
dist[src] = 0;
q.push(src);

while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (int v : adj[u]) {
        if (dist[v] == -1) {
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
}
```

Proof intuition:

```text
BFS explores all nodes at distance d before distance d+1
```

## DFS

Problem family: components, cycle detection, topological ideas, tree DP.

```cpp
void dfs(int u) {
    vis[u] = true;
    for (int v : adj[u]) {
        if (!vis[v]) dfs(v);
    }
}
```

Trap: recursion depth can overflow for `n = 2e5`. Use iterative DFS when needed.

## DSU

Problem family: dynamic connectivity with union operations, Kruskal MST, grouping.

```cpp
struct DSU {
    std::vector<int> parent, sz;

    DSU(int n) : parent(n), sz(n, 1) {
        std::iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (sz[a] < sz[b]) std::swap(a, b);
        parent[b] = a;
        sz[a] += sz[b];
        return true;
    }
};
```

Small detail: DSU handles merges well. It does not handle arbitrary deletions easily.

## Dijkstra

Problem family: shortest path with non-negative weights.

```cpp
const long long INF = 4e18;
std::vector<long long> dist(n, INF);
using P = std::pair<long long, int>;
std::priority_queue<P, std::vector<P>, std::greater<P>> pq;

dist[src] = 0;
pq.push({0, src});

while (!pq.empty()) {
    auto [d, u] = pq.top();
    pq.pop();
    if (d != dist[u]) continue;
    for (auto [v, w] : adj[u]) {
        if (dist[v] > d + w) {
            dist[v] = d + w;
            pq.push({dist[v], v});
        }
    }
}
```

Trap: negative edges invalidate Dijkstra's greedy finalization idea.

## Trees

Tree facts:

- connected with `n - 1` edges
- unique simple path between any two nodes
- DFS/BFS can root the tree
- many problems become parent/children DP

Common tree DP pattern:

```cpp
void dfs(int u, int p) {
    dp[u] = base;
    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
        combine dp[v] into dp[u];
    }
}
```

## Small Details That Matter Later

- Convert input indexes if problem uses 1-based labels.
- Undirected graph needs adding both directions.
- BFS shortest path only for equal edge weights.
- 0-1 BFS works for weights 0/1 using deque.
- Dijkstra requires non-negative weights.
- Bellman-Ford handles negative edges and detects negative cycles, slower.
- DFS recursion depth can crash.
- Parent check matters in undirected DFS.
- Disconnected graphs require loop over all nodes.
- DSU cannot answer path queries inside a component.
- Tree root is chosen for convenience unless problem gives one.

## Debugging / Answer Method

Graph checklist:

1. Directed or undirected?
2. Weighted or unweighted?
3. Negative weights?
4. Connected or disconnected?
5. Need shortest path, reachability, components, ordering, or tree DP?
6. Indexing?
7. Multi-edges/self-loops?
8. Maximum `n + m`?

## Questions to Test Understanding

1. Why does BFS find shortest path in unweighted graphs?
2. Why does Dijkstra fail with negative edges?
3. What does DSU solve?
4. Why can recursive DFS fail?
5. What makes a tree special?

## Answers and Reasoning

1. It processes nodes by increasing edge distance.
2. Its greedy assumption that the current smallest distance is final can be broken by later negative edges.
3. It maintains connected components under merge operations.
4. Deep recursion can exceed call stack.
5. A tree is connected and acyclic, with a unique path between any two nodes.

