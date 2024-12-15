warehouse = []
instructions = []
isInstruction = False


def getRobotPosition(warehouse):
    for x, r in enumerate(warehouse):
        for y, e in enumerate(r):
            if e == "@":
                return x, y


def isMovable(warehouse, rx, ry, dx, dy):
    if warehouse[rx + dx][ry + dy] == "#":
        return False
    elif warehouse[rx + dx][ry + dy] == ".":
        return True
    elif warehouse[rx + dx][ry + dy] == "[":
        if warehouse[rx][ry] == "]":
            return True
        else:
            return isMovable(warehouse, rx + dx, ry + dy, rx, ry) and isMovable(
                warehouse, rx + dx, ry + dy + 1, dx, dy
            )
    elif warehouse[rx + dx][ry + dy] == "]":
        if warehouse[rx][ry] == "[":
            return True
        else:
            return isMovable(warehouse, rx + dx, ry + dy, rx, ry) and isMovable(
                warehouse, rx + dx, ry + dy - 1, dx, dy
            )


def moveH(warehouse, rx, ry, direction):
    if warehouse[rx][ry + direction] == ".":
        warehouse[rx][ry + direction] = warehouse[rx][ry]
        warehouse[rx][ry] = "."

    elif warehouse[rx][ry + direction] == "[" or warehouse[rx][ry + direction] == "]":
        moveH(warehouse, rx, ry + direction * 2, direction)
        moveH(warehouse, rx, ry + direction, direction)
        warehouse[rx][ry + direction] = warehouse[rx][ry]
        warehouse[rx][ry] = "."


def moveV(warehouse, rx, ry, direction):
    if warehouse[rx + direction][ry] == ".":
        warehouse[rx + direction][ry] = warehouse[rx][ry]
        warehouse[rx][ry] = "."

    elif warehouse[rx + direction][ry] == "[":
        moveV(warehouse, rx + direction, ry, direction)
        moveV(warehouse, rx + direction, ry + 1, direction)
        warehouse[rx + direction][ry] = warehouse[rx][ry]
        warehouse[rx][ry] = "."
    elif warehouse[rx + direction][ry] == "]":
        moveV(warehouse, rx + direction, ry, direction)
        moveV(warehouse, rx + direction, ry - 1, direction)
        warehouse[rx + direction][ry] = warehouse[rx][ry]
        warehouse[rx][ry] = "."


def isMovableHorizontal(warehouse, rx, ry, direction):
    if warehouse[rx][ry + direction] == "#":
        return False
    elif warehouse[rx][ry + direction] == ".":
        return True
    elif warehouse[rx][ry + direction] == "[" or warehouse[rx][ry + direction] == "]":
        return isMovableHorizontal(warehouse, rx, ry + direction * 2, direction)


def isMovableVertically(warehouse, rx, ry, direction):
    print(warehouse[rx][ry])
    if warehouse[rx + direction][ry] == "#":
        return False
    elif warehouse[rx + direction][ry] == ".":
        return True
    elif warehouse[rx + direction][ry] == "[":
        return isMovableVertically(
            warehouse, rx + direction, ry, direction
        ) and isMovableVertically(warehouse, rx + direction, ry + 1, direction)
    elif warehouse[rx + direction][ry] == "]":
        return isMovableVertically(
            warehouse, rx, ry + direction, direction
        ) and isMovableVertically(warehouse, rx + direction, ry - 1, direction)


converter = {"#": "##", "O": "[]", ".": "..", "@": "@."}


def printStatus(move, warehouse):
    print(f"Move: {move}")
    for l in warehouse:
        print("".join(l))
    print()


with open("./test1.txt") as f:
    for l in f:
        if l == "\n":
            isInstruction = True
        elif isInstruction:
            l = l.strip()
            instructions.append(l)
        else:
            l = [x for c in l.strip() for x in converter[c]]
            warehouse.append(l)
    instructions = "".join(instructions)


rx, ry = getRobotPosition(warehouse)


def parseInstr():
    key = input()
    if key == "w":
        return "^"
    elif key == "a":
        return "<"
    elif key == "d":
        return ">"
    elif key == "s":
        return "v"
    else:
        return "n"


printStatus("", warehouse)
# for i, instr in enumerate(instructions):
while 1:
    instr = parseInstr()
    if instr == ">":
        if isMovableHorizontal(warehouse, rx, ry, 1):
            moveH(warehouse, rx, ry, 1)
    if instr == "<":
        if isMovableHorizontal(warehouse, rx, ry, -1):
            moveH(warehouse, rx, ry, -1)
    if instr == "^":
        if isMovableVertically(warehouse, rx, ry, -1):
            print("isMovableVertically")
            moveV(warehouse, rx, ry, -1)
    if instr == "v":
        if isMovableVertically(warehouse, rx, ry, 1):
            print("isMovableVertically")
            moveV(warehouse, rx, ry, 1)
    rx, ry = getRobotPosition(warehouse)
    printStatus(instr, warehouse)


coordinates = 0
for i, r in enumerate(warehouse):
    for j, e in enumerate(r):
        if e == "[":
            coordinates += (i * 100) + j
print(coordinates)
