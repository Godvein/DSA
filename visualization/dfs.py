# you need to have matplotlib and networkx installed before running 
# run this in your terminal

from matplotlib import pyplot as plt
import networkx as nx

edges = [
    (1, 2), (1, 3), (1, 4), 
    (2, 5), (2, 6), 
    (3, 7), (3, 8), 
    (4, 9), (4, 10), 
    (5, 11), 
    (6, 12), 
    (7, 10), (7, 11), 
    (8, 12), (8, 1), 
    (9, 6), (9, 12), 
    (10, 2)
]

G = nx.Graph()
G.add_edges_from(edges)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels  = True)

plt.show(block = False)

seen = set()
def dfs_iteration(graph, root):
    
    stk = [root]

    while stk:
        node = stk.pop()

        if node not in seen:
            seen.add(node)
            nx.draw_networkx_nodes(G, pos, [node], node_color= "orange")
            plt.pause(1)
            for neighbor in graph.neighbors(node):
                stk.append(neighbor)

    plt.show()

dfs_iteration(G, 1)
