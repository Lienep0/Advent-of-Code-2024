import heapq as hp

size = 71
board = [["." for _ in range(size)] for _ in range(size)]
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, Right, Down, Left

with open("input.txt", "r") as file:
    for _ in range(1024):
        x, y = (int(x) for x in next(file).split(","))
        board[y][x] = "#"

def h(x, y):
    return (size - x - 1) + (size - y - 1)

def reconstruct_path(startpos, endpos, board, parents):
    i = 0
    x, y = endpos

    while (x, y) != startpos:
        i += 1
        board[x][y] = "O"
        x, y = parents[x][y]

    board[x][y] = "O"
    return i

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
            return reconstruct_path(startpos, endpos, board, parents)
        
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

print(A_star((0, 0), (size - 1, size - 1), board, size))