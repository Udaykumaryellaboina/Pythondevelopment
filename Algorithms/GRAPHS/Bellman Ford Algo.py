# Bellman–Ford Algorithm — Explanation + Python implementation (copy-paste friendly)

## Short summary
"""
Bellman–Ford computes **single-source shortest paths** in a graph that **may have negative edge weights**. 
It also **detects negative-weight cycles** reachable from the source (which make shortest paths undefined).
 The algorithm relaxes all edges repeatedly (|V|−1 times), and then makes one extra pass to check for further
   relaxations (which indicate negative cycles).

---

## Why it’s used

* It works when edge weights can be **negative** (Dijkstra cannot handle negative weights).
* It **detects negative cycles** reachable from the source and can report which nodes are affected.
* It’s simple and works for both **directed** and **undirected** graphs (treat undirected edges as two 
directed edges).

---

## When to use (vs alternatives)

* **Use Bellman–Ford** when: you need shortest paths and the graph may contain **negative edge weights**,
 or you need to detect negative cycles.
* **Use Dijkstra** when all weights are **non-negative** — it’s faster (`O(E log V)`).
* For **all pairs** shortest paths: consider **Johnson’s algorithm** (reweights edges using Bellman–Ford,
 then run Dijkstra from every vertex) or **Floyd–Warshall** for dense graphs.

---

## Time & space complexity

* **Time:** `O(V * E)` in the worst case (|V| vertices, |E| edges).
* **Space:** `O(V + E)` to store graph plus `O(V)` for `dist` / `prev` arrays/dicts.
  Bellman–Ford is significantly slower than Dijkstra for large graphs without negative weights, 
  but necessary when negatives exist.

---

## High-level algorithm

1. Initialize `dist[source] = 0` and `dist[other] = +∞`. `prev[node] = None`.
2. Repeat `V-1` times: for every edge `(u, v, w)`, if `dist[u] + w < dist[v]` then `dist[v] = dist[u] + w` 
and `prev[v] = u`.

   * Why V-1 passes? The longest simple path uses at most V-1 edges; after V-1 relaxations, any further 
   improvement indicates a negative cycle.
3. Do one more pass over edges. If any edge can still be relaxed, there is a **negative-weight cycle reachable
 from the source**. Mark nodes involved / affected.
4. (Optional) Propagate negative-cycle influence to all nodes reachable from those cycle nodes (their shortest
 path is undefined → `-∞` conceptually).

---

## Python implementation (robust, hashable node labels, negative-cycle reporting)

```python"""
from typing import Iterable, Tuple, Any, Dict, List, Set, Optional

def bellman_ford(edges: Iterable[Tuple[Any, Any, float]], source: Any):
    """
    Bellman-Ford shortest paths.

    Args:
        edges: iterable of (u, v, weight) for directed edges. For undirected edges,
               include both (u,v,w) and (v,u,w).
        source: source node (hashable).

    Returns:
        dist: dict node -> shortest distance from source (float('inf') if unreachable)
        prev: dict node -> predecessor on shortest path (None if no predecessor)
        negative_cycle_nodes: set of nodes that are part of or reachable from a negative cycle
                              (empty set if no negative cycle reachable from source).
    Notes:
        - If negative_cycle_nodes is non-empty, shortest paths to those nodes are undefined.
    """
    edges_list = list(edges)

    # Collect nodes (ensure source exists)
    nodes = set()
    for u, v, _w in edges_list:
        nodes.add(u); nodes.add(v)
    nodes.add(source)

    dist: Dict[Any, float] = {n: float('inf') for n in nodes}
    prev: Dict[Any, Optional[Any]] = {n: None for n in nodes}
    dist[source] = 0.0

    V = len(nodes)

    # Relax edges up to V-1 times
    for i in range(V - 1):
        updated = False
        for u, v, w in edges_list:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:
            # No change in this pass -> distances stabilized early
            break

    # Detect negative cycles: any edge that can still be relaxed indicates one
    neg_nodes: Set[Any] = set()
    for u, v, w in edges_list:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            # v can be reduced further -> v (and u) are affected by a negative cycle
            neg_nodes.add(v)
            neg_nodes.add(u)

    # Propagate negativity: nodes reachable from neg_nodes are also affected
    if neg_nodes:
        # Repeat propagation up to V times (enough to reach all)
        for _ in range(V):
            for u, v, w in edges_list:
                if u in neg_nodes and v not in neg_nodes:
                    neg_nodes.add(v)

    return dist, prev, neg_nodes


