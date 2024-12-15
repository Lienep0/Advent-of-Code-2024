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

    def get_coordinates(self):
        return (self.x, self.y)

robots = set()

for line in open("input.txt").readlines():
    robots.add(Robot(*(int(x) for x in re.findall(r'(-?\d+)', line))))

for i in range(1, 7688):
    img = Image.new("RGB", (width, height))

    for robot in robots:
        robot.move()
        k, l = robot.get_coordinates()
        img.putpixel((l, k), (255, 255, 255))

    img.save(f"Robots/image_{i}.png")