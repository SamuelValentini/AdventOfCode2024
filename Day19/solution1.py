from functools import cache


@cache
def findDesign(pattern, towels, currentPos):
    if currentPos == len(pattern):
        return True

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
        if result:
            return result
    return False


patterns = []
with open("./input.txt") as f:
    towels = tuple([p.strip() for p in next(f).split(",")])
    next(f)
    for l in f:
        l = l.strip()
        patterns.append(l)


count = 0
for p in patterns:
    print(p)
    d = findDesign(p, towels, 0)
    if d:
        count += 1
print(count)
