# Import deque for queue implementation in BFS
from collections import deque


# Graph represented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

"""
Time Complexity
For both DFS and BFS:

O(V+E)

Where:

V = Number of Vertices
E = Number of Edges

Reason:

Every vertex is visited once
Every edge is checked once


Space Complexity : O(V)

Which algorithm gives shortest path?

BFS gives shortest path in unweighted graphs.

"""

# ---------------- DFS USING RECURSION ---------------- #

def dfs(graph, node, visited):
    
    # Mark current node as visited
    visited.add(node)

    # Print the node
    print(node, end=" ")

    # Visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

"""
Recursive DFS uses the system call stack internally
Iterative DFS uses a manual stack data structure
"""
# ---------------- DFS USING STACK ---------------- #

def dfs_using_stack(graph, start):

    # Stack for DFS
    stack = [start]

    # Set to store visited nodes
    visited = set()

    while stack:

        # Remove top element from stack
        node = stack.pop()

        # Visit only if not already visited
        if node not in visited:

            print(node, end=" ")

            # Mark node as visited
            visited.add(node)

            # Add neighbors to stack
            # reverse() helps maintain proper traversal order
            for neighbor in reversed(graph[node]):

                if neighbor not in visited:
                    stack.append(neighbor)


# ---------------- BFS USING QUEUE ---------------- #

def bfs(graph, start):

    # Set to store visited nodes
    visited = set()

    # Queue for BFS
    queue = deque()

    # Add starting node
    visited.add(start)
    queue.append(start)

    while queue:

        # Remove node from front of queue
        node = queue.popleft()

        # Print node
        print(node, end=" ")

        # Visit all neighbors
        for neighbor in graph[node]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# ---------------- MAIN PROGRAM ---------------- #

if __name__ == "__main__":
    
    print("Depth First Search Traversal:")
    visited_nodes = set()
    dfs(graph, 'A', visited_nodes)

    print("\n")

    print("Breadth First Search Traversal:")
    bfs(graph, 'A')