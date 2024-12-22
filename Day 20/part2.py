import sys

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, Right, Down, Left

race, found, startpos = [], False, (-1, -1)
with open("input.txt", "r") as file:
    for i, line in enumerate(file):
        line = line.strip()
        for j, char in enumerate(line):
            if not found and char == "S":
                found, startpos = True, (i, j)
        race.append(line)

height = len(race)
width = len(race[0])
sys.setrecursionlimit(height * width)

grid_scores = [[0 for _ in line] for line in race]

max_distance = 20
cheatable_relative_nodes = {(x, y, abs(x) + abs(y)) for x in range(-max_distance, max_distance + 1) for y in range(-max_distance, max_distance + 1) if abs(x) + abs(y) <= max_distance}
cheats = []

def build_data(x, y, score, dir):
    grid_scores[x][y] = score

    if race[x][y] != "E":
        for i, j, dist in cheatable_relative_nodes:
            new_x, new_y = x + i, y + j
            if not (new_x < 0 or new_x >= height or new_y < 0 or new_y >= width) and race[new_x][new_y] != "#":
                cheats.append((score, new_x, new_y, dist))

        for k, direction in enumerate(DIRECTIONS):
            if k != dir:
                dir_x, dir_y = direction
                new_x, new_y = x + dir_x, y + dir_y

                match race[new_x][new_y]:
                    case "#":
                        pass
                    case _:
                        return build_data(new_x, new_y, score + 1, (k + 2) % 4)

build_data(*startpos, 0, -1)

cheat_scores = []
for cheat in cheats:
    score, new_x, new_y, dist = cheat
    cheat_scores.append(grid_scores[new_x][new_y] - score - dist)

print(len([cheat_score for cheat_score in cheat_scores if cheat_score >= 100]))