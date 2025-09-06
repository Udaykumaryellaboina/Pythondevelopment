# Floyd–Warshall Algorithm — Explanation + Python implementation (copy-paste friendly)

## Short summary
"""
Floyd–Warshall is an **all-pairs shortest paths** algorithm: it computes the shortest path distance between **every** pair of vertices in a weighted graph.
It handles **negative edge weights** (unlike Dijkstra) and can detect negative cycles. The method uses dynamic programming with a triple loop over nodes and runs in `O(V³)` time.

---

## Why it’s used

* You need shortest distances **between every pair** of nodes (not just single-source).
* You want a simple algorithm that handles **negative edge weights** (but not negative cycles).
* It’s very easy to implement and reason about (matrix-based DP).
* Useful when `V` is small-to-moderate and you need complete distance information (dense graphs or small graphs).

---

## When to use / limitations

* **Use Floyd–Warshall** when:

  * You require **all-pairs** shortest paths.
  * The graph is relatively small (because `O(V³)` grows quickly).
  * Edge weights may be negative but you still want to compute shortest paths (and detect negative cycles).
* **Avoid** if:

  * Graph is large (V in thousands) — `O(V³)` becomes impractical.
  * Graph is sparse and you only need a few source nodes — use repeated Dijkstra (or Johnson’s algorithm) instead.

---

## Time & space complexity

* **Time:** `O(V³)` (three nested loops over vertices).
* **Space:** `O(V²)` to store the distance matrix (and `O(V²)` extra if you store path reconstruction helpers like `next`).
* Path reconstruction requires additional `O(V²)` space for the successor/predecessor matrix.

---

## High-level idea

Let `dist[i][j]` be the shortest distance from vertex `i` to vertex `j` using only intermediate vertices from the set `{0..k-1}`. The classical DP recurrence:

```
dist_k[i][j] = min(dist_{k-1}[i][j], dist_{k-1}[i][k] + dist_{k-1}[k][j])
```

We iterate `k` from `0` to `V-1` and update `dist` in place. If at the end `dist[i][i] < 0` for some `i`, a negative cycle exists reachable from `i`.

---

## Python implementation (with path reconstruction & negative-cycle handling)

```python"""
from typing import Iterable, Tuple, Any, List, Dict, Optional
import math

INF = float('inf')
NEG_INF = -float('inf')

def floyd_warshall(edges: Iterable[Tuple[Any, Any, float]]):
    """
    Floyd-Warshall algorithm for all-pairs shortest paths.

    Args:
        edges: iterable of (u, v, weight). For undirected graphs, include both directions.

    Returns:
        nodes: list of nodes (index -> node)
        dist: 2D list of distances (dist[i][j] is shortest distance from nodes[i] -> nodes[j])
              distances may be INF (no path) or NEG_INF (path can be made arbitrarily small due to a negative cycle).
        next_hop: 2D list used for path reconstruction. next_hop[i][j] is index of the next node
                  after i on a shortest path to j, or None if no path or path affected by negative cycle.
        negative_cycle_nodes: set of node indices that are on or affected by negative cycles.
    """
    # 1) collect nodes and create index mapping
    nodes_set = set()
    edges_list = list(edges)
    for u, v, _w in edges_list:
        nodes_set.add(u); nodes_set.add(v)
    nodes = list(nodes_set)
    n = len(nodes)
    idx = {node: i for i, node in enumerate(nodes)}

    # 2) initialize distance and next matrices
    dist: List[List[float]] = [[INF]*n for _ in range(n)]
    next_hop: List[List[Optional[int]]] = [[None]*n for _ in range(n)]

    # distance to self is 0
    for i in range(n):
        dist[i][i] = 0.0
        next_hop[i][i] = i

    # fill direct edges (keep smallest weight if multiple edges)
    for u, v, w in edges_list:
        i, j = idx[u], idx[v]
        if w < dist[i][j]:
            dist[i][j] = w
            next_hop[i][j] = j

    # 3) core triple loop
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] == INF:
                    continue
                new_dist = dist[i][k] + dist[k][j]
                if new_dist < dist[i][j]:
                    dist[i][j] = new_dist
                    next_hop[i][j] = next_hop[i][k]

    # 4) detect and propagate negative cycles
    negative_cycle_nodes = set()
    for v in range(n):
        if dist[v][v] < 0:
            negative_cycle_nodes.add(v)

    # propagate -inf to any pair (i,j) that can go through a negative cycle node
    if negative_cycle_nodes:
        for k in negative_cycle_nodes:
            for i in range(n):
                if dist[i][k] == INF:
                    continue
                for j in range(n):
                    if dist[k][j] == INF:
                        continue
                    dist[i][j] = NEG_INF
                    next_hop[i][j] = None  # no well-defined path

    return nodes, dist, next_hop, negative_cycle_nodes


