DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
board = [[x for x in line.removesuffix("\n")] for line in open("input.txt").readlines()]
marked = [[False for _ in line] for line in board]

height = len(board)
width = len(board[0])

def count_field(i, j, tile, area, perimeter):
    marked[i][j] = True
    area += 1

    for direction in DIRECTIONS:
        dir_i, dir_j = direction
        new_i, new_j = i + dir_i, j + dir_j

        if not (new_i < 0 or new_i >= height or new_j < 0 or new_j >= width):
            if board[new_i][new_j] == tile:
                if not marked[new_i][new_j]:
                    area, perimeter = count_field(new_i, new_j, tile, area, perimeter)
            else:
                perimeter += 1
        else:
            perimeter += 1

    return area, perimeter

def count_barriers(board):
    s = 0
    for i, line in enumerate(board):
        for j, tile in enumerate(line):
            if not marked[i][j]:
                area, perimeter = count_field(i, j, tile, 0, 0)
                s += area * perimeter
    return s

print(count_barriers(board))