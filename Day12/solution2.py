from collections import Counter

garden = []
cc = []
visited = []
with open("./test.txt") as f:
    for l in f:
        l = l.strip()
        l = [c for c in l]
        garden.append(l)
        cc.append([0] * len(l))
        visited.append([0] * len(l))


def getConnectedComponents(garden, visited, i, j, n):
    visited[i][j] = n
    maxI = len(garden)
    maxJ = len(garden[0])

    if i + 1 < maxI and garden[i + 1][j] == garden[i][j] and not visited[i + 1][j]:
        getConnectedComponents(garden, visited, i + 1, j, n)
    if i - 1 >= 0 and garden[i - 1][j] == garden[i][j] and not visited[i - 1][j]:
        getConnectedComponents(garden, visited, i - 1, j, n)
    if j + 1 < maxJ and garden[i][j + 1] == garden[i][j] and not visited[i][j + 1]:
        getConnectedComponents(garden, visited, i, j + 1, n)
    if j - 1 >= 0 and garden[i][j - 1] == garden[i][j] and not visited[i][j - 1]:
        getConnectedComponents(garden, visited, i, j - 1, n)


def checkCorners(cc, visited, i, j):
    maxI = len(cc)
    maxJ = len(cc[0])

    upLeft = ((i, j - 1), (i - 1, j - 1), (i - 1, j))

    upRigth = ((i - 1, j), (i - 1, j + 1), (i, j + 1))

    bottomLeft = ((i, j + 1), (i + 1, j + 1), (i + 1, j))

    bottomRigth = ((i + 1, j), (i + 1, j - 1), (i, j - 1))


def computeCorners(cc, visited, i, j):
    corners = checkCorners(cc, visited, i, j)


cost = 0

n = 1
for i, row in enumerate(garden):
    for j, current in enumerate(row):
        if not cc[i][j]:
            getConnectedComponents(garden, visited, i, j, n)
            n += 1

for i, row in enumerate(garden):
    for j, current in enumerate(row):
        if not cc[i][j]:
            getConnectedComponents(garden, visited, i, j, n)
            n += 1
