from collections import Counter

MAXX = 101
MAXY = 103


class Robot:
    def __init__(self, x, y, vx, vy) -> None:
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def __str__(self) -> str:
        return f"p = {self.x}, {self.y}. V = {self.vx}, {self.vy}"

    def updatePosition(self, maxX, maxY, steps):
        self.x = (self.x + self.vx * steps) % maxX
        self.y = (self.y + self.vy * steps) % maxY

    def getQuadrant(self, maxX, maxY):
        upX = maxX // 2
        upY = maxY // 2
        if self.x < upX and self.y < upY:
            return 1
        if self.x > upX and self.y < upY:
            return 2
        if self.x < upX and self.y > upY:
            return 3
        if self.x > upX and self.y > upY:
            return 4

        else:
            return -1


robots = []
with open("./input.txt") as f:
    for l in f:
        l = l.strip().split()
        p = l[0][2:].split(",")
        v = l[1][2:].split(",")
        r = Robot(int(p[0]), int(p[1]), int(v[0]), int(v[1]))
        robots.append(r)

for r in robots:
    r.updatePosition(MAXX, MAXY, 100)
    print(r)

result = Counter([r.getQuadrant(MAXX, MAXY) for r in robots])

safety = 1
for k in result:
    if k > 0:
        print(result[k])
        safety *= result[k]
print(safety)
