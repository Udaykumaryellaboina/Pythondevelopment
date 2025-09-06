# Lee’s algorithm — explanation + Python implementation (copy-paste friendly)

## Short summary

Lee’s algorithm is **BFS on a grid** used to find the **shortest path (in number of steps)** from a start cell to a goal cell in an unweighted grid/maze where some cells are blocked. It guarantees the shortest path (by steps) because BFS explores cells in increasing distance order.

---

# Why it’s used

* It finds the **shortest path** on a discrete grid/maze (when all moves cost the same).
* It’s conceptually simple and easy to implement with a queue (`deque`).
* It works for pathfinding in mazes, routing on grids, board games, robotics discretized maps, and many grid-based problems in programming contests.

---

# When to use / Limitations

* **Use Lee** when the grid is unweighted (every move has equal cost) and you need the shortest number-of-steps path.
* **Do not use** Lee when edges have different weights — then use Dijkstra (or 0-1 BFS for weights 0/1).
* For huge grids with memory constraints, you may need memory-optimized variants or external storage.

---

# Time & Space Complexity

Let `R` = number of rows, `C` = number of columns, `N = R * C`.

* **Time:** `O(N)` worst-case — each cell is enqueued/visited at most once and each neighbor check is constant-time.
* **Space:** `O(N)` for `dist`/`visited`/`parent` arrays and for the queue in the worst case.

---

# High-level idea

1. Use a queue (BFS) starting from the seed cell.
2. Mark visited and record parent/distance for each neighbor you push into the queue.
3. When you first reach the goal, you have the shortest path — reconstruct it using parent pointers.
4. If the queue empties without reaching the goal, there is no path.

---

# Python implementation (4-directional with optional 8-direction mode)

```python
from collections import deque
from typing import List, Tuple, Optional

Coord = Tuple[int, int]

def lee_shortest_path(
    grid: List[List[int]],
    start: Coord,
    goal: Coord,
    allow_diagonal: bool = False
) -> Tuple[List[Coord], int]:
    """
    Find shortest path (list of (r,c) coords) from start to goal on a grid using Lee's algorithm (BFS).
    grid: 2D list where 0 = free cell, 1 = blocked cell (change as needed).
    start, goal: (row, col) 0-based coordinates.
    allow_diagonal: if True, allows 8-directional moves (including diagonals).
    Returns: (path, steps) where path is list of coords from start to goal inclusive,
             and steps is number of moves (len(path)-1). If unreachable, returns ([], -1).
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    sr, sc = start
    gr, gc = goal

    # Basic validation
    if not (0 <= sr < rows and 0 <= sc < cols):
        raise ValueError("start out of bounds")
    if not (0 <= gr < rows and 0 <= gc < cols):
        raise ValueError("goal out of bounds")
    if grid[sr][sc] != 0 or grid[gr][gc] != 0:
        # blocked start or goal
        return [], -1

    if start == goal:
        return [start], 0

    # Directions: 4-neighborhood by default; add diagonals if requested
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    if allow_diagonal:
        dirs += [(1,1), (1,-1), (-1,1), (-1,-1)]

    # Distance array initialized to -1 (unvisited)
    dist = [[-1] * cols for _ in range(rows)]
    parent: List[List[Optional[Coord]]] = [[None] * cols for _ in range(rows)]

    q = deque()
    q.append((sr, sc))
    dist[sr][sc] = 0
    parent[sr][sc] = None  # start has no parent

    while q:
        r, c = q.popleft()
        # Explore neighbors
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # bounds check
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue
            # only step into free and unvisited cells
            if grid[nr][nc] == 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                parent[nr][nc] = (r, c)
                # If goal found we can reconstruct path early (optional speed-up)
                if (nr, nc) == (gr, gc):
                    return _reconstruct_path(parent, start, goal), dist[nr][nc]
                q.append((nr, nc))

    # goal not reached
    return [], -1


def _reconstruct_path(parent: List[List[Optional[Coord]]],
                      start: Coord, goal: Coord) -> List[Coord]:
    """Reconstruct path from start to goal using parent pointers (returns list of coords)."""
    path: List[Coord] = []
    cur = goal
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur[0]][cur[1]]
    path.reverse()
    # Verify that path starts with start (otherwise goal unreachable)
    if not path or path[0] != start:
        return []
    return path


# Example usage
if __name__ == "__main__":
    grid = [
        [0,0,0,0,1],
        [1,1,0,1,0],
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
    ]
    start = (0, 0)
    goal = (4, 4)
    path, steps = lee_shortest_path(grid, start, goal, allow_diagonal=False)
    print("Path:", path)
    print("Steps:", steps)
```

