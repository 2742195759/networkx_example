import networkx as nx
G = nx.Graph()
with open("graph.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        if not line : continue
        A, B = line.strip().split("-")
        A, B = int(A), int (B)
        G.add_edge(A, B)
print ("edge number", len(G.edges()))
print (G.edges())
print ("node connectivity:", nx.node_connectivity(G))
print ("edge connectivity:", nx.edge_connectivity(G))
