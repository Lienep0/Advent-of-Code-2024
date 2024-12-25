from collections import defaultdict
rules = defaultdict(list)

file = open("input.txt", "r")

def check_data(data, rules):
    for i in range(len(data)):
        for comparaison in rules[data[i]]:
            if comparaison in data[:i] :
                return 0
    
    return data[len(data) // 2]

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