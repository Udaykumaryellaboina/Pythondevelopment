# Dijkstra’s Algorithm — Explanation + Python implementation (copy-paste friendly)

## Short summary

"""Dijkstra’s algorithm computes the **shortest path distances** from a 
single source node to every other node in a graph with **non-negative edge weights**.
 It’s a greedy algorithm that repeatedly selects the currently closest (unsettled) node
   and relaxes its outgoing edges using a priority queue (min-heap).

---

## Why it’s used

* To find the cheapest/shortest route from one place to many places 
(single-source shortest paths) in networks with **non-negative** weights.
* It’s efficient and simple to implement with a binary heap.
* Widely used in routing, mapping, and any system that needs shortest-paths
 quickly on graphs with non-negative costs.

---

## When to use / limitations

* **Use Dijkstra** when:

  * Edge weights are **non-negative**.
  * You need shortest paths from a single source to all (or some) nodes.
  * Graphs can be directed or undirected.
* **Don’t use** Dijkstra if edges can have **negative weights** → use **Bellman–Ford**
 (or detect and fix negatives).
* For **multiple sources / all pairs** shortest paths, consider Floyd–Warshall (dense small graphs) 
or Johnson’s algorithm (sparse graphs).

---

## Time & space complexity

* With a binary heap (Python `heapq`) and adjacency list:

  * **Time:** `O((V + E) log V)` which is commonly written as **O(E log V)** for connected graphs 
  (each edge may cause a heap push, and each push/pop costs `O(log V)`).
  * **Space:** `O(V + E)` to store the graph (adjacency list) plus `O(V)` for distance/prev/heap.
* With a naive array (no heap): **O(V²)** time (better for dense graphs or small V).
* With a Fibonacci heap (rare in practice): **O(E + V log V)**.

---

## Python implementation (readable, robust — works for arbitrary hashable nodes)

```python"""
import heapq
from typing import Dict, List, Tuple, Any, Optional

def dijkstra(graph: Dict[Any, List[Tuple[Any, float]]], source: Any):
    """
    Single-source shortest paths using Dijkstra (non-negative weights).

    Args:
        graph: adjacency dict where graph[u] = list of (v, weight)
               (graph can be directed or undirected).
        source: starting node (must be present or at least referenced).

    Returns:
        dist: dict mapping node -> shortest distance from source (float('inf') if unreachable)
        prev: dict mapping node -> predecessor on shortest path (None if no predecessor)
    """
    # Collect all nodes (in case some appear only as neighbors)
    nodes = set(graph.keys())
    for nbrs in graph.values():
        for v, _w in nbrs:
            nodes.add(v)

    dist: Dict[Any, float] = {node: float('inf') for node in nodes}
    prev: Dict[Any, Optional[Any]] = {node: None for node in nodes}

    dist[source] = 0.0
    # heap of (distance_to_node, node)
    heap: List[Tuple[float, Any]] = [(0.0, source)]

    while heap:
        d_u, u = heapq.heappop(heap)
        # If we popped a stale (outdated) pair, skip it
        if d_u > dist[u]:
            continue

        # Relax neighbors
        for v, weight in graph.get(u, []):
            if weight < 0:
                raise ValueError("Dijkstra cannot handle negative edge weights")
            alt = d_u + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (alt, v))

    return dist, prev


def reconstruct_path(prev: Dict[Any, Optional[Any]], source: Any, target: Any) -> List[Any]:
    """Reconstruct shortest path from source to target using prev dict.
       Returns an empty list if target unreachable."""
    path = []
    node = target
    while node is not None:
        path.append(node)
        if node == source:
            break
        node = prev.get(node)
    path.reverse()
    if not path or path[0] != source:
        return []   # unreachable
    return path