def reconstruct_path(nodes: List[Any], next_hop: List[List[Optional[int]]], src: Any, dst: Any):
    """
    Reconstruct the path from src to dst using the next_hop matrix.
    Returns an empty list if no path or path undefined due to negative cycle.
    """
    idx = {node: i for i, node in enumerate(nodes)}
    if src not in idx or dst not in idx:
        return []

    i, j = idx[src], idx[dst]
    if next_hop[i][j] is None:
        return []  # no path or affected by negative cycle

    path = [src]
    while i != j:
        i = next_hop[i][j]
        if i is None:
            return []  # safety: undefined
        path.append(nodes[i])
        # guard against accidental infinite loops:
        if len(path) > len(nodes) + 5:
            return []  # something went wrong

    return path


# Example usage
if __name__ == "__main__":
    edges = [
        ('A','B',3),
        ('A','C',8),
        ('B','C',2),
        ('C','A',4),
        ('B','D',5),
        ('D','E',-6),
        ('E','B',1)   # creates a negative cycle: B->D->E->B has total weight 0? (example)
    ]

    nodes, dist, next_hop, neg_nodes = floyd_warshall(edges)
    print("Nodes (index -> node):", nodes)
    print("Negative-cycle node indices:", neg_nodes)
    print("\nDistance matrix:")
    n = len(nodes)
    for i in range(n):
        row = []
        for j in range(n):
            d = dist[i][j]
            if d == INF:
                row.append("INF")
            elif d == NEG_INF:
                row.append("-INF")
            else:
                row.append(f"{d:.1f}")
        print(row)

    print("\nExample path A -> E:", reconstruct_path(nodes, next_hop, 'A', 'E'))
"""```

---

## Detailed code explanation (block-by-block)

**1) Node indexing**

* Floyd–Warshall naturally works on indices `0..n-1`. If input nodes are arbitrary hashable objects (strings, tuples), we map each node to an integer index (`idx`) and keep `nodes` list to convert back.

**2) Matrices**

* `dist[i][j]` holds the current best-known distance from `nodes[i]` to `nodes[j]`.

  * Initialize all to `INF`.
  * Set `dist[i][i] = 0.0`.
  * Fill in `dist[u][v] = weight` for each direct edge (keep smallest if multiple edges).
* `next_hop[i][j]` holds the **index** of the next vertex after `i` on a shortest path to `j`.

  * If there's a direct edge `i->j`, `next_hop[i][j] = j`.
  * If no path, `next_hop[i][j] = None`.
  * When updating via an intermediate `k`, we set `next_hop[i][j] = next_hop[i][k]`.

**3) Triple loop**

* For each `k` (allowed intermediate nodes `0..k`), for each `(i,j)` we check whether going `i -> k -> j` improves the `i -> j` distance:

  * if `dist[i][k] + dist[k][j] < dist[i][j]` then update `dist[i][j]` and set `next_hop[i][j] = next_hop[i][k]`.
* We skip updates when either `dist[i][k]` or `dist[k][j]` is `INF` to avoid overflow/incorrect arithmetic.

**4) Negative-cycle detection**

* If after the algorithm `dist[v][v] < 0` for some `v`, a negative cycle exists and is reachable from `v`.
* Pairs `(i,j)` that can pass through such a node `k` have undefined finite shortest distance (you can keep reducing cost by looping the negative cycle). We mark these distances as `-INF` (or handle differently depending on application) and set `next_hop[i][j] = None` to indicate no well-defined finite path.

**5) Path reconstruction**

* Use `next_hop` to walk from `src` to `dst`:

  * Start `i = idx[src]`. While `i != idx[dst]`: set `i = next_hop[i][dst]` and append `nodes[i]`.
  * If `next_hop[i][dst]` is `None` we return empty list (no path or negative-cycle affected).
* This reconstruction is `O(path_length)`.

---

## Use cases

* **All-pairs shortest paths** in small to medium graphs.
* **Graphs with negative edge weights** (but no negative cycles), e.g., certain economic models.
* Computing **reachability / transitive closure** (if you set weight 1 for edges and 0 on diagonal, iterating min-plus can compute reachability; Warshall algorithm is an adaptation).
* Useful in dynamic programming solutions where you need distances between all pairs for later composition (e.g., some routing, clustering, or network analysis tasks).
* **Pedagogical / prototyping**: easy to code and reason about.

---

## Practical tips & variants

* For **sparse graphs** and large `V`, prefer Johnson’s algorithm (Bellman–Ford once + `V` Dijkstra runs) which is usually faster in practice.
* For **only single-source** queries, use Dijkstra (if weights non-negative) or Bellman–Ford (if negatives).
* When implementing, watch for floating-point issues if weights are floats — comparisons with `INF` must be explicit.
* If you only need distances (not reconstructable paths), you can skip the `next_hop` matrix to save memory — still `O(V²)` space for distances.
* You can adapt Floyd–Warshall to compute other path properties (e.g., count of shortest paths, lexicographically smallest path) with extra bookkeeping.

---

If you want, I can:

* Produce a **copy-paste Word document** of this content, or
* Provide a **step-by-step trace** on a small graph you give me, showing matrix values after each `k` iteration, or
* Convert this code to use **0..n-1 integer-only nodes** for maximal speed.

"""
