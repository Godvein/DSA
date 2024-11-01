# Adjacency List
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
from collections import defaultdict

d = defaultdict(list)

for u, v in A:
    d[u].append(v)  # d[v].append(u) if undirected graph

print(d)

# Traversal DFS (Recursive)
def dfs_recursive(node):
    print(node)
    for node_nei in d[node]:
        if node_nei not in seen:
            seen.add(node_nei)
            dfs_recursive(node_nei)

source = 0
seen = set()
seen.add(source)
print("traversal dfs")
dfs_recursive(source)

# Iterative DFS
iterative_source = 0
iterative_seen = set()
iterative_seen.add(iterative_source)

def iterative_dfs(node):
    stk = [node]

    while stk:
        curr_node = stk.pop()
        print(curr_node)

        for node_nei in d[curr_node]:
            if node_nei not in iterative_seen:
                iterative_seen.add(node_nei)  # Corrected from `seen` to `iterative_seen`
                stk.append(node_nei)

print("Iterative DFS")
iterative_dfs(iterative_source)

# Big O Notation:

# 1. **Space Complexity**:
#    - For the adjacency list representation: O(V + E)
#      - Where V is the number of vertices (nodes) and E is the number of edges.
#    - For the recursive DFS: O(V) due to the recursion stack.
#    - For the iterative DFS: O(V) due to the stack used for storing nodes.

# 2. **Time Complexity**:
#    - For both recursive and iterative DFS: O(V + E)
#      - Each vertex is visited once, and each edge is examined once.
