from itertools import combinations
from collections import defaultdict

adj = defaultdict(set)

with open("input.txt", "r") as file:
    for line in file:
        c1, c2 = line.strip().split("-")
        adj[c1].add(c2)
        adj[c2].add(c1)

def clique_check(subgraph):
    for n1, n2 in combinations(subgraph, 2):
        if n1 not in adj[n2] or n2 not in adj[n1]:
            return False
    return True

s = 0
triangles = combinations(adj.keys(), 3)
for triangle in triangles:
    if clique_check(triangle):
        for element in triangle:
            if element[0] == 't':
                s += 1
                break

print(s)