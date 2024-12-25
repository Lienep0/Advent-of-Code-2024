directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
word = "XMAS"

def search_position(board, direction, i, j, height, width, word):
    i_direction, j_direction = directions[direction]

    for k in range(1, len(word)):
        new_i = i + i_direction * k
        new_j = j + j_direction * k

        if (new_i >= height) or (new_i < 0):
            return False
        if (new_j >= width) or (new_j < 0):
            return False
        
        if board[new_i][new_j] != word[k]:
            return False
    
    return True

def search_board(board, height, width, word):
    s = 0
    directions_length = len(directions)

    for i in range(height):
        for j in range(width):
            if board[i][j] == word[0]:
                for k in range(directions_length):
                    if search_position(board, k, i, j, height, width, word):
                        s += 1
    
    return s

with open("input.txt", "r") as file :
    board = []
    height = 0
    for line in file:
        board.append(line.removesuffix("\n"))
        height += 1
    width = len(board[0])
    
    print(search_board(board, height, width, word))