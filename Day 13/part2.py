import re

UNIT_ERROR = 10000000000000
equations = []

with open("input.txt") as file:
    while (line := file.readline().strip()):
        coefficients = []

        while line.startswith("Button"):
            coefficients.append([int(x) for x in re.findall(r'\+(\d*)', line)])
            line = file.readline().strip()

        targets = [int(x) + UNIT_ERROR for x in re.findall(r'=(\d+)', line)]

        equations.append([coefficients, targets])

        file.readline()

def PGCD(a, b):
    r = a
    while r != 0:
        r = a % b
        a = b
        b = r
    return a

def PPCM(a, b):
    return (a * b) // PGCD(a, b)

def solve_system(coefficients, targets):
    X, Y = targets

    a, c = coefficients[0][0], coefficients[0][1]
    b, d = coefficients[1][0], coefficients[1][1]

    ppcm = PPCM(a,c)

    coeff_l1 = ppcm // a
    coeff_l2 = ppcm // c

    y = (coeff_l2 * Y - coeff_l1 * X) / (d * coeff_l2 - b * coeff_l1)

    y = int(y)
    x = (X - b * y) // a

    return (x, y) if a * x + b * y == X and c * x + d * y == Y else (0, 0)

s = 0
for equation in equations:
    result = solve_system(equation[0], equation[1])
    s += result[0] * 3 + result[1] * 1

print(s)