densemap = open("input.txt").readline().removesuffix("\n")
map = []

id = 0
for number in densemap:
    char = "." if id % 2 == 1 else id // 2
    for _ in range(int(number)):
        map.append(char)
    id += 1

length = len(map)

def update_start_pointer(pos):
    for i in range(pos, length):
        if map[i] == "." : 
            return i

def update_end_pointer(pos):
    for i in range(pos - 1, -1, -1):
        if map[i] != "." : 
            return i

def remap(map):
    start_pointer = update_start_pointer(0)
    end_pointer = update_end_pointer(length)

    while start_pointer < end_pointer:
        map[start_pointer] = map[end_pointer]
        map[end_pointer] = "."
        start_pointer = update_start_pointer(start_pointer)
        end_pointer = update_end_pointer(end_pointer)

def checksum(map):
    s = 0
    i = 0
    while map[i] != ".":
        s += map[i] * i
        i += 1
    return s

remap(map)
print(checksum(map))