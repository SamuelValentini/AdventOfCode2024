import networkx as nx

G = nx.Graph()
with open("input.txt") as f:
    for l in f:
        l = l.strip().split("-")
        G.add_edge(l[0], l[1])

maxClique = []
for clique in nx.find_cliques(G):
    if len(clique) > len(maxClique):
        maxClique = clique
print(",".join(sorted(maxClique)))
