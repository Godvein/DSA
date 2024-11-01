n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

#Adjacency Matrix
M = []
for i in range(n):
    M.append([0] * n)

for u,v in A:
    M[u][v] = 1 #M[v][u] = 1 if undirected graph
print(M)

#Adjancency List
from collections import defaultdict

d = defaultdict(list)

for u,v in A:
    d[u].append(v)#d[v].append[u] if undirected graph

print(d)