def reconstruct_path(prev: Dict[Any, Optional[Any]], source: Any, target: Any,
                     negative_cycle_nodes: Optional[Set[Any]] = None) -> List[Any]:
    """
    Reconstruct path from source to target using prev dict.
    Returns empty list if target unreachable or if target is affected by a negative cycle.
    """
    if negative_cycle_nodes and target in negative_cycle_nodes:
        # Path undefined when target is affected by negative cycle
        return []

    path = []
    node = target
    while node is not None:
        path.append(node)
        if node == source:
            break
        node = prev.get(node)
    path.reverse()
    if not path or path[0] != source:
        return []  # unreachable
    return path
"""```

---

## Detailed code explanation (line-by-line / block-by-block)

* **Collect nodes** — we build the `nodes` set from edges and ensure `source` is present. 
This lets the function work when nodes appear only as neighbors.

* **Initialization**:

  * `dist[n] = +∞` for all nodes, `dist[source] = 0`.
  * `prev[n] = None` will hold the predecessor for path reconstruction.

* **Relaxation loop (V-1 passes)**:

  * For each pass, iterate every edge `(u, v, w)`. If `dist[u]` is finite and `dist[u] + w < dist[v]`, 
update `dist[v]` and `prev[v] = u`.
  * Use an `updated` flag to break early if no changes occur on a full pass (speeds up many graphs).

* **Negative cycle detection**:

  * After V-1 passes, do one more pass through the edges. If any edge can still relax, a negative cycle 
is reachable from the source and influences some vertex.
  * We add both `u` and `v` to `neg_nodes` for safety (they are directly involved or next to the relaxing edge).
  * Then we **propagate**: repeatedly go over edges and add any vertex reachable from nodes in `neg_nodes`.
After up to V iterations, we've added all nodes reachable from those cycles. These nodes' shortest distances are undefined (conceptually `-∞`).

* **Return**:

  * `dist` and `prev` give computed shortest distances for nodes **not** affected by negative cycles.
  * `negative_cycle_nodes` lists every node for which a finite shortest path is **not** defined because it can be improved indefinitely via cycles.

* **Path reconstruction**:

  * If the `target` is unreachable (dist is +∞) or is affected by a negative cycle, return `[]`.
  * Otherwise follow `prev` pointers back to the source and reverse.

---

## Example 1 — graph without negative cycle

```python"""
edges = [
    ('A','B',6),
    ('A','D',6),
    ('B','C',5),
    ('C','D',1),
    ('D','E',-2),
    ('B','E',-1)
]

dist, prev, neg = bellman_ford(edges, 'A')
print("Distances:", dist)
print("Negative cycle nodes:", neg)
print("Path A -> E:", reconstruct_path(prev, 'A', 'E', neg))
"""and```

Expected outcome:

* Distances will be finite for reachable nodes (example: `A:0`, `B:6`, `C:11`, `D:10`, `E:9` or similar depending on edge ordering).
* `neg` is empty (no negative cycle).
* Path `A -> E` will be printed as a list like `['A', 'B', 'E']` if that is the shortest.

---

## Example 2 — graph with a negative cycle

```python"""
edges = [
    ('A','B',1),
    ('B','C',1),
    ('C','A',-3),   # cycle A->B->C->A has total weight -1
    ('C','D',2)
]

dist, prev, neg = bellman_ford(edges, 'A')
print("Distances:", dist)
print("Negative cycle nodes:", neg)
print("Path A -> D:", reconstruct_path(prev, 'A', 'D', neg))
"""

Expected outcome:

* `neg` will include `A`, `B`, `C` (and any nodes reachable from them).
* Distances for nodes in `neg` are unreliable (the algorithm may still show some numbers but
                                                they can be reduced without bound).
* `reconstruct_path` to `D` returns `[]` if `D` is affected by the negative cycle; otherwise
 if `D` is reachable only through the cycle it’s also affected.

---

## Use cases

* **Graphs with negative weights** (e.g., costs that can be negative).
* **Detecting negative cycles** — financial arbitrage detection (take `-log(rate)` and find negative cycles), 
protocol analysis.
* **Routing protocols** of distance-vector type (Bellman–Ford principles are used conceptually in e.g. RIP).
* **Preprocessing for Johnson’s algorithm** (Bellman–Ford is used to compute reweighting potentials to remove 
                                             negative weights, then run Dijkstra per node).

---

## Tips, pitfalls & variants

* Bellman–Ford is **slower** (`O(VE)`) than Dijkstra, so prefer Dijkstra when weights are non-negative.
* Always **check for negative weights**: if none exist, use Dijkstra for much faster performance.
* When detecting a negative cycle, you often want **the actual cycle** — retrieving the cycle requires
 a little more bookkeeping (e.g., when an edge relaxes in the final pass, follow `prev` pointers V steps to
find a node in the cycle and then output the cycle). The provided implementation
focuses on identifying affected nodes.
* For very large graphs where you need all-pairs shortest paths and negative edges exist, use **Johnson’s
 algorithm** (Bellman–Ford + many Dijkstras) for better performance than repeated Bellman–Ford.

"""
