equations = []

for line in open("input.txt").readlines():
    equation = line.split(":")
    equation[1] = equation[1].removeprefix(" ").removesuffix("\n").split(" ")
    equations.append((int(equation[0]), [int(x) for x in equation[1]]))

def solve_equation(value, subvalues, current, depth, maxdepth):
    new_plus = current + subvalues[depth]
    new_mult = current * subvalues[depth]

    if new_plus == value or new_mult == value:
        return value
    
    depth += 1
    if depth >= maxdepth:
        return 0
    
    return (solve_equation(value, subvalues, new_plus, depth, maxdepth) 
            or solve_equation(value, subvalues, new_mult, depth, maxdepth))

s = 0
for equation in equations:
    s += solve_equation(equation[0], equation[1], 0, 0, len(equation[1]))
print(s)