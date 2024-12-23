def run(a, b, c):
    P = 0
    output = []

    def combo(l):
        nonlocal a, b, c
        if l < 4: return l
        return [a, b, c][l - 4]

    def adv(l): # 0
        nonlocal a
        a = a // (2 ** combo(l))

    def bxl(l): # 1
        nonlocal b
        b = b ^ l

    def bst(l): # 2
        nonlocal b
        b = combo(l) % 8

    def jnz(l): # 3
        nonlocal a, P
        if a != 0:
            P = l - 2

    def bxc(_): # 4
        nonlocal b, c
        b = b ^ c

    def out(l): # 5
        nonlocal output
        output.append(combo(l) % 8)

    def bdv(l): # 6
        nonlocal a, b
        b = a // (2 ** combo(l))

    def cdv(l): # 7
        nonlocal a, c
        c = a // (2 ** combo(l))

    functions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

    while True:
        if P >= len(instructions) - 1:
            break

        functions[instructions[P]](instructions[P + 1])
        P += 2

    return output

if __name__ == "__main__":
    import re
    
    with open("input.txt", "r") as file:
        A, B, C = map(int, (re.search(r'\d+', line).group() for line in [next(file) for _ in range(3)]))
        next(file)
        instructions = [int(x) for x in re.search(r' .*', next(file)).group().strip().split(",")]

    print(run(A,B,C))