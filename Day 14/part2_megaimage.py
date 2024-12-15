from PIL import Image
import re

width = 101
height = 103
p = width * height

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

img = Image.new("RGB", (p, p))
filepath = "Robots/megaimage.png"

for i in range(height):
    for j in range(width):
        for robot in robots:
            robot.move()
            k, l = robot.get_coordinates()
            img.putpixel((i * width + l, j * height + k), (255, 255, 255))

img.save(filepath)