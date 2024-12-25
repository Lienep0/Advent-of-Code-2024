def checkforproblem(a, b, incr):
    diff = ((-1) ** (not incr)) * (b - a)
    return (diff < 1 or diff > 3)

def validlevel(data, incr, charge):
    problemcharge = charge
    l = len(data)

    for i in range(l - 1):
        if checkforproblem(data[i], data[i + 1], incr) :
            if problemcharge :
                return (validlevel(data[:i] + data[i + 1:], incr, False) # Try again without the values
                        or validlevel(data[:i + 1] + data[i + 2:], incr, False)) 
            else :
                return False
    return True

with open("input.txt", 'r') as file :
    sum = 0
    for line in file :
        data = [int(x) for x in line.split()]
        if (validlevel(data, True, True) or validlevel(data, False, True)) :
            sum += 1

    print(sum)

# O(n)