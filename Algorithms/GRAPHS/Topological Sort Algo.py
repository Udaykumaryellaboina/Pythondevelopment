# Topological Sort — Explanation + Python implementations (copy-paste friendly)
"""
**Short summary**
Topological sort orders the vertices of a **directed acyclic graph (DAG)** so that for every directed edge `u → v`, `u` comes before `v` in the ordering. It's used whenever you must linearize tasks with dependencies (build systems, course prerequisites, job scheduling, etc.). Topological order exists **iff** the graph is a DAG.

---

**Two common algorithms**

1. **Kahn’s algorithm** (BFS / indegree) — iterative, easy to reason about, detects cycles by checking whether all nodes are output.
2. **DFS-based** (reverse postorder) — run DFS, push nodes after visiting all descendants, then reverse the result. Use a recursion stack or color-marking to detect cycles.

Both run in **O(V + E)** time and use **O(V + E)** space (adjacency list + helper arrays).

---

## Kahn’s algorithm (indegree / queue)

**Why it works**
Start from nodes with no incoming edges (indegree 0). Removing them removes outgoing edges and may create new indegree-0 nodes. Repeating this produces a valid order. If you cannot visit all nodes, a cycle exists.

**Python code (Kahn)**

```python"""
from collections import deque, defaultdict
from typing import Dict, List, Any, Tuple

def topo_kahn(edges: List[Tuple[Any, Any]]) -> List[Any]:
    """
    edges: list of (u, v) directed edges
    Returns topological order list (empty list if cycle detected).
    """
    # Build adjacency list and indegree map
    adj: Dict[Any, List[Any]] = defaultdict(list)
    indegree: Dict[Any, int] = defaultdict(int)
    nodes = set()
    for u, v in edges:
        nodes.add(u); nodes.add(v)
        adj[u].append(v)
        indegree[v] += 1
        indegree.setdefault(u, indegree.get(u, 0))  # ensure u present

    # Initialize queue with all indegree-0 nodes
    q = deque([n for n in nodes if indegree.get(n, 0) == 0])
    order: List[Any] = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    # If order doesn't contain all nodes, there's a cycle
    if len(order) != len(nodes):
        return []  # cycle detected
    return order

# Example:
# edges = [('A','C'), ('B','C'), ('C','D'), ('D','E')]
# topo_kahn(edges) -> e.g. ['A','B','C','D','E'] (A and B order may swap)

"""**Step-by-step trace (Kahn) on example `A->C, B->C, C->D`:**

* indegree: A:0, B:0, C:2, D:1
* queue init: \[A, B]
* pop A → order \[A], decrease indegree(C)=1
* pop B → order \[A,B], decrease indegree(C)=0 → push C
* pop C → order \[A,B,C], decrease indegree(D)=0 → push D
* pop D → order \[A,B,C,D] done.

---

## DFS-based algorithm (reverse postorder)

**Why it works**
A DFS finishes (postorder) a node only after all nodes reachable from it are finished. If you append nodes to a list when finishing them and then reverse that list, you get a topological order.

**Cycle detection**
Use a `visiting` set (recursion stack) or 3-color scheme (`0=unvisited,1=visiting,2=visited`). If you see a `visiting` node again, there's a back-edge → cycle.

**Python code (DFS)**

```python"""
from collections import defaultdict
from typing import Dict, List, Any, Tuple

def topo_dfs(edges: List[Tuple[Any, Any]]) -> List[Any]:
    """
    Returns topological order list, or [] if a cycle is detected.
    """
    adj: Dict[Any, List[Any]] = defaultdict(list)
    nodes = set()
    for u, v in edges:
        nodes.add(u); nodes.add(v)
        adj[u].append(v)

    visited: Dict[Any, int] = {n: 0 for n in nodes}  # 0=unvisited,1=visiting,2=visited
    order: List[Any] = []
    cycle_found = False

    def dfs(u: Any):
        nonlocal cycle_found
        if cycle_found:
            return
        visited[u] = 1  # visiting
        for v in adj[u]:
            if visited[v] == 0:
                dfs(v)
                if cycle_found:
                    return
            elif visited[v] == 1:
                # back-edge found -> cycle
                cycle_found = True
                return
        visited[u] = 2  # finished
        order.append(u)

    for n in nodes:
        if visited[n] == 0:
            dfs(n)
            if cycle_found:
                return []

    order.reverse()
    return order

