import networkx as nx

N = 5
M = 4
#    N
# . . . . . 
# . . . . .  M
# . . . . .
# . . . . .
direct = [[0,1], [1,0], [0, -1], [-1, 0]]
G = nx.Graph()
for i in range(N):
    for j in range(M):
        node = (i, j)
        for di in direct : 
            node_next = ((i+di[0]+N)%N, (j+di[1]+M)%M)
            G.add_edge(node, node_next)

number_edges = G.number_of_edges()
number_nodes = G.number_of_nodes()
print ("edges:", number_edges)
print ("nodes:", number_nodes)
print ("node connectivity:", nx.node_connectivity(G))
print ("edge connectivity:", nx.edge_connectivity(G))

T = nx.minimum_spanning_tree(G)
def calculate_leaf(Tree):
    ans = 0 
    root = 0
    for _ in Tree.degree:
        ans += int(_[1] == 1)
        if _[0] == (0,0): root = (int(_[1] == 1))
    return ans - root

number = 0
number += calculate_leaf(T)
print ("first:", number)
for _ in T.edges:
    G.remove_edge(*_)

T = nx.minimum_spanning_tree(G)
number += calculate_leaf(T)

print ("second:", number)
print ("total:", number + 2 * (number_edges - number_nodes + 1))

