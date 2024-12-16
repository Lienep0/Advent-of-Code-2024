import heapq as hp

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, Right, Down, Left

lab = []
with open("input.txt", "r") as file:
    for line in file:
        lab.append(list(line.strip()))

startpos = (len(lab) - 2, 1)
endpos = (1, len(lab[0]) - 2)

bestscores = [[[float("inf")] * 4 for _ in line] for line in lab]
bestendscore = float("inf")

heap = []
hp.heappush(heap, (0, *startpos, 1))

while len(heap) > 0:
    score, i, j, og_dir = hp.heappop(heap)
    if not score > bestendscore:
        bestscores[i][j][og_dir] = score    
        if (i, j) == endpos:
            bestendscore = score

        for k, dir in enumerate(DIRECTIONS):
            if not (k == (og_dir + 2) % 4): # Can't turn backwards
                dir_i, dir_j = dir
                new_i, new_j = i + dir_i, j + dir_j

                match lab[new_i][new_j]:
                    case "#":
                        pass
                    case _:
                        if k == og_dir and bestscores[new_i][new_j][k] > score + 1:
                            hp.heappush(heap, (score + 1, new_i, new_j, k))
                        elif bestscores[new_i][new_j][k] > score + 1001:
                            hp.heappush(heap, (score + 1001, new_i, new_j, k))

print(bestendscore)