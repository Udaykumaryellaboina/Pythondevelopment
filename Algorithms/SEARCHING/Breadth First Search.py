#🔍 What is Breadth-First Search (BFS)?
'''BFS is a graph traversal algorithm. It starts at a starting node
(called the root in tree structures) and explores all the neighboring nodes at
the current depth before moving on to the nodes at the next depth level.

Think of it as:

🌊 Waves of exploration — first explore all close nodes, then go deeper step by step.
It works for:
Graphs (connected or disconnected)
Trees (BFS in trees = Level Order Traversal)

🧠 Core Concepts
🔗 Graph Terminology
Node (or Vertex): A point in the graph.
Edge: A connection between two nodes.
Neighbor: A node connected directly to another node.

🧰 BFS Needs:
Queue: To process nodes in "First In First Out" (FIFO) order.
Visited Set: To keep track of already visited nodes (avoid infinite loops).

🎯 BFS Strategy (Step-by-step)
Start from the source node.
Mark it as visited.
Put it in a queue.
While the queue is not empty:
Remove the node from the front.
For each unvisited neighbor, mark it as visited and add to the queue.

✍️ BFS Implementation in Python (from Scratch)
We’ll represent the graph as an adjacency list using a dictionary.

Example Graph:
mathematica
Copy
Edit
A -- B -- D
|    |
C    E
Adjacency list:


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}'''
from collections import deque  # for efficient queue

def bfs(graph, start_node):
    visited = set()            # To keep track of visited nodes
    queue = deque([start_node])  # Start with the starting node

    while queue:
        node = queue.popleft()  # Remove node from the front of the queue

        if node not in visited:
            print("Visited:", node)
            visited.add(node)   # Mark the node as visited

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
#Run the BFS:

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A'],
    'D': ['B'],
    'E': ['B']
}

bfs(graph, 'A')
'''Output:
Visited: A
Visited: B
Visited: C
Visited: D
Visited: E

🔁 How BFS Works (Trace)
Start at A, visit → Queue: ['B', 'C']

Visit B → Queue: ['C', 'D', 'E']

Visit C → Queue: ['D', 'E']

Visit D → Queue: ['E']

Visit E → Queue: [] (done!)

🧠 When to Use BFS?
✅ Find shortest path in unweighted graphs
✅ Level order traversal of trees
✅ Web crawling
✅ Social networking (shortest connection path)
✅ Maze solving

✅ Key Points Summary
Concept             	Description
Type	                 Traversal Algorithm
Data Structure	          Queue (FIFO)
Time Complexity	         O(V + E) → V: Vertices, E: Edges
Space Complexity	      O(V) for visited set and queue
Use Case	              Shortest path, Level order, Connectivity'''