from functools import cache


@cache
def findDesign(pattern, towels, currentPos):
    solutions = 0
    if currentPos == len(pattern):
        return 1

    choices = set()
    for t in towels:
        match = True
        for i in range(len(t)):
            if currentPos + i >= len(pattern) or t[i] != pattern[currentPos + i]:
                match = False
        if match:
            choices.add(t)

    for c in choices:
        result = findDesign(pattern, towels, currentPos + len(c))
        if result > 0:
            solutions += result

    return solutions


patterns = []
with open("./input.txt") as f:
    towels = tuple([p.strip() for p in next(f).split(",")])
    next(f)
    for l in f:
        l = l.strip()
        patterns.append(l)

count = 0
for p in patterns:
    d = findDesign(p, towels, 0)
    if d > 0:
        count += d
print(count)
