from functools import reduce
import re

width = 101
height = 103

class Robot():
    def __init__(self, y, x, vy, vx):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x = (self.x + self.vx) % height
        self.y = (self.y + self.vy) % width

robots = set()

for line in open("input.txt").readlines():
    robots.add(Robot(*(int(x) for x in re.findall(r'(-?\d+)', line))))

for _ in range(100):
    for robot in robots:
        robot.move()

quadrants = [0, 0, 0, 0]

h = height // 2
w = width // 2

for robot in robots:
    if robot.x != h and robot.y != w:
        quadrants[(robot.y > w) * 2 + (robot.x > h)] += 1

board = [[0 for _ in range(width)] for _ in range(height)]

for robot in robots:
    board[robot.x][robot.y] += 1

for i, line in enumerate(board):
    print(''.join([(str(x) if x != 0 else '.') if i != h and j != w else ' ' for j, x in enumerate(line)]))

print()
print(quadrants)
print(reduce(lambda x, y: x * y, quadrants, 1))