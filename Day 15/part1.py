directions_map = {"^" : (-1, 0), ">" : (0, 1), "v" : (1, 0), "<" : (0, -1)}
board = []
directions = ""

with open("input.txt", "r") as file:
    line = next(file)
    while line != "\n":
        board.append(list(line.strip()))
        line = next(file)
    for line in file:
        directions += line.strip()

for i, line in enumerate(board):
    for j, char in enumerate(line):
        if char == "@":
            bot_pos = [i, j]

def update_bot_pos(x, y):
    global bot_pos
    fx, fy = bot_pos
    board[fx][fy] = "."
    bot_pos = [x, y]
    board[x][y] = "@"

for arrow in directions:
    x, y = bot_pos
    dir_x, dir_y = directions_map[arrow]
    new_x, new_y = x + dir_x, y + dir_y

    match board[new_x][new_y]:
        case "#":
            pass
        case "O":
            while True:
                new_x += dir_x
                new_y += dir_y
                if board[new_x][new_y] != "O":
                    break

            match board[new_x][new_y]:
                case "#":
                    pass
                case _:
                    board[new_x][new_y] = "O"
                    update_bot_pos(x + dir_x, y + dir_y)
        case _:
            update_bot_pos(new_x, new_y)

s = 0
for i, line in enumerate(board):
    for j, char in enumerate(line):
        if char == "O":
            s += i * 100 + j

print(s)