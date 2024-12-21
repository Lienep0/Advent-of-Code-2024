with open("input.txt", "r") as file:
    patterns = next(file).strip().split(", ")
    next(file)
    designs = [line.strip() for line in file]

def design_backtrack(design, i):
    for pattern in patterns:
        if len(pattern) + i <= len(design):
            k = 0
            while k < len(pattern) and pattern[k] == design[i + k]:
                k += 1
            
            if k == len(pattern) and (i + k == len(design) or design_backtrack(design, i + len(pattern))):
                return True
            
    return False

def design_availability(design):
    return design_backtrack(design, 0)

print(sum([design_availability(design) for design in designs]))