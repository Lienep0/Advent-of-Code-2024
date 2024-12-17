import re

with open("input.txt", "r") as file:
    A, B, C = map(int, (re.search(r'\d+', line).group() for line in [next(file) for _ in range(3)]))
    next(file)
    instructions = [int(x) for x in re.search(r' .*', next(file)).group().strip().split(",")]

print(f"A = {A}, B = {B}, C = {C}")
P = 0
output = []

def combo(c):
    if c < 4: return c
    return [A, B, C][c - 4]

def adv(c): # 0
    global A
    A = A // (2 ** combo(c))

def bxl(l): # 1
    global B
    B = B ^ l

def bst(c): # 2
    global B
    B = combo(c) % 8

def jnz(l): # 3
    if A != 0:
        global P
        P = l - 2

def bxc(_): # 4
    global B
    B = B ^ C

def out(c): # 5
    output.append(combo(c) % 8)

def bdv(c): # 6
    global B
    B = A // (2 ** combo(c))

def cdv(c): # 7
    global C
    C = A // (2 ** combo(c))

functions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

while True:
    if P >= len(instructions) - 1:
        break

    functions[instructions[P]](instructions[P + 1])
    P += 2

print(f"A = {A}, B = {B}, C = {C}")
print(instructions)

print(','.join(str(i) for i in output))