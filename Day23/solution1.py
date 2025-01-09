import networkx as nx

G = nx.Graph()
with open("input.txt") as f:
    for l in f:
        l = l.strip().split("-")
        G.add_edge(l[0], l[1])

count = 0
for cycle in nx.simple_cycles(G, 3):
    for computer in cycle:
        if computer.startswith("t"):
            count += 1
            break
print(count)
