DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
board = [[x for x in line.removesuffix("\n")] for line in open("input.txt").readlines()]

new_board = [[0] * (len(board[0]) + 2) for _ in range(len(board) + 2)]
for i in range(len(board)):
    for j in range((len(board[0]))):
        new_board[i + 1][j + 1] = board[i][j]
board = new_board

marked = [[False for _ in line] for line in board]

def count_region(i, j, corners, area):
    marked[i][j] = True

    area += 1
    corners += count_corners(i, j)

    for direction in DIRECTIONS:
        dir_i, dir_j = direction
        new_i, new_j = i + dir_i, j + dir_j

        if board[new_i][new_j] == board[i][j]:
            if not marked[new_i][new_j]:
                marked[new_i][new_j] = True
                corners, area = count_region(new_i, new_j, corners, area)
    
    return corners, area
                
def count_corners(i, j):
    tile = board[i][j]
    neighbors = [[], 0]

    for direction in DIRECTIONS:
        dir_i, dir_j = direction
        new_i, new_j = i + dir_i, j + dir_j

        if board[new_i][new_j] == tile:
            neighbors[0].append(direction)
            neighbors[1] += 1

    neighbors_count = neighbors[1]
    neighbors = neighbors[0]

    def corner_check(n_0, n_1):
        n_0_i, n_0_j = n_0
        n_1_i, n_1_j = n_1
        return board[i + n_0_i + n_1_i][j + n_0_j + n_1_j] != tile
    
    match neighbors_count:
        case 0:
            # 1.2
            # .X.
            # 4.3 

            return 4
        case 1:
            # ..1
            # XX.
            # ..2 

            return 2
        case 2:
            n_0 = neighbors[0]
            n_1 = neighbors[1]

            # ...
            # XXX
            # ... 

            if abs(n_0[0]) == abs(n_1[0]):
                return 0
            
            # ..1
            # XX
            # ?X. 

            return 1 + corner_check(n_0, n_1)
        case 3:

            # ...
            # XXX
            # ?X? 

            top = [direction for direction in DIRECTIONS if direction not in neighbors][0]
            bottom = (-top[0], -top[1])
            neighbors = [neighbor for neighbor in neighbors if neighbor != bottom]

            return corner_check(neighbors[0], bottom) + corner_check(neighbors[1], bottom)
        case _:

            # ?X?
            # XXX
            # ?X? 

            return sum([corner_check(neighbors[i], neighbors[(i + 1) % len(neighbors)]) for i in range(len(neighbors))])
        
def count_barriers(board):
    s = 0
    for i in range(1, len(board) - 1):
        for j in range(1, len(board[i]) - 1):
            if not marked[i][j]:
                corners, area = count_region(i, j, 0, 0)
                s += area * corners
    return s

print(count_barriers(board))