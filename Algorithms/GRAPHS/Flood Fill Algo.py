# Flood Fill — explanation + Python implementations (copy-paste friendly)
# This file explains the Flood Fill algorithm and provides several Python implementations.
# Flood Fill is commonly used in image processing, games, and graph problems to fill a connected region.


# --- Short summary ---


# Flood Fill fills a connected region of a grid/image starting from a seed pixel with a new color/value.
# It replaces every cell reachable from the seed by moving along allowed neighbors (usually 4-directional: up, down, left, right — sometimes 8-directional including diagonals) that have the same original color.


# Think of the “paint bucket” tool in graphics editors.

---


# --- Why it’s used ---


# - To recolor a connected region of pixels (paint-bucket).
# - To label connected components in binary/segmented images (preprocessing for computer vision).
# - To detect area/region size and boundaries (game maps, flood-fill area checks).
# - As a building block in image processing, pathfinding, terrain generation, and graph connectivity tasks.

---


# --- When to use (vs alternatives) ---


# Use flood fill when you need to operate on all cells in a connected region reachable by equality of value/color.
# For small-to-moderate regions and grids, simple DFS/BFS implementations are fine.
# For very large images or performance-critical applications, use optimized variants (scanline flood fill, union-find labeling, or specialized image libraries that operate in C).
# If you need connected-component labeling over the whole image, use multi-pass algorithms or union-find approaches instead of repeated flood fill calls.

---


# --- Time & space complexity ---


# Let R = rows, C = cols, and N = R * C.


# - Time: O(K) where K is the number of cells visited (cells in the filled region). Worst-case K = N, so O(N).
# - Space: O(K) for recursion stack or queue/stack used to track frontier (worst-case O(N)).
# - Recursive implementations risk hitting recursion depth limits for large K; iterative (stack/queue) avoids that.

---


# --- Variants ---


# - Recursive DFS: very simple, but may overflow recursion stack on big regions.
# - Iterative BFS (queue): breadth-first filling; safe for deep regions.
# - Iterative DFS (stack): similar to recursive DFS but avoids recursion limits.
# - Scanline flood fill: faster in practice for large contiguous horizontal spans (fills whole scanlines); more code but fewer pushes/pops.
# - Union-Find: useful when labeling all components in the entire image (connected-component labeling).
# - Image-library methods: Pillow/OpenCV have optimized routines and are recommended for production.

---


# --- Correctness details / pitfalls ---


# - Early exit: if newColor == originalColor, do nothing — otherwise you will loop infinitely or keep processing.
# - Bounds checks: always ensure neighbor coordinates are inside the grid/image.
# - Marking visited: change color to newColor as soon as you visit/enqueue a cell to avoid revisiting duplicates.
# - Connectivity: 4-direction vs 8-direction determines which neighbors count as connected. Choose per problem.

---


# --- Implementations (clear, explained) ---


# 1) Simple recursive DFS (easy to read — watch recursion depth)

