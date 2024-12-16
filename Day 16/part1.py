DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, Right, Down, Left

lab = []
with open("easyinput.txt", "r") as file:
    for line in file:
        lab.append(list(line.strip()))

startpos = (len(lab) - 2, 1)
endpos = (1, len(lab[0]) - 2)

bestscores = [[[float("inf")] * 4 for _ in line] for line in lab]

heap = [(*startpos, 1, 0)]

while len(heap) > 0:
    i, j, og_dir, score = heap.pop()

    bestscores[i][j][og_dir] = score

    for k, dir in enumerate(DIRECTIONS):
        dir_i, dir_j = dir
        new_i, new_j = i + dir_i, j + dir_j

        match lab[new_i][new_j]:
            case "#":
                pass
            case _:
                if k == og_dir and bestscores[new_i][new_j][k] > score + 1:
                    heap.append((new_i, new_j, k, score + 1))
                elif bestscores[new_i][new_j][k] > score + 1001:
                    heap.append((new_i, new_j, k, score + 1001))

ei, ej = endpos
print(bestscores[ei][ej])