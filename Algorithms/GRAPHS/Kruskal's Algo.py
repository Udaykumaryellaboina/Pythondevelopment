# Kruskal’s algorithm — full explanation + Python implementation
""" Kruskal’s algorithm finds a **minimum spanning tree (MST)** of a connected,
 undirected, weighted graph. It’s a greedy algorithm that repeatedly picks the 
 smallest-weight edge that doesn’t create a cycle, until every vertex is connected 
 (or until no more safe edges exist, producing a minimum spanning **forest** for disconnected graphs).

---

# Why it’s used

* To build a lowest-cost set of connections that links all nodes (telecom, roads, electric grids).
* It’s conceptually simple and easy to implement when you can list all edges.
* Works well for **sparse** graphs (E much smaller than V²).
* Produces the global optimal MST thanks to the cut property / greedy correctness.

---

# When to use (vs alternatives)

* Use **Kruskal** when you have an edge list or the graph is sparse.
* Use **Prim** when you have adjacency lists and want to start from a vertex 
(Prim with a binary heap is good for many graphs; Prim with adjacency matrix can 
be O(V²) and better when graph is dense).
* If the graph is directed, MST is not defined — you’d need directed-arborescence
 algorithms (e.g., Edmonds’ algorithm).

---

# High-level algorithm

1. Sort all edges by weight (ascending).
2. Initialize a Disjoint Set Union (Union-Find) structure for vertices.
3. Iterate edges in ascending order; for each edge (u, v, w):

   * If `find(u) != find(v)`, include the edge and `union(u, v)`.
   * Else skip the edge (would form a cycle).
4. Stop when you have `V-1` edges (for a connected graph) or when edges are exhausted.

The resulting edges form an MST (or minimum spanning forest).

---

# Time & space complexity

* Sorting edges: `O(E log E)` (often written `O(E log V)` because `E ≤ V^2` and `log E = O(log V)`).
* Union-Find operations: each `find`/`union` is near-constant amortized — `O(α(V))` where
 `α` is inverse Ackermann (effectively constant).
* Total time: `O(E log E)` ≈ `O(E log V)`.
* Space: `O(E + V)` to store edges plus parent/rank arrays for Union-Find.

Kruskal performs especially well when `E` is small relative to `V^2` (sparse graphs).

---

# Union-Find (Disjoint Set) — brief

* Supports `find(x)` (which set is x in) and `union(x,y)` (merge sets).
* Optimizations: **path compression** (in `find`) and **union by rank/size** — give 
amortized near-constant time per op.
* Used to quickly test whether adding an edge will create a cycle.

---

# Code — clean Python implementation (generic node labels)

```python"""
from typing import Iterable, Tuple, List, Any

class UnionFind:
    """Union-Find with path compression and union by rank. Works with arbitrary hashable nodes."""
    def __init__(self, elements: Iterable[Any]):
        self.parent = {x: x for x in elements}
        self.rank = {x: 0 for x in elements}

    def find(self, x: Any) -> Any:
        """Find representative (with path compression)."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: Any, b: Any) -> bool:
        """Union sets of a and b. Return True if merged, False if already in same set."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        # union by rank
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True

def kruskal(edges: Iterable[Tuple[Any, Any, float]]) -> Tuple[List[Tuple[Any, Any, float]], float]:
    """
    edges: iterable of (u, v, weight). Graph is undirected. Node labels can be any hashable type.
    Returns (mst_edges, total_weight).
    If the input graph is disconnected, returns a minimum spanning forest (mst_edges < V-1).
    """
    # Collect vertices
    edges_list = list(edges)
    nodes = set()
    for u, v, _w in edges_list:
        nodes.add(u); nodes.add(v)

    # Sort edges by weight
    edges_list.sort(key=lambda e: e[2])

    uf = UnionFind(nodes)
    mst = []
    total_weight = 0.0

    for u, v, w in edges_list:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            # early stop for connected graph:
            if len(mst) == len(nodes) - 1:
                break

    return mst, total_weight

# Example / quick test:
if __name__ == "__main__":
    edges = [
        ('A','B',4),
        ('A','C',3),
        ('B','C',1),
        ('B','D',2),
        ('C','D',4),
        ('C','E',2),
        ('D','E',3),
    ]
    mst_edges, weight = kruskal(edges)
    print("MST edges:")
    for u, v, w in mst_edges:
        print(f"{u} - {v} : {w}")
    print("Total MST weight:", weight)
"""
---

# Detailed code explanation (walk-through)

1. **UnionFind class**

   * `__init__(elements)`: initializes `parent[x] = x` and `rank[x] = 0` for each node.
     Works with arbitrary hashable node labels (ints, strings, etc.).
   * `find(x)`: recursive find that compresses path (`self.parent[x] = self.find(parent)`),
     so subsequent finds are faster.
   * `union(a, b)`: finds root representatives; if same, returns `False` (edge would create a cycle).
     Otherwise merges by rank and returns `True`.

2. **kruskal(edges)**

   * `edges_list = list(edges)`: materialize edges so we can sort them; edges are tuples `(u, v, weight)`.
   * Build `nodes` set from edges — supports graphs where node set isn't separately provided.
   * `edges_list.sort(key=lambda e: e[2])`: sorts edges ascending by weight.
   * `uf = UnionFind(nodes)` sets up DSU.
   * Loop through sorted edges:

     * If `uf.union(u, v)` returns `True`, the edge was safe (didn’t make cycle) and is added to `mst`.
     * Add weight to `total_weight`.
     * Early-stop when we have `V-1` edges (connected MST) for efficiency.
   * Returns the `mst` list and `total_weight`. For disconnected graphs, you will get a minimum
     spanning forest.

3. **Example block**

   * Demonstrates usage and prints the MST edges and total weight.

---

# Example run (from code above)

For the sample graph edges, the program prints an MST like:

```
MST edges:
B - C : 1
B - D : 2
C - E : 2
A - C : 3
Total MST weight: 8.0
```

(Edge order in output depends on sorting ties and the order chosen; total weight is the key correctness.)

---

# Use cases

* Telecommunications / network layout (minimize cable cost).
* Road planning, utility distribution (power lines).
* Clustering (single-linkage hierarchical clustering uses MST).
* Image segmentation techniques (some algorithms use MST-based approaches).
* Producing baseline low-cost connection skeletons for more complex optimization.

---

# Tips, pitfalls & variants

* Kruskal expects an undirected weighted graph. For directed problems use different algorithms.
* If the graph is **disconnected**, Kruskal produces a **minimum spanning forest** — this may be 
desired or not.
* If you have a very large edge list that doesn’t fit in memory, you can externally sort the edges
 (external merge sort) and stream them to the Union-Find (still linear passes).
* For dense graphs, Prim (with a Fibonacci heap or using an adjacency matrix implementation) can 
be as good or better.
* Handle multiple edges between the same nodes (parallel edges): Kruskal naturally keeps the cheapest
 non-cycling one.
* Edge weights can be negative — Kruskal still works fine.
"""
