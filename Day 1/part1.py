with open("input.txt", 'r') as file :
    list1 = []
    list2 = []
    i = 0
    for line in file :
        numbers = [int(x) for x in line.split()]
        list1.append(numbers[0])
        list2.append(numbers[1])
        i += 1
    
    list1.sort()
    list2.sort()

    sum = 0
    for k in range(i):
        sum += abs(list1[k] - list2[k])
    print(sum)

    # O(nlogn) pour le tri