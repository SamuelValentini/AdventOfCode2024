import heapq

MAXDIM = 71
TODROP = 1024

matrix = []
visited = []


def bfs(visited, x, y):
    queue = [(0, x, y)]
    heapq.heapify(queue)
    while len(queue) > 0 and not ((x == MAXDIM - 1) and (y == MAXDIM - 1)):
        d, x, y = heapq.heappop(queue)
        if visited[y][x] == 0:
            visited[y][x] = 1
            if (y - 1 >= 0) and not visited[y - 1][x]:
                heapq.heappush(queue, (d + 1, x, y - 1))
            if (x - 1 >= 0) and not visited[y][x - 1]:
                heapq.heappush(queue, (d + 1, x - 1, y))
            if not (y + 1 >= MAXDIM) and (not visited[y + 1][x]):
                heapq.heappush(queue, (d + 1, x, y + 1))
            if not (x + 1 >= MAXDIM) and (not visited[y][x + 1]):
                heapq.heappush(queue, (d + 1, x + 1, y))

    if x == MAXDIM - 1 and y == MAXDIM - 1:
        return d
    else:
        return 0


for i in range(MAXDIM):
    l = []
    v = []
    for j in range(MAXDIM):
        l.append(".")
        v.append(0)
    matrix.append(l)
    visited.append(v)

corrupted = []
with open("./input.txt") as f:
    for l in f:
        l = l.strip().split(",")
        corrupted.append((int(l[0]), int(l[1])))

for i in range(TODROP):
    x, y = corrupted[i]
    matrix[y][x] = "#"
    visited[y][x] = 1


minPath = 1
dropping = 1024
while minPath:
    current = []
    x, y = corrupted[dropping]
    visited[y][x] = 1
    for l in visited:
        current.append(l.copy())
    minPath = bfs(current, 0, 0)
    dropping += 1
print(x, y)
