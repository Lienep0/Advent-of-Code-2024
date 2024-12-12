DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Up, right, down, left (clockwise)
WORDS = ["↑", "→", "↓", "←"]

board = [[0] + [x for x in line.removesuffix("\n")] + [0] for line in open("input.txt").readlines()]
board = [[0 for _ in range(len(board[0]))]] + board
board += [[0 for _ in range(len(board[0]))]]

marked = [[False for _ in line] for line in board]

def count_area(i, j, tile, area):
    marked[i][j] = True
    area += 1

    for direction in DIRECTIONS:
        dir_i, dir_j = direction
        new_i, new_j = i + dir_i, j + dir_j

        if board[new_i][new_j] == tile:
            if not marked[new_i][new_j]:
                area = count_area(new_i, new_j, tile, area)

    return area

# Could be written so much better, probably

def turn_right(looking_direction_counter):
    return (looking_direction_counter + 1) % 4

def turn_left(looking_direction_counter):
    return (looking_direction_counter - 1) % 4

def count_sides(i, j, tile):
    startpos = (i, j)
    sides = 0
    looking_direction_counter = 0
    
    while True:
        looking_dir_i, looking_dir_j = DIRECTIONS[looking_direction_counter]
        movement_dir_i, movement_dir_j = DIRECTIONS[(looking_direction_counter + 1) % 4]
        looking_new_i, looking_new_j = i + looking_dir_i, j + looking_dir_j
        movement_new_i, movement_new_j = i + movement_dir_i, j + movement_dir_j

        if board[looking_new_i][looking_new_j] == tile:

            i += looking_dir_i
            j += looking_dir_j
            looking_direction_counter = turn_left(looking_direction_counter)

            sides += 1
        elif board[movement_new_i][movement_new_j] != tile:

            looking_direction_counter = turn_right(looking_direction_counter)

            sides += 1
        else:
            i += movement_dir_i
            j += movement_dir_j
            
        if (i, j) == startpos and looking_direction_counter == 0:
            break
        
    return sides

def count_field(i, j, tile):
    area = count_area(i, j, tile, 0)
    sides = count_sides(i, j, tile)

    return area, sides

def count_barriers(board):
    s = 0
    for i in range(1, len(board) - 1):
        for j in range(1, len(board) - 1):
            if not marked[i][j]:
                area, sides = count_field(i, j, board[i][j])
                s += area * sides
    return s

print(count_barriers(board))