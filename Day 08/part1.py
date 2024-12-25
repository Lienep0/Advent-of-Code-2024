from collections import defaultdict
from itertools import combinations

city = list()
nodes = defaultdict(list)

for i, line in enumerate(open("input.txt").readlines()):
    line = list(line.removesuffix("\n"))
    for j, node in enumerate(line):
        if node != ".":
            nodes[node].append((i, j))
    city.append(line)

def apply_antinodes(city, nodes):
    height, width = len(city), len(city[0])

    for node in nodes:
        for pos_1, pos_2 in combinations(nodes[node], 2):
            i_1, j_1 = pos_1
            i_2, j_2 = pos_2
            delta_i, delta_j = i_2 - i_1, j_2 - j_1

            antinode_1_i, antinode_1_j = i_1 - delta_i, j_1 - delta_j
            if not (antinode_1_i < 0 or antinode_1_i >= height or antinode_1_j < 0 or antinode_1_j >= width):
                city[antinode_1_i][antinode_1_j] = "#"

            antinode_2_i, antinode_2_j = i_2 + delta_i, j_2 + delta_j
            if not (antinode_2_i < 0 or antinode_2_i >= height or antinode_2_j < 0 or antinode_2_j >= width):
                city[antinode_2_i][antinode_2_j] = "#"

def count_antinodes(city):
    s = 0
    for line in city:
        for node in line:
            if node == "#":
                s += 1
    return s

apply_antinodes(city, nodes)
print(count_antinodes(city))