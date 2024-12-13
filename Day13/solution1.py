from functools import cache


@cache
def computeCost(x, y, a, b, nx, ny):
    if x == 0 and y == 0:
        return 0

    if x < 0 or y < 0:
        return INF

    if nx == 0 and ny == 0:
        return INF

    if nx == 0:
        return 1 + computeCost(x - b[0], y - b[1], a, b, nx, ny - 1)

    if ny == 0:
        return 3 + computeCost(x - a[0], y - a[1], a, b, nx - 1, ny)

    if nx > 0 and ny > 0:
        return min(
            3 + computeCost(x - a[0], y - a[1], a, b, nx - 1, ny),
            1 + computeCost(x - b[0], y - b[1], a, b, nx, ny - 1),
        )


INF = 10000000000

machines = []
currentMachine = [0, 0, 0]
with open("./input.txt") as f:
    for l in f:
        if l.startswith("Button A"):
            l = l.strip().split(" ")
            x = int(l[2][2:][:-1])
            y = int(l[3][2:])
            currentMachine[0] = (x, y)

        elif l.startswith("Button B"):
            l = l.strip().split(" ")
            x = int(l[2][2:][:-1])
            y = int(l[3][2:])
            currentMachine[1] = (x, y)

        elif l.startswith("Prize"):
            l = l.strip().split(" ")
            x = int(l[1][2:][:-1])
            y = int(l[2][2:])
            currentMachine[2] = (x, y)
        elif l == "\n":
            machines.append(currentMachine)
            currentMachine = [0, 0, 0]

cost = 0
for machine in machines:
    c = computeCost(machine[2][0], machine[2][1], machine[0], machine[1], 100, 100)
    if c < INF:
        cost += c
print(cost)
