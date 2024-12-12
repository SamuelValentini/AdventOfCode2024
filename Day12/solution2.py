from collections import Counter

garden = []
cc = []
visited = []
with open("./input.txt") as f:
    for l in f:
        l = l.strip()
        l = [c for c in l]
        garden.append(l)
        cc.append([0] * len(l))
        visited.append([0] * len(l))


def getConnectedComponents(garden, visited, i, j, n):
    visited[i][j] = n

    if i + 1 < maxI and garden[i + 1][j] == garden[i][j] and not visited[i + 1][j]:
        getConnectedComponents(garden, visited, i + 1, j, n)
    if i - 1 >= 0 and garden[i - 1][j] == garden[i][j] and not visited[i - 1][j]:
        getConnectedComponents(garden, visited, i - 1, j, n)
    if j + 1 < maxJ and garden[i][j + 1] == garden[i][j] and not visited[i][j + 1]:
        getConnectedComponents(garden, visited, i, j + 1, n)
    if j - 1 >= 0 and garden[i][j - 1] == garden[i][j] and not visited[i][j - 1]:
        getConnectedComponents(garden, visited, i, j - 1, n)


def isOutside(p):
    x = p[0]
    y = p[1]
    if x < 0 or x >= maxI or y < 0 or y >= maxJ:
        return True
    return False


def externalCorner(points, cc, i, j):
    currentCC = cc[i][j]
    p1, p3 = points

    return (isOutside(p1) or cc[p1[0]][p1[1]] != currentCC) and (
        isOutside(p3) or cc[p3[0]][p3[1]] != currentCC
    )


def internalCorner(points, cc, i, j):
    currentCC = cc[i][j]
    p1, p2, p3 = points

    if any(map(isOutside, points)):
        return 0

    return (
        (cc[p1[0]][p1[1]] == currentCC)
        and (cc[p3[0]][p3[1]] == currentCC)
        and (cc[p2[0]][p2[1]] != currentCC)
    )


def checkCorners(cc, i, j):
    corners = 0
    upLeft = ((i, j - 1), (i - 1, j - 1), (i - 1, j))
    upRigth = ((i - 1, j), (i - 1, j + 1), (i, j + 1))
    bottomLeft = ((i, j + 1), (i + 1, j + 1), (i + 1, j))
    bottomRigth = ((i + 1, j), (i + 1, j - 1), (i, j - 1))

    if externalCorner(upLeft, cc, i, j):
        corners += 1
    if externalCorner(upRigth, cc, i, j):
        corners += 1
    if externalCorner(bottomLeft, cc, i, j):
        corners += 1
    if externalCorner(bottomRigth, cc, i, j):
        corners += 1

    if internalCorner(upLeft, cc, i, j):
        corners += 1
    if internalCorner(upRigth, cc, i, j):
        corners += 1
    if internalCorner(bottomLeft, cc, i, j):
        corners += 1
    if internalCorner(bottomRigth, cc, i, j):
        corners += 1

    return corners


def computeCorners(cc, visited, i, j):
    visited[i][j] = 1
    currentCorners = checkCorners(cc, i, j)
    if i + 1 < maxI and cc[i + 1][j] == cc[i][j] and not visited[i + 1][j]:
        currentCorners += computeCorners(cc, visited, i + 1, j)
    if i - 1 >= 0 and cc[i - 1][j] == cc[i][j] and not visited[i - 1][j]:
        currentCorners += computeCorners(cc, visited, i - 1, j)
    if j + 1 < maxJ and cc[i][j + 1] == cc[i][j] and not visited[i][j + 1]:
        currentCorners += computeCorners(cc, visited, i, j + 1)
    if j - 1 >= 0 and cc[i][j - 1] == cc[i][j] and not visited[i][j - 1]:
        currentCorners += computeCorners(cc, visited, i, j - 1)
    return currentCorners


cost = 0
maxI = len(cc)
maxJ = len(cc[0])
corners = {}

n = 1
for i, row in enumerate(garden):
    for j, current in enumerate(row):
        if not cc[i][j]:
            getConnectedComponents(garden, cc, i, j, n)
            n += 1

areas = Counter([x for xs in cc for x in xs])

for i, row in enumerate(cc):
    for j, current in enumerate(row):
        if not visited[i][j]:
            if current in corners:
                corners[current] += computeCorners(cc, visited, i, j)
            else:
                corners[current] = computeCorners(cc, visited, i, j)

cost = 0
for k in areas:
    cost += areas[k] * corners[k]
print(cost)
