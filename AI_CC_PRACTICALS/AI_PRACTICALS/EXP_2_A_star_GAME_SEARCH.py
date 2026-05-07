# Simple implementation of A* Algorithm

# Graph with cost values
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('G', 2)],
    'D': [],
    'E': [('G', 1)],
    'G': []
}

# Heuristic values (estimated distance to goal)
heuristic = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 1,
    'G': 0
}

"""
Time Complexity

Worst Case: O(E log V)

Where:
V = Number of vertices
E = Number of edges

Space Complexity : O(V)

Because nodes are stored in open list and visited list.
"""

def a_star(start, goal):

    # Open list stores nodes to visit
    open_list = [(start, 0)]

    # Store visited nodes
    visited = []

    while open_list:

        # Sort according to lowest cost
        open_list.sort(key=lambda x: x[1])

        # Select node with minimum cost
        current_node, current_cost = open_list.pop(0)

        # Skip if already visited
        if current_node in visited:
            continue

        # Print traversal
        print(current_node, end=" ")

        # Mark node as visited
        visited.append(current_node)

        # Goal condition
        if current_node == goal:
            print("\nGoal node found!")
            return

        # Explore neighbors
        for neighbor, cost in graph[current_node]:

            # f(n) = g(n) + h(n)
            total_cost = current_cost + cost + heuristic[neighbor]

            open_list.append((neighbor, total_cost))


# Main Program
print("A* Traversal Path:")
a_star('A', 'G')