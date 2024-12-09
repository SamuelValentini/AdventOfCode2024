import itertools


def getAntennasPositions(map):
    antennas = {}
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != ".":
                if map[i][j] not in antennas:
                    antennas[map[i][j]] = [(i, j)]
                else:
                    antennas[map[i][j]].append((i, j))
    return antennas


def inline(a1, a2):
    if a1[0] == a2[0]:
        return True
    if a1[1] == a2[1]:
        return True
    d1 = abs(a1[0] - a2[0])
    d2 = abs(a1[1] - a2[1])
    if d1 == d2 == 1:
        return True
    return False


def computeDistance(a1, a2):
    x1 = a1[0]
    y1 = a1[1]

    x2 = a2[0]
    y2 = a2[1]

    return abs(x1 - x2) + abs(y1 - y2)


map = []
with open("./input.txt") as f:
    for l in f:
        l = l.strip()
        l = [c for c in l]
        map.append(l)

antennas = getAntennasPositions(map)

antinodesNumber = 0
antinodes = set()
for k in antennas:
    for a1, a2 in itertools.combinations(antennas[k], 2):
        for i in range(len(map)):
            for j in range(len(map[0])):
                d1 = computeDistance(a1, (i, j))
                d2 = computeDistance(a2, (i, j))
                if 2 * d1 == d2 or 2 * d2 == d1:
                    try:
                        coeff = (a1[1] - a2[1]) / (a1[0] - a2[0])
                        coeff1 = (a1[1] - j) / (a1[0] - i)
                        coeff2 = (a2[1] - j) / (a2[0] - i)
                    except ZeroDivisionError:
                        coeff = 1
                        coeff1 = 2
                        coeff2 = 3

                    if coeff == coeff1 == coeff2:
                        map[i][j] = "#"
                        if (i, j) not in antinodes:
                            antinodes.add((i, j))
                            antinodesNumber += 1

print(antinodesNumber)
