# Kruskal's Algorithm

"""
| Feature        | Kruskal               | Dijkstra         |
| -------------- | --------------------- | ---------------- |
| Purpose        | Minimum Spanning Tree | Shortest Path    |
| Works On       | Edges                 | Vertices         |
| Greedy Choice  | Minimum edge          | Minimum distance |
| Cycles Allowed | No                    | Yes              |

Time Complexity

O(E log E)

Where:
E = Number of edges
Space Complexity

O(V)

Where:
V = Number of Vertices
"""

# List of edges: (weight, node1, node2)
edges = [
    (1, 'A', 'B'),
    (4, 'A', 'C'),
    (2, 'B', 'D'),
    (3, 'C', 'D')
]

# Sort edges according to weight
edges.sort()

parent = {}

# Function to find parent
def find(node):

    if parent[node] == node:
        return node

    return find(parent[node])


# Function to perform union
def union(node1, node2):

    root1 = find(node1)
    root2 = find(node2)

    parent[root2] = root1


# Initialize parent
nodes = ['A', 'B', 'C', 'D']

for node in nodes:
    parent[node] = node

mst = []

# Kruskal Algorithm
for weight, u, v in edges:

    if find(u) != find(v):

        union(u, v)

        mst.append((u, v, weight))

# Print MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)