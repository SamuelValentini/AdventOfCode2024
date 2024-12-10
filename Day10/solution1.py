def getDirections(map, i, j):
    currentValue = map[i][j]
    directions = []
    maxI = len(map)
    maxJ = len(map[0])
    if i + 1 < maxI and map[i + 1][j] == (currentValue + 1):
        directions.append((i + 1, j))
    if i - 1 >= 0 and map[i - 1][j] == (currentValue + 1):
        directions.append((i - 1, j))
    if j + 1 < maxJ and map[i][j + 1] == (currentValue + 1):
        directions.append((i, j + 1))
    if j - 1 >= 0 and map[i][j - 1] == (currentValue + 1):
        directions.append((i, j - 1))

    return directions


def checkTrail(map, i, j, alreadyExplored):
    if (i, j) not in alreadyExplored:
        alreadyExplored.add((i, j))
        currentValue = map[i][j]
        validDirections = getDirections(map, i, j)
        if currentValue == 9:
            return 1
        else:
            return sum(
                [checkTrail(map, i, j, alreadyExplored) for i, j in validDirections]
            )
    return 0


map = []
with open("./input.txt") as f:
    for l in f:
        l = [int(x) for x in l.strip()]
        map.append(l)

score = 0
for i, r in enumerate(map):
    for j, e in enumerate(r):
        if e == 0:
            alreadyExplored = set()
            score += checkTrail(map, i, j, alreadyExplored)

print(score)
