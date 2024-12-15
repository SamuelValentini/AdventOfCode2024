warehouse = []
instructions = []
isInstruction = False


def getRobotPosition(warehouse):
    for x, r in enumerate(warehouse):
        for y, e in enumerate(r):
            if e == "@":
                return x, y


def move(warehouse, rx, ry, dx, dy):
    if warehouse[rx + dx][ry + dy] == "#":
        return rx, ry
    elif warehouse[rx + dx][ry + dy] == ".":
        warehouse[rx + dx][ry + dy] = warehouse[rx][ry]
        warehouse[rx][ry] = "."
        return rx + dx, ry + dy
    elif warehouse[rx + dx][ry + dy] == "O":
        move(warehouse, rx + dx, ry + dy, dx, dy)
        if warehouse[rx + dx][ry + dy] == ".":
            warehouse[rx + dx][ry + dy] = warehouse[rx][ry]
            warehouse[rx][ry] = "."
            return rx + dx, ry + dy
        else:
            return rx, ry


with open("./input.txt") as f:
    for l in f:
        if l == "\n":
            isInstruction = True
        elif isInstruction:
            l = l.strip()
            instructions.append(l)
        else:
            l = [c for c in l.strip()]
            warehouse.append(l)
    instructions = "".join(instructions)


rx, ry = getRobotPosition(warehouse)

for i, instr in enumerate(instructions):
    if instr == ">":
        rx, ry = move(warehouse, rx, ry, 0, 1)
    if instr == "<":
        rx, ry = move(warehouse, rx, ry, 0, -1)
    if instr == "^":
        rx, ry = move(warehouse, rx, ry, -1, 0)
    if instr == "v":
        rx, ry = move(warehouse, rx, ry, 1, 0)


coordinates = 0
for i, r in enumerate(warehouse):
    for j, e in enumerate(r):
        if e == "O":
            coordinates += (i * 100) + j
print(coordinates)
