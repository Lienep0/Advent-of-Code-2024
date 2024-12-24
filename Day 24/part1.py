from itertools import takewhile
from collections import deque, defaultdict

class Formula:
    def __init__(self, x, operator, y, result):
        self.x = x
        self.y = y
        self.operator = operator
        self.result = result

    def evaluate(self):
        match self.operator:
            case "OR":
                try: 
                    x = valuations[self.x]
                    if x != 1:
                        raise KeyError
                    else:
                        return 1
                except KeyError:
                    try: 
                        return valuations[self.y]
                    except KeyError:
                        raise "Not enough set variables"
                
            case "AND":
                return valuations[self.x] and valuations[self.y]
            
            case "XOR":
                return valuations[self.x] ^ valuations[self.y]
                
valuations = {}
formulas = []
free = deque()
dependencies = defaultdict(list)

def free_check(formula):
    if len([v for v in (formula.x, formula.y) if v not in valuations]) == 0:
        free.append(formula)

with open("input.txt", "r") as file:
    for line in takewhile(lambda line: line != "\n", file):
        x, y = line.split(": ")
        valuations[x] = int(y)
    for i, line in enumerate(file):
        x, operator, y, _, result = line.strip().split(" ")
        formula = Formula(x, operator, y, result)
        free_check(formula)
        formulas.append(formula)
        dependencies[x].append(i)
        dependencies[y].append(i)

while len(free) > 0:
    f = free.popleft()
    valuations[f.result] = f.evaluate()
    for formula_index in dependencies[f.result]:
        free_check(formulas[formula_index])

# Bruh
print(int(''.join(map(str, [v for _, v in reversed(sorted([(k, v) for (k, v) in valuations.items() if k[0] == "z"], key = lambda x: x[0]))])), 2))