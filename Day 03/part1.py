import re

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

s = 0
matches = re.findall(pattern, open("input.txt").read())
s += sum([int(a) * int(b) for a, b in matches])

print(s)