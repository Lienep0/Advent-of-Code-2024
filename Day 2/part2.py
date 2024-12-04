def checkforproblem(a, b, incr):
    diff = ((-1) ** (not incr)) * (b - a)
    return (diff < 1 or diff > 3)

def validlevel(data, incr, linenumber):
    problemcharge = True
    problemid = -1
    l = len(data)

    for i in range(l - 1):
        if checkforproblem(data[i], data[i + 1], incr) :
            if problemcharge :
                if i == l - 2 : # Only needed to remove last value
                    return True
                
                if i < l - 2 and checkforproblem(data[i], data[i + 2], incr) : # Removing creates a problem
                    return False
                else : # Removal sucessfull, skip ahead to normal data
                    problemid = i + 1
                    problemcharge = False
                    i += 2
            else :
                return False
            
    if problemid != -1 :
        st = str(data)
        open('positives.txt', 'a').write(st + (' ' * (40 - len(st))) + f" problem id : {problemid}, incr : {incr}, id : {linenumber}\n")
    return True

with open("input.txt", 'r') as file :
    open('positives.txt', 'w').write('')

    sum = 0
    j = 0
    for line in file :
        j += 1
        data = [int(x) for x in line.split()]
        if (validlevel(data, True, j) or validlevel(data, False, j)) :
            sum += 1

    print(sum)

# O(n)