---

# Detailed code explanation (block-by-block)

**Validation & early returns**

* We check bounds and whether start/goal are blocked. If start==goal we return immediately with a 0-step path.

**Directions**

* `dirs = [(1,0),(-1,0),(0,1),(0,-1)]` covers 4-neighborhood. If `allow_diagonal=True` we append the 4 diagonal directions.
* *Note:* when allowing diagonal moves, consider "corner cutting" — moving diagonally between two orthogonally blocked cells might be disallowed in some problems. You can add a check to prevent diagonal moves that pass through corners blocked on both orthogonal neighbors.

**dist and parent**

* `dist[r][c] == -1` means unvisited. When we visit a neighbor we set `dist[nr][nc] = dist[r][c] + 1`.
* `parent[nr][nc] = (r, c)` lets us reconstruct the path backward from the goal.

**BFS loop**

* `while q: r,c = q.popleft()`
* For each neighbor: check bounds and `grid[nr][nc] == 0` (free) and not yet visited.
* We mark `dist` & `parent` **when we enqueue** the neighbor (not when dequeuing). This avoids multiple enqueues of the same cell and ensures O(N) time.
* If the neighbor equals the goal, we reconstruct and return early. Otherwise we `append` the neighbor to the queue.

**Reconstruction**

* `_reconstruct_path` follows parent pointers from goal back to start, builds the reversed path, then reverses it. If path doesn't start at start, the goal was unreachable — return `[]`.

---

# Example (walkthrough)

Using the example grid in code:

* BFS will explore cells layer by layer (distance 0, then 1, then 2...).
* The first time we pop the goal (or discover it), the `dist` value is the shortest number of moves.
* `_reconstruct_path` will return the actual coordinates visited in the shortest path.

---

# Variants & useful adaptations

* **Multi-source BFS**: push multiple start coordinates into the initial queue with distance 0 to compute shortest distance from the nearest source (useful for fire spread, multi-start routing).
* **Distance map**: run BFS from a source (or multi-source) and return the whole `dist` matrix — gives shortest distance to every reachable cell.
* **Avoid corner-cutting** for diagonal moves: when moving diagonally `(dr,dc)` ensure at least one of the orthogonal neighbors is free (or ensure both are free) depending on problem rules.
* **Weighted grid**: if moves have different costs, use Dijkstra (priority queue) or 0-1 BFS for costs 0/1. Lee’s BFS is only for uniform-cost moves.
* **Memory optimization**: if you only need distances and not parents, skip parent array to halve memory. If you only need reachability, use boolean `visited` instead of `dist`.

---

# Practical tips & pitfalls

* **Mark visited on enqueue** (not on dequeue) — prevents pushing the same cell many times.
* **Check start/goal are free** before starting.
* For **very large grids**, ensure you don’t keep giant parent arrays if memory is constrained; consider reconstructing path differently or compressing parents.
* **Corner-cutting rules** matter for diagonal movement — clarify problem spec.
* **Use iterative BFS** rather than recursion to avoid recursion depth issues.

---

# Use cases

* Maze shortest path (classic maze solver).
* Grid-based path planning in robotics on occupancy grids (discrete maps).
* Game AI for grid movement (when cost is uniform).
* Nearest-signal/nearest-source calculations (multi-source BFS).
* Flood-fill-like distance propagation (distance transform with Manhattan metric).

---

If you want, I can:

* Give a version that forbids diagonal corner-cutting,
* Provide a multi-source BFS or a function that returns the full distance matrix, or
* Convert this into a Word-ready document or a step-by-step animated trace on a sample grid. Which would you like next?
