directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
word = "MAS"

def search_position(board, i, j, direction, height, width, word):
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

def search_cross_position(board, i, j, height, width, word, middle):
    if (i < middle or i >= height - middle) or (j < middle or j >= width - middle):
        return False
    
    starts = [(i + a, j + b, d) for (a, b, d) in [(-middle, -middle, 7), (-middle, middle, 5), (middle, -middle, 2), (middle, middle, 0)] if board[i + a][j + b] == word[0]]

    if len(starts) < 2 :
        return False
    
    return search_position(board, *starts[0], height, width, word) and search_position(board, *starts[1], height, width, word)

def search_board(board, height, width, word):
    s = 0
    middle = int(len(word) / 2)

    for i in range(height):
        for j in range(width):
            if board[i][j] == word[middle]:
                if search_cross_position(board, i, j, height, width, word, middle):
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