DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
mountain = []

for line in open("input.txt").readlines():
    mountain.append([int(x) if x != "." else x for x in line.removesuffix("\n")])

length = len(mountain)
width = len(mountain[0])

def count_trailheads(mountain, i, j, height):
    if height == 9 : 
        return 1

    s = 0
    for direction in DIRECTIONS:
        dir_i, dir_j = direction
        new_i, new_j = i + dir_i, j + dir_j

        if not (new_i < 0 or new_i >= length or new_j < 0 or new_j >= width):
            new_height = height + 1
            if mountain[new_i][new_j] == new_height:
                s += count_trailheads(mountain, new_i, new_j, new_height)
    return s


s = 0

for i, line in enumerate(mountain):
    for j, height in enumerate(line):
        if height == 0:
            s += count_trailheads(mountain, i, j, height)

print(s)