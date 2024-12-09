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


def computeDistance(a1, a2):
    x1 = a1[0]
    y1 = a1[1]

    x2 = a2[0]
    y2 = a2[1]

    return abs(x1 - x2) + abs(y1 - y2)


map = []
solution = []
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
                try:
                    coeff = abs(a1[1] - a2[1]) / abs(a1[0] - a2[0])
                    coeff1 = abs(a1[1] - j) / abs(a1[0] - i)
                    coeff2 = abs(a2[1] - j) / abs(a2[0] - i)
                except ZeroDivisionError:
                    coeff = 1
                    coeff1 = 2
                    coeff2 = 3

                if coeff == coeff1 == coeff2 or (i, j) == a1 or (i, j) == a2:
                    if (i, j) not in antinodes:
                        antinodesNumber += 1
                        antinodes.add((i, j))

print(antinodesNumber)
