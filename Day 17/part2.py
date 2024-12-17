from part1 import run

goal = [0,3,5,4,3,0]
goal_lenght = len(goal)

a = 1
bestcount = 0

while True:
    output = run(a, 0, 0)

    count = 0
    for x, y in zip(output, goal):
        if x == y:
            count += 1
        else:
            break
    
    if count == goal_lenght and len(output) == len(goal):
        print(output, a)
        break
    elif count > bestcount:
        print(count, a)
        bestcount = count
        a *= 3
    else:
        a += 1

def compare(output):
    for i in range(len(output)):
        if output[i] != goal[i]:
            return i
    return True # Found a

def reca(curr_a, decision):
    for i in range(decision, 8):

    return compare(run(curr_a, )) 

# Need to backtrack on A using the fact that it's a base 8 number that gets divided by 3 each loop