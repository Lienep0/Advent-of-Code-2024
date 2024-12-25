from itertools import takewhile

def convert(schematic, reverse):
    data = []
    for column in schematic:
        i = -2 if reverse else 1
        while column[i] == "#":
            i += -1 if reverse else 1
        data.append(-i - 2 if reverse else i - 1)
    return tuple(data)

def matching(lock, key):
    for i in range(len(lock)):
        if lock[i] + key[i] > 5:
            return False
    return True

locks, keys = [], []
with open("input.txt", "r") as file:
    while True:
        schematic = [line.strip() for line in takewhile(lambda line: line != "\n", file)]
        if not schematic: break
        
        match schematic[0][0]:
            case "#": locks.append(convert(zip(*schematic), False))
            case ".": keys.append(convert(zip(*schematic), True))

s = 0
for lock in locks:
    for key in keys:
        s += matching(lock, key)
print(s)