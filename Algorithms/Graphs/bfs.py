# Adjacency List
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
from collections import defaultdict

# Create the adjacency list representation of the graph
d = defaultdict(list)

for u, v in A:
    d[u].append(v)  # d[v].append(u) if undirected graph

print(d)

# BFS Iterative Function
seen = set()
source = 0
seen.add(source)

from collections import deque

def bfs_iterative(node):
    q = deque()  # Use a deque to implement the queue for BFS
    q.append(node)

    while q:
        curr_node = q.popleft()  # Remove the front of the queue
        print(curr_node)
        for node_nei in d[curr_node]:  # Access the adjacency list
            if node_nei not in seen:
                seen.add(node_nei)  # Mark the neighbor as seen
                q.append(node_nei)  # Add the neighbor to the queue

# Call the BFS function
bfs_iterative(source)

# Big O Notation:

# 1. **Space Complexity**:
#    - For the adjacency list representation: O(V + E)
#      - Where V is the number of vertices (nodes) and E is the number of edges.
#    - For the BFS queue: O(V)
#      - The queue can hold at most all vertices in the worst-case scenario, especially in a dense graph.

# 2. **Time Complexity**:
#    - For BFS: O(V + E)
#      - Each vertex is visited once, and each edge is examined once during the traversal.