# Example:
# edges = [('A','C'), ('B','C'), ('C','D')]
# topo_dfs(edges) -> ['A','B','C','D'] or ['B','A','C','D']
```"""

**Trace (DFS) on `A->C, B->C, C->D`:**

* Start A: dfs(A) → visit C → visit D → finish D (append), finish C (append), finish A (append) => partial order \[D,C,A]
* Start B: dfs(B) → reach C (already finished), finish B (append) => \[D,C,A,B]
* Reverse => \[B,A,C,D] (A and B may swap; both valid)

---

## Detecting cycles (explicit)

* **Kahn**: after algorithm, if produced order length < `|V|`, a cycle exists.
* **DFS**: detect back-edge during traversal (visited==1).

I gave both implementations returning `[]` when a cycle is present. If you want the actual cycle nodes/edges, I can add code to extract the cycle.

---

## Complexity

* **Time:** `O(V + E)` for both Kahn and DFS.

  * Building adjacency lists and indegree arrays: `O(E + V)`.
  * Each edge is considered exactly once when decreasing indegree (Kahn) or when exploring neighbors (DFS).
* **Space:** `O(V + E)` for adjacency + bookkeeping (indegree/visited/stack/order).

---

## When to use which algorithm

* **Kahn’s**:

  * Good when you prefer an iterative BFS-like solution.
  * Easy to stream or implement non-recursively.
  * Useful when you want to produce *any* topological order and also want trivial cycle detection.
* **DFS-based**:

  * Natural if you already use DFS for other graph analyses.
  * Slightly simpler to get reverse-postorder.
  * Beware recursion depth on very deep graphs (use iterative DFS or increase recursion limit for Python).

---

## Use cases

* **Build systems / compilation order** (source files with dependencies).
* **Task scheduling** (jobs with prerequisites).
* **Course prerequisite resolution** (a valid class order).
* **Package / dependency managers** (install order).
* **Data pipeline orchestration** (DAGs in workflow engines like Airflow).
* **Topological sorting of partial orders** in combinatorics, scheduling, and serialization.

---

## Practical notes & tips

* Graph must be **directed**; topological order doesn’t apply to undirected graphs (except trivial cases).
* If multiple valid orders exist, algorithms return one — Kahn’s result depends on queue order; DFS depends on node iteration order. If you need a *lexicographically smallest* topo order, push indegree-0 nodes into a min-heap (priority queue) instead of a plain queue.
* For very large graphs, prefer adjacency lists; avoid adjacency matrices.
* If you need to enumerate **all** topological sorts, that’s an exponential problem (use backtracking with indegree updates) — feasible only for very small graphs.

---

## All-in-one example (Kahn + detect cycle + lexicographic variant)

```python"""
import heapq
from collections import defaultdict
from typing import List, Tuple, Any

def topo_kahn_any(edges: List[Tuple[Any, Any]]):
    # standard Kahn
    return topo_kahn(edges)

def topo_kahn_lexicographic(edges: List[Tuple[str, str]]):
    # returns lexicographically smallest topological order (strings or comparable)
    adj = defaultdict(list)
    indeg = defaultdict(int)
    nodes = set()
    for u, v in edges:
        nodes.add(u); nodes.add(v)
        adj[u].append(v)
        indeg[v] += 1
        indeg.setdefault(u, indeg.get(u,0))

    heap = [n for n in nodes if indeg[n] == 0]
    heapq.heapify(heap)
    order = []
    while heap:
        u = heapq.heappop(heap)
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)
    return order if len(order) == len(nodes) else []  # empty => cycle

