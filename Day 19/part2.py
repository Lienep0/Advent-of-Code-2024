with open("input.txt", "r") as file:
    patterns = next(file).strip().split(", ")
    next(file)
    designs = [line.strip() for line in file]

memo = {}
sum = 0

def design_backtrack(design, i):
    global sum

    if (design, i) in memo:
        sum += memo[(design, i)]
    else:
        last_sum = sum

        for pattern in patterns:
            if len(pattern) + i <= len(design):
                k = 0
                while k < len(pattern) and pattern[k] == design[i + k]:
                    k += 1
                
                if k == len(pattern):
                    if i + k == len(design):
                        sum += 1
                    
                    else:
                        design_backtrack(design, i + len(pattern))

        memo[(design, i)] = sum - last_sum
    

def design_availability(design):
    design_backtrack(design, 0)

for design in designs:
    design_availability(design)
print(sum)