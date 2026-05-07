# Dijkstra's Algorithm

"""
Time Complexity

O(V**2) 

Space Complexity

O(V)

"""

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Store shortest distances
distances = {}

# Initialize distances
for node in graph:
    distances[node] = float('inf')

# Distance of source node
distances['A'] = 0

visited = []

while len(visited) < len(graph):

    # Find minimum distance node
    min_node = None

    for node in graph:

        if node not in visited:

            if min_node is None or distances[node] < distances[min_node]:
                min_node = node

    # Mark node as visited
    visited.append(min_node)

    # Update distances
    for neighbor, weight in graph[min_node].items():

        new_distance = distances[min_node] + weight

        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance

# Print shortest distances
print("Shortest Distances from A:")

for node, distance in distances.items():
    print(node, ":", distance)