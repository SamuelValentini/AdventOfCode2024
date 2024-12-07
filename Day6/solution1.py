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


matrix = []
with open("./input.txt") as text:
    for l in text:
        l = [c for c in l.strip()]
        matrix.append(l)

i, j = detectStartingPoint(matrix)
direction = detectDirection(directions, matrix, i, j)

out = False
matrix[i][j] = VISITED

while not out:
    i, j, direction = move(matrix, i, j, direction)
    if i < 0 or j < 0 or i == len(matrix) or j == len(matrix[0]):
        out = True
    else:
        matrix[i][j] = VISITED

v = 0
print(matrix)
for r in matrix:
    for e in r:
        if e == VISITED:
            v += 1
print(v)
