densemap = open("input.txt").readline().removesuffix("\n")

map = []
map_blocks = []
empty_blocks = []
id = 0

for i, number in enumerate(densemap):
    n = int(number)

    if i % 2 == 1 :
        empty_blocks.append([id, n])
        for _ in range(n):
            id += 1
            map.append(".")

    else :
        map_blocks.append((id, n, i // 2))
        for _ in range(n):
            id += 1
            map.append(i // 2)

length = len(map)

def remap(map):
    for i in range(len(map_blocks) - 1, -1, -1):
        map_block_pos = map_blocks[i][0]
        map_block_size = map_blocks[i][1]
        map_block_number = map_blocks[i][2]

        for empty_block in empty_blocks:
            empty_block_pos = empty_block[0]
            empty_block_size = empty_block[1]

            if empty_block_size >= map_block_size and empty_block_pos < map_block_pos:
                for j in range(empty_block_pos, empty_block_pos + map_block_size):
                    map[map_block_pos + j - empty_block_pos] = "." # Digits being removed
                    map[j] = map_block_number # Empty spaces being filled

                empty_block[0] += map_block_size # Refresh empty block's position
                empty_block[1] -= map_block_size # Refresh empty block's size

                break

def checksum(map):
    s = 0
    for i in range(length):
        if map[i] != '.':
            s += map[i] * i
    return s

remap(map)
print(checksum(map))