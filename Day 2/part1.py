with open("input.txt", 'r') as file :
    sum = 0
    for line in file :
        data = [int(x) for x in line.split()]
        incr = data[1] > data[0]
        safe = True

        for i in range(len(data) - 1):
            diff = ((-1) ** (not incr)) * (data[i+1] - data[i]) # magie
            if diff < 1 or diff > 3 :
                safe = False
                break

        sum += safe

    print(sum)
    
# O(n)