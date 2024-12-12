from collections import Counter

garden = []
visited = []
with open("./input.txt") as f:
    for l in f:
        l = l.strip()
        l = [c for c in l]
        garden.append(l)
        visited.append([0] * len(l))


def computePerimeter(garden, visited, i, j):
    perimeter = 0
    area = 1
    visited[i][j] = 1
    maxI = len(garden)
    maxJ = len(garden[0])

    if not (i + 1 < maxI and garden[i + 1][j] == garden[i][j]):
        perimeter += 1
    elif not visited[i + 1][j]:
        p, a = computePerimeter(garden, visited, i + 1, j)
        perimeter += p
        area += a
    if not (i - 1 >= 0 and garden[i - 1][j] == garden[i][j]):
        perimeter += 1
    elif not visited[i - 1][j]:
        p, a = computePerimeter(garden, visited, i - 1, j)
        perimeter += p
        area += a
    if not (j + 1 < maxJ and garden[i][j + 1] == garden[i][j]):
        perimeter += 1
    elif not visited[i][j + 1]:
        p, a = computePerimeter(garden, visited, i, j + 1)
        perimeter += p
        area += a
    if not (j - 1 >= 0 and garden[i][j - 1] == garden[i][j]):
        perimeter += 1
    elif not visited[i][j - 1]:
        p, a = computePerimeter(garden, visited, i, j - 1)
        perimeter += p
        area += a
    return perimeter, area


cost = 0

for i, row in enumerate(garden):
    for j, current in enumerate(row):
        if not visited[i][j]:
            perimeter, area = computePerimeter(garden, visited, i, j)
            cost += perimeter * area
print(cost)
