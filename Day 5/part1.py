from collections import defaultdict
rules = defaultdict(list)

file = open("input.txt", "r")

def check_data(data, rules):
    checked = []
    for element in data:
        for comparaison in rules[element]:
            if comparaison in checked :
                return 0
        checked.append(element)
    
    return data[len(data) // 2]

line = file.readline()
while line != "\n":
    numbers = [int(x) for x in line.split('|')]
    rules[numbers[0]].append(numbers[1])
    line = file.readline()

s = 0
for line in file.readlines():
    data = [int(x) for x in line.split(",")]
    s += check_data(data, rules)

print(s)