import re

pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
matches = re.findall(pattern, open("input.txt").read())

s = 0
active = True
for match in matches:
    if match[2] == "do()":
        active = True
    elif match[3] == "don't()":
        active = False
    elif active :
        s += int(match[0]) * int(match[1])

print(s)