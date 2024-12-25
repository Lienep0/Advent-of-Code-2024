equations = []

for line in open("input.txt").readlines():
    equation = line.split(":")
    equation[1] = equation[1][1:-1].split(" ")
    equations.append((int(equation[0]), [int(x) for x in equation[1]]))

def solve_equation(value, subvalues, current, depth, maxdepth):
    if current > value:
        return False
    operand = subvalues[depth]

    new_plus = current + operand
    new_mult = current * operand
    new_concat = int(str(current) + str(operand))
    
    depth += 1
    if depth == maxdepth:
        return new_plus == value or new_mult == value or new_concat == value
    
    return (solve_equation(value, subvalues, new_plus, depth, maxdepth) 
            or solve_equation(value, subvalues, new_mult, depth, maxdepth)
            or solve_equation(value, subvalues, new_concat, depth, maxdepth))

s = 0
for equation in equations:
    s += equation[0] if solve_equation(equation[0], equation[1], 0, 0, len(equation[1])) else 0
print(s)