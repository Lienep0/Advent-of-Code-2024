from collections import deque
import heapq as hp

size = 71
board = [["." for _ in range(size)] for _ in range(size)]
bytepositions = deque()
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, Right, Down, Left

with open("input.txt", "r") as file:
    for line in file:
        bytepositions.append(int(x) for x in line.split(","))

def byte_fall():
    global bytepositions
    byte_x, byte_y = bytepositions.popleft()
    board[byte_x][byte_y] = "#"
    return byte_x, byte_y

def h(x, y):
    return (size - x - 1) + (size - y - 1)

def rebuild_path(startpos, endpos, parents):
    path = set()
    x, y = endpos

    while (x, y) != startpos :
        path.add((x, y))
        x, y = parents[x][y]

    path.add(startpos)
    return path

def A_star(startpos, endpos, board, size):
    start_x, start_y = startpos

    parents = [[(-1, -1) for _ in range(size)] for _ in range(size)]

    get_costs = [[float("inf") for _ in range(size)] for _ in range(size)]
    get_costs[start_x][start_y] = 0
    find_costs = [[float("inf") for _ in range(size)] for _ in range(size)]
    find_costs[start_x][start_y] = h(start_x, start_y)

    heap = []
    hp.heappush(heap, (find_costs[start_x][start_y], start_x, start_y))

    while len(heap) > 0:
        _, x, y = hp.heappop(heap)

        if (x, y) == endpos:
            return True, rebuild_path(startpos, endpos, parents)
        
        for direction in DIRECTIONS:
            dir_x, dir_y = direction
            new_x, new_y = x + dir_x, y + dir_y

            if not (new_x < 0 or new_x >= size or new_y < 0 or new_y >= size):
                match board[new_x][new_y]:
                    case "#":
                        pass
                    case ".":
                        tentative_score = get_costs[x][y] + 1

                        if tentative_score < get_costs[new_x][new_y]:
                            parents[new_x][new_y] = (x, y)
                            get_costs[new_x][new_y] = tentative_score
                            find_costs[new_x][new_y] = tentative_score + h(new_x, new_y)

                            if (new_x, new_y) not in heap:
                                hp.heappush(heap, (find_costs[new_x][new_y], new_x, new_y))

    return False, None

possible, path = A_star((0, 0), (size - 1, size - 1), board, size)

while possible:
    x, y = byte_fall()
    if (x, y) in path:
        possible, path = A_star((0, 0), (size - 1, size - 1), board, size)

print(x, y)