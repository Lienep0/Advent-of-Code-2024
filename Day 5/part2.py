from collections import defaultdict
rules = defaultdict(list)

file = open("input.txt", "r")

def rebuild_data(data, rules):
    new_data = list(data)

    # Bit of a hack : Assume every list has an exact order where no elements can be placed freely
    for element in data:
        score = 0
        for constraint in rules[element]:
            if constraint in data:
                score += 1
        new_data[score] = element
    
    return new_data[len(data) // 2]

def check_data(data, rules):
    for i in range(len(data)):
        for comparaison in rules[data[i]]:
            if comparaison in data[:i] :
                return rebuild_data(data, rules)
    
    return 0

line = file.readline()
while line != "\n":
    rule = [int(x) for x in line.split('|')]
    rules[rule[0]].append(rule[1])
    line = file.readline()

s = 0
for line in file.readlines():
    data = [int(x) for x in line.split(",")]
    s += check_data(data, rules)

print(s)