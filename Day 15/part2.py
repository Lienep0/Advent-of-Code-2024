widening_map = {"#" : "##", "O": "[]", ".": "..", "@":"@."}
directions = ""
board = []

with open("input.txt", "r") as file:
    line = next(file)
    while line != "\n":
        board.append(sum([[y for y in widening_map[x]] for x in line.strip()], []))
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

def hpush(x, y, direction):
    global board
    dir_y = -1 if direction else 1
    new_y = y

    while True:
        new_y += dir_y
        new_obj = board[x][new_y]
        if new_obj != "[" and new_obj != "]":
            break
    
    match new_obj:
        case "#":
            pass
        case _:
            if direction: board[x][new_y:y - 1] = board[x][new_y + 1:y]
            else: board[x][y + 2:new_y + 1] = board[x][y + 1:new_y]
            update_bot_pos(x, y + dir_y)

def bot_vpush_seeker(x, y, dir_x, quality):
    # Quality indicates wether or not the bot sees "]" pieces, to avoid unnecessary recursion on verical stacks
    global board
    new_x = x + dir_x

    match board[new_x][y]:
        case "#":
            return False
        case "]":
            if not quality: return True
            else:
                return (bot_vpush_seeker(new_x, y - 1, dir_x, True)
                        and bot_vpush_seeker(new_x, y, dir_x, False))
        case "[":
            return (bot_vpush_seeker(new_x, y, dir_x, True)
                    and bot_vpush_seeker(new_x, y + 1, dir_x, False))
        case _:
            return True
        
def bot_vpush_pusher(x, y, dir_x, right):
    # Right indictes wether the bot is on a "[" piece
    global board
    new_x = x + dir_x

    match board[new_x][y]:
        case "]":
            bot_vpush_pusher(new_x, y - 1, dir_x, True)
            bot_vpush_pusher(new_x, y, dir_x, False)
        case "[":
            bot_vpush_pusher(new_x, y, dir_x, True)
            bot_vpush_pusher(new_x, y + 1, dir_x, False)
        case _:
            pass
    
    board[new_x][y] = ("[" if right else "]")
    board[x][y] = "."

def vpush(x, y, direction):
    dir_x = -1 if direction else 1
    new_x = x + dir_x

    match board[new_x][y]:
        case "#":
            return
        case ".":
            update_bot_pos(new_x, y)
        case _:
            if bot_vpush_seeker(x, y, dir_x, True):

                if board[new_x][y] == "]":
                    bot_vpush_pusher(new_x, y - 1, dir_x, True)
                    bot_vpush_pusher(new_x, y, dir_x, False)
                else:
                    bot_vpush_pusher(new_x, y, dir_x, True)
                    bot_vpush_pusher(new_x, y + 1, dir_x, False)

                update_bot_pos(new_x, y)

for arrow in directions:
    match arrow:
        case "^": vpush(*bot_pos, True)
        case "<": hpush(*bot_pos, True)
        case "v": vpush(*bot_pos, False)
        case ">": hpush(*bot_pos, False)
    
s = 0
for i, line in enumerate(board):
    enum = enumerate(line)
    for j, char in enum:
        if char == "[":
            s+= i * 100 + j
            next(enum)

print(f"GPS score: {s}")