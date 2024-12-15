from PIL import Image
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

for i in range(1, 7688):
    for robot in robots:
        robot.move()

    filepath = f"Robots/image_{i}.png"

    board = [[0 for _ in range(width)] for _ in range(height)]

    for robot in robots:
        board[robot.x][robot.y] += 1

    img = Image.new("RGB", (width, height))

    for i in range(height):
        for j in range(width):
            if board[i][j] > 0:
                img.putpixel((j, i), (255, 255, 255))
            else:
                img.putpixel((j, i), (0, 0, 0))

    img.save(filepath)