# Example usage
if __name__ == "__main__":
    # Example directed graph (weights non-negative)
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 5), ('D', 10)],
        'C': [('E', 3)],
        'D': [('F', 11)],
        'E': [('D', 4)],
        # 'F': []  # optional: nodes can be included implicitly
    }

    dist, prev = dijkstra(graph, 'A')
    print("Distances from A:")
    for node in sorted(dist):
        print(f"  {node:>2}: {dist[node]}")

    # Reconstruct path A -> F
    path = reconstruct_path(prev, 'A', 'F')
    print("\nShortest path A -> F:", path)

    """
```

---

## Line-by-line / block-by-block explanation

1. **Graph representation**

   * `graph` is a dictionary keyed by node; each value is a list of `(neighbor, weight)` tuples.
   * This adjacency-list form is memory-efficient for sparse graphs.

2. **Preparing nodes & init**

   * We build a `nodes` set because sometimes nodes only appear as neighbors and may be missing as keys.
   * `dist[node] = float('inf')` initially meaning unknown/very large distance.
   * `prev[node] = None` will store the predecessor used to reconstruct the shortest path.

3. **Heap (priority queue)**

   * `heapq` holds `(distance_so_far, node)` tuples. The heap gives the next node with smallest 
   provisional distance.
   * We push the source with distance `0.0`.

4. **Main loop**

   * Pop the smallest-distance tuple `(d_u, u)`.
   * **Stale check**: If `d_u > dist[u]` skip — this entry is outdated because we already found 
   a shorter path to `u` and pushed a newer tuple.
   * For every neighbor `(v, weight)`:

     * Compute alternative distance `alt = d_u + weight`.
     * If `alt < dist[v]`, update `dist[v]` and set `prev[v] = u`. Push new `(alt, v)` onto the heap.
   * Repeat until heap empty (all reachable nodes settled).

5. **Path reconstruction**

   * Follow `prev` pointers from the target back to the source, reverse the list. If the path doesn't 
   start with the source, the target is unreachable.

6. **Negative weights**

   * Dijkstra assumes weights are non-negative. If a negative weight is encountered, raise error or use
     Bellman-Ford instead.

---

## Step-by-step (short trace on the example)

Given `graph` above and source `'A'`:

1. Init: `dist[A]=0`, others `inf`. Heap = `[(0,A)]`.
2. Pop `(0,A)`, relax B -> dist\[B]=4, prev\[B]=A; relax C -> dist\[C]=2, prev\[C]=A. Heap now `[(2,C),(4,B)]`.
3. Pop `(2,C)`, relax E -> dist\[E]=5, prev\[E]=C`. Heap now `\[(4,B),(5,E)]\`.
4. Pop `(4,B)`, relax D -> dist\[D]=14, prev\[D]=B`. Heap now `\[(5,E),(14,D)]\`.
5. Pop `(5,E)`, relax D -> alt=9 < 14, so dist\[D]=9, prev\[D]=E; push `(9,D)`. Heap `[(9,D),(14,D)]`.
6. Pop `(9,D)` (14,D is stale), relax F -> dist\[F]=20, prev\[F]=D\`.
7. Continue until heap empty. Final distances: A:0, B:4, C:2, E:5, D:9, F:20.

Reconstructing A->F gives `['A','C','E','D','F']`.

---

## Use cases

* **Map routing / navigation** (shortest driving/walking distances when costs non-negative).
* **Network routing** (shortest path in link-state protocols).
* **Game AI pathfinding** (often combined with heuristics → A\*).
* **Resource allocation / logistics** where costs are additive and non-negative.
* **Shortest cost in weighted directed graphs** (when all weights are non-negative).

---

## Variants & tips

* To find **shortest path to a single target** faster, stop the algorithm when the target node is popped 
from the heap (it’s then finalized).
* For **dense graphs** (E ≈ V²), the O(V²) array-based implementation can be faster in practice.
* For **all pairs** shortest paths:

  * Use **Floyd–Warshall** for small dense graphs.
  * Use **Johnson’s algorithm** (runs Dijkstra from each vertex with weight reweighting) for sparse graphs.
* For better theoretical bounds with many decrease-key operations, Fibonacci heaps give `O(E + V log V)`, but 
they are rarely used in production (complex).
* If you need integer weights and very fast performance, specialized algorithms (e.g., Dial’s algorithm / bucket
 queues) may be preferable.

"""
