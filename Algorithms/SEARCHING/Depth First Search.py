#🌳 What is DFS (Depth First Search)?
'''DFS is a graph traversal algorithm that starts from a source node
and explores as far as possible along each branch before backtracking.
It uses the stack data structure (either explicitly or via recursion) and is used in:
Solving mazes
Path finding
Topological sorting
Cycle detection
Solving puzzles (e.g., Sudoku)

📌 Key Concepts
Graph: A collection of nodes (vertices) connected by edges.
DFS works on both directed and undirected graphs.
DFS can be implemented using:
Recursion
Explicit stack'''

#🔁 DFS Process (Step-by-Step)
'''Start at a node (called source).
Mark the node as visited.
For each unvisited neighbor:
Recursively apply DFS.
Backtrack when no unvisited neighbor is left.

✅ DFS Pseudocode
🔹 Recursive DFS:

DFS(node):
    if node is not visited:
        mark node as visited
        for each neighbor of node:
            DFS(neighbor)
 '''

#🧠 DFS vs BFS (Key Differences)
'''Feature     	           DFS	                           BFS
Data Structure	      Stack / Recursion	Queue
Explores	          As deep as possible	           Level by level
Time Complexity	      O(V + E)	                         O(V + E)
Space Complexity	  O(V) (due to recursion/stack)	   O(V) (due to queue)
Use Case            Pathfinding, cycle detection	  Shortest path in unweighted graph
'''

#💻 DFS Code in Python
#1. Recursive DFS for Adjacency List Graph

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example graph (undirected)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
dfs(graph, 'A', visited)
# Output: A B D E F C (depending on graph structure)


#2. Iterative DFS using Stack

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Push neighbors in reverse to maintain order
            for neighbor in reversed(graph[node]):
                stack.append(neighbor)

dfs_iterative(graph, 'A')

#🔁 Time and Space Complexity
'''Let:
V = number of vertices
E = number of edges

Operation	Complexity
Time	O(V + E)
Space	O(V)

🧪 Applications of DFS
✅ Pathfinding in mazes
✅ Topological Sorting (in DAGs)
✅ Connected Components
✅ Cycle Detection in Graphs
✅ Solving puzzles (Sudoku, etc.)
✅ Web Crawlers (Explore all linked pages)

🧩 Real-world Analogy
Imagine a maze. DFS keeps going down one path until it can’t go any further,
 then backtracks and tries another. It's like exploring every hallway in depth before trying others.'''