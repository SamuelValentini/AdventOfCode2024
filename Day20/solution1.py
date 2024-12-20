import heapq
import itertools

matrix = []
visited = []


def bfs(visited, x, y):
    maxX = len(visited)
    maxY = len(visited[0])
    queue = [(0, x, y)]
    heapq.heapify(queue)
    while len(queue) > 0 and not visited[y][x] == "E":
        d, x, y = heapq.heappop(queue)
        if visited[y][x] == "." or visited[y][x] == "S":
            visited[y][x] = d
            if (y - 1 >= 0) and visited[y - 1][x] != "#":
                heapq.heappush(queue, (d + 1, x, y - 1))
            if (x - 1 >= 0) and visited[y][x - 1] != "#":
                heapq.heappush(queue, (d + 1, x - 1, y))
            if not (y + 1 >= maxY) and visited[y + 1][x] != "#":
                heapq.heappush(queue, (d + 1, x, y + 1))
            if not (x + 1 >= maxX) and visited[y][x + 1] != "#":
                heapq.heappush(queue, (d + 1, x + 1, y))
    visited[y][x] = d


def getStart(race):
    for x, r in enumerate(race):
        for y, e in enumerate(r):
            if e == "S":
                return x, y


def manhattan(x, y, x1, y1):
    return abs(x - x1) + abs(y - y1)


race = []
with open("./input.txt") as f:
    for l in f:
        race.append([c for c in l.strip()])

for l in race:
    print(l)

x, y = getStart(race)

bfs(race, y, x)
for l in race:
    print(l)


count = 0
for x, y in itertools.product(range(len(race)), range(len(race))):
    for x1, y1 in itertools.product(range(len(race)), range(len(race))):
        if isinstance(race[x][y], int) and isinstance(race[x1][y1], int):
            d = manhattan(x, y, x1, y1)
            if d <= 2:
                r = race[x1][y1] - race[x][y] - d
                if r >= 100:
                    count += 1
print(count)
