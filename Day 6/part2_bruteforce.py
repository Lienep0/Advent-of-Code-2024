import copy
import time

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
board = [list(line.removesuffix("\n")) for line in open("input.txt").readlines()]
height = len(board)
width = len(board[0])

def print_board(board, path):
    for i in range(height):
        for j in range(width):
            if (i, j) in path : print("X", end = " ")
            elif board[i][j] == "#": print("#", end = " ")
            else: print(". ", end = "")
        print("")
    print("")

def find_startpos(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == "^":
                return (i, j)

def explore(board, start):
    visited = set()
    i, j = start
    direction = 0
    board[i][j] = 0

    while True:
        i_dir, j_dir = DIRECTIONS[direction]
        i += i_dir
        j += j_dir

        if not (i >= 0 and i < height and j >= 0 and j < width):
            break

        elif board[i][j] == "#":
            direction = (direction + 1) % 4
            i -= i_dir
            j -= j_dir

        else :
            visited.add((i, j))
    
    return visited

def check_for_loops(board, visited, start):
    loops = 0
    for block in visited:
        i_block, j_block = block
        loop_board = copy.deepcopy(board)
        loop_board[i_block][j_block] = "#"

        path = [start]
        i, j = start
        direction = 0
        while True:
            i_dir, j_dir = DIRECTIONS[direction]
            i += i_dir
            j += j_dir

            if not (i >= 0 and i < height and j >= 0 and j < width):
                break

            elif loop_board[i][j] == direction:
                loops += 1
                break

            elif loop_board[i][j] == "#":
                direction = (direction + 1) % 4
                i -= i_dir
                j -= j_dir

            else:
                path.append((i, j))
                loop_board[i][j] = direction
    
    return loops

top = time.perf_counter()

start = find_startpos(board)
visited = explore(board, start)
print(f"{check_for_loops(board, visited, start)} ways to stop the guard")

bottom = time.perf_counter()

print(f"Time spent : {bottom - top:.4} seconds")

# O(n^4)