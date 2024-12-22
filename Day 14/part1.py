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

    def move(self, iterations = 1):
        self.x = (self.x + self.vx * iterations) % height
        self.y = (self.y + self.vy * iterations) % width

robots = set()
for line in open("input.txt").readlines():
    robot = Robot(*(int(x) for x in re.findall(r'(-?\d+)', line)))
    robot.move(100)
    robots.add(robot)

quadrants = [0, 0, 0, 0]
h = height // 2
w = width // 2

for robot in robots:
    if robot.x != h and robot.y != w:
        quadrants[(robot.y > w) * 2 + (robot.x > h)] += 1

print(reduce(lambda x, y: x * y, quadrants, 1))