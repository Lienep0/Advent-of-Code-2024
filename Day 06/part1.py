DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
board = [list(line.removesuffix("\n")) for line in open("input.txt").readlines()]
height = len(board)
width = len(board[0])

def find_startpos(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == "^":
                return (i, j)
            
def count_crosses(board):
    s = 0
    for row in board:
        for value in row:
            if value == "X":
                s += 1
    return s

def path(board, start):
    i, j = start
    direction = 0
    board[i][j] = "X"

    while True:
        i_dir, j_dir = DIRECTIONS[direction % 4]
        i += i_dir
        j += j_dir

        if not (i >= 0 and i < height and j >= 0 and j < width):
            return board

        elif board[i][j] == "#":
            direction += 1
            i -= i_dir
            j -= j_dir

        else :
            board[i][j] = "X"

new_board = path(board, find_startpos(board))
for line in new_board :
    print(''.join(line))

print(count_crosses(new_board))

# O(n)