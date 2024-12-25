with open("input.txt", 'r') as file :
    list1 = []
    list2 = []
    i = 0
    for line in file :
        numbers = [int(x) for x in line.split()]
        list1.append(numbers[0])
        list2.append(numbers[1])
        i += 1

    sum = 0
    for j in range(i):
        n = list1[j]
        for k in range(i):
            if list2[k] == n :
                sum += n
        
    print(sum)

    # O(n^2)