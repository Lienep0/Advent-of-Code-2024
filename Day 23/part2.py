from collections import defaultdict

adj = defaultdict(set)

with open("input.txt", "r") as file:
    for line in file:
        c1, c2 = line.strip().split("-")
        adj[c1].add(c2)
        adj[c2].add(c1)

maximal_cliques = []
def bron_kerbosch(r, p, x):
    if not p and not x:
        return maximal_cliques.append(r)
    
    u = next(iter(p | x))
    for v in p - adj[u]:
        bron_kerbosch(r | {v}, p & adj[v], x & adj[v])
        p = p - {v}
        x = x | {v}

bron_kerbosch(set(), set(adj.keys()), set())
print(','.join(sorted(list(max(maximal_cliques, key = len)))))