```python
def flood_fill_recursive(grid, sr, sc, new_color):
    # Recursive DFS implementation of flood fill
    """
    grid: list of lists, grid[r][c] is a color/value
    sr, sc: start row, col
    new_color: value to fill

    Modifies grid in-place and returns it.
    """

    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    orig = grid[sr][sc]  # Store the original color to be replaced


    # Early exit: nothing to do if the color is already the new color
    if orig == new_color:
        return grid

    def dfs(r, c):
        # Helper function for recursive DFS

        # Bounds check
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        # Only fill cells that have the original color
        if grid[r][c] != orig:
            return
        # Fill current cell
        grid[r][c] = new_color
        # Explore 4 neighbors (up, down, left, right)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return grid


# --- Line-by-line notes ---

"""* `orig = grid[sr][sc]` stores the color to replace.
* `if orig == new_color:` avoids infinite work when nothing should change.
* `dfs` checks bounds and whether the current cell still has the original color. If so, it sets it to `new_color` and recurses to neighbors.
* This visits each cell in the connected region exactly once (if no cycles of color change), but recursion depth equals the longest path in region — might overflow Python recursion for large regions.

---'"""


# 2) Iterative BFS (safer for deep/large regions; preferable)


from collections import deque

def flood_fill_bfs(grid, sr, sc, new_color):
    # Iterative BFS implementation of flood fill

    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    orig = grid[sr][sc]  # Store the original color


    if orig == new_color:
        return grid  # Early exit if already filled


    q = deque()
    q.append((sr, sc))
    # Mark visited by setting to new_color immediately to avoid re-adding
    grid[sr][sc] = new_color


    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):  # 4-connected neighbors
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == orig:
                grid[nr][nc] = new_color  # mark visited
                q.append((nr, nc))
    return grid


# Why mark on enqueue?
#Setting `grid[nr][nc] = new_color` when we enqueue prevents pushing the same cell multiple times (saves memory/time). You still visit each cell exactly once.



# 3) Iterative DFS (stack) — similar to BFS, sometimes faster

def flood_fill_stack(grid, sr, sc, new_color):
    # Iterative DFS implementation using a stack

    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    orig = grid[sr][sc]
    if orig == new_color:
        return grid
    stack = [(sr, sc)]
    grid[sr][sc] = new_color


    while stack:
        r, c = stack.pop()
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == orig:
                grid[nr][nc] = new_color
                stack.append((nr, nc))
    return grid



# 4) Flood fill on a Pillow image (practical image example)

# Requires: pip install pillow
from PIL import Image

def flood_fill_pil(img: Image.Image, x: int, y: int, new_color):
    # Flood fill for a Pillow image
    """
    img: PIL Image (mode 'RGB' or 'RGBA' or 'L', etc.)
    x, y: pixel coordinates (x horizontal, y vertical)
    new_color: tuple or int matching image mode, e.g. (255,0,0) for RGB
    Returns modified image (in-place).
    """

    pixels = img.load()
    w, h = img.size
    orig = pixels[x, y]  # Store the original pixel value


    if orig == new_color:
        return img  # Early exit if already filled


    stack = [(x, y)]
    pixels[x, y] = new_color


    while stack:
        cx, cy = stack.pop()
        for nx, ny in ((cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)):
            if 0 <= nx < w and 0 <= ny < h and pixels[nx, ny] == orig:
                pixels[nx, ny] = new_color
                stack.append((nx, ny))
    return img


# Notes

#* Pixel values may be tuples (`(R,G,B)`) or integers (grayscale). Use a `new_color` that matches the image mode.
#* Converting image to `RGBA` or `RGB` first can simplify handling.



# --- Example (grid) — quick demo ---


flood_fill_bfs(grid, 1, 1, 2)

# Example usage:
grid = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
flood_fill_bfs(grid, 1, 1, 2)
# result:
# [
#  [2,2,2],
#  [2,2,0],
#  [2,0,1]
# ]


# Seed (1,1) had value 1, so all connected 1’s reachable via 4-neighbor connectivity become 2.



# --- Practical tips & optimizations ---


# - Always early-exit if orig == new_color. This avoids altering the grid and avoids infinite loops.
# - Prefer iterative implementations for production to avoid recursion-depth issues.
# - Marking on enqueue (BFS) or on push (DFS stack) prevents duplicate pushes and reduces memory.
# - For large contiguous regions, implement scanline flood fill (fills horizontal segments and then checks above/below spans) — fewer push/pop operations and much faster in practice for large blocks.
# - For color images compare pixels exactly (tuples). If using floating colors, be careful with equality; consider thresholding.
# - For repeated labeling across the whole image, use a connected-component labeling algorithm (two-pass union-find) rather than many flood fills.



# --- Use cases (concise) ---


# - Paint/bucket fill in image editors.
# - Connected-component labeling for segmentation.
# - Region counting and area measurement (e.g., count lakes/patches in maps).
# - Game logic: reachable area, flood-fill puzzles, territory coloring.
# - Preprocessing for computer vision tasks (remove small islands, fill holes).
# - Simple mask-growing segmentation.



# --- When flood fill is NOT ideal ---


# - If you need to fill many independent regions across a huge image, a full connected-component labeling algorithm is more efficient.
# - When you need very fast low-level operations on large images — prefer OpenCV or Pillow routines implemented in C.
# - If you need to fill based on color similarity (not exact equality), use region-growing with thresholds or morphological methods instead.

