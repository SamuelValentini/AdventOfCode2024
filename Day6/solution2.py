UP = "^"
DOWN = "v"
RIGHT = ">"
LEFT = "<"

directions = [UP, RIGHT, DOWN, LEFT]

VISITED = "X"


def detectStartingPoint(m):
    for i, r in enumerate(m):
        for j, e in enumerate(r):
            if e == UP or e == DOWN or e == RIGHT or e == LEFT:
                return i, j


def detectDirection(directions, matrix, i, j):
    d = matrix[i][j]
    direction = directions.index(d)
    return direction


def newPosition(i, j, d):
    if directions[d] == UP:
        i -= 1
    elif directions[d] == RIGHT:
        j += 1
    elif directions[d] == DOWN:
        i += 1
    elif directions[d] == LEFT:
        j -= 1
    return i, j


def move(matrix, i, j, d):
    newi, newj = newPosition(i, j, d)
    try:
        if matrix[newi][newj] == "#":
            return i, j, ((d + 1) % 4)
        else:
            return (newi, newj, d)
    except IndexError:
        return (newi, newj, d)


originalMatrix = []
with open("./input.txt") as text:
    for l in text:
        l = [c for c in l.strip()]
        originalMatrix.append(l)

maxSteps = len(originalMatrix) * len(originalMatrix[0])

loops = 0

print(len(originalMatrix))
print(len(originalMatrix[0]))

for k, r in enumerate(originalMatrix):
    for h, e in enumerate(originalMatrix[k]):
        print(k, h)
        matrix = []
        for r in originalMatrix:
            matrix.append(r.copy())
        matrix[k][h] = "#"
        stepsLeft = maxSteps
        out = False
        i, j = detectStartingPoint(originalMatrix)
        direction = detectDirection(directions, originalMatrix, i, j)

        while not out and stepsLeft > 0:
            i, j, direction = move(matrix, i, j, direction)
            if i < 0 or j < 0 or i == len(matrix) or j == len(matrix[0]):
                out = True
            stepsLeft -= 1

        if not out:
            loops += 1

print(loops)
