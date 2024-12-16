import heapq
from collections import defaultdict

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

d = 1


def getPosition(m, element):
    for x, r in enumerate(m):
        for y, e in enumerate(r):
            if e == element:
                return x, y


def getNeighbours(maze, x, y, d, directions):
    possibleDirections = []
    dx, dy = directions[d]
    if maze[x + dx][y + dy] != "#":
        possibleDirections.append((1, x + dx, y + dy, d))

    dir1 = (d + 1) % len(directions)
    d1x, d1y = directions[dir1]
    if maze[x + d1x][y + d1y] != "#":
        possibleDirections.append((1001, x + d1x, y + d1y, dir1))

    dir2 = (d - 1) % len(directions)
    d2x, d2y = directions[dir2]
    if maze[x + d2x][y + d2y] != "#":
        possibleDirections.append((1001, x + d2x, y + d2y, dir2))
    return possibleDirections


def getPath(cameFrom, gscore, x, y):
    totalPath = [(x, y)]
    totalCost = gscore[x, y]
    while (x, y) in cameFrom:
        x, y = cameFrom[(x, y)]
        totalPath.insert(0, (x, y))
        # totalCost += gscore[x, y]
    return totalPath, totalCost


def A_Star(x, y, d, directions, xEnd, yEnd):
    minPath = []
    minCost = 1000000000
    moves = [(0, x, y, d)]
    heapq.heapify(moves)
    cameFrom = {}
    gscore = defaultdict(lambda: 1000000000)
    gscore[(x, y)] = 0

    while len(moves) > 0:
        currentCost, currentX, currentY, currentDirection = heapq.heappop(moves)
        if currentX == xEnd and currentY == yEnd:
            path, cost = getPath(cameFrom, gscore, currentX, currentY)
            if cost <= minCost:
                minCost = cost
                minPath = path

        neighbours = getNeighbours(
            maze, currentX, currentY, currentDirection, directions
        )
        for n in neighbours:
            gscoreT = gscore[(currentX, currentY)] + n[0]
            if gscoreT < gscore[(n[1], n[2])]:
                cameFrom[(n[1], n[2])] = (currentX, currentY)
                gscore[(n[1], n[2])] = gscoreT
                if n not in moves:
                    heapq.heappush(moves, n)

    return minPath, minCost


def dfs(
    x,
    y,
    d,
    directions,
    xEnd,
    yEnd,
    currentCost,
    minimum,
    marker,
    pathSoFar,
):
    if x == xEnd and y == yEnd and currentCost == minimum:
        for p in pathSoFar:
            try:
                marker[p[0]][p[1]] += 1
            except TypeError:
                pass
        return
    elif currentCost > minimum:
        return
    else:
        neighbours = getNeighbours(maze, x, y, d, directions)
        for n in neighbours:
            if (n[1], n[2]) not in pathSoFar:
                localPath = pathSoFar.copy()
                localPath.add((n[1], n[2]))
                visited.add((n[1], n[2], n[3]))
                dfs(
                    n[1],
                    n[2],
                    n[3],
                    directions,
                    xEnd,
                    yEnd,
                    currentCost + n[0],
                    minimum,
                    marker,
                    localPath,
                )


maze = []
marker = []
with open("./input.txt") as f:
    for l in f:
        l = [x for x in l.strip()]
        m = [0 if x == "." else x for x in l]
        maze.append(l)
        marker.append(m)

x, y = getPosition(maze, "S")
xEnd, yEnd = getPosition(maze, "E")
shortestPath, totalCost = A_Star(x, y, 1, directions, xEnd, yEnd)

print(len(shortestPath))
print(totalCost)
pathSoFar = set()
visited = set((x, y, d))
dfs(
    x,
    y,
    d,
    directions,
    xEnd,
    yEnd,
    0,
    totalCost,
    marker,
    pathSoFar,
)

for x in marker:
    x = [str(e) for e in x]
    print(x)

tiles = 0
for l in marker:
    for e in l:
        try:
            if int(e) > 0:
                tiles += 1
        except ValueError:
            pass
print(tiles + 2)
