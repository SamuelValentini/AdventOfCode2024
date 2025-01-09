locks = []
keys = []


def checkFit(lock, key):
    print(lock, key)
    for i in range(len(lock)):
        if lock[i] + key[i] > 5:
            return False
    return True


with open("./input.txt") as f:
    isKey = False
    isLock = False
    current = [0, 0, 0, 0, 0]

    for l in f:
        l = l.strip()
        if l == "":
            if isKey:
                for i in range(len(current)):
                    current[i] -= 1
                keys.append((current))
            if isLock:
                locks.append((current))
            isKey = False
            isLock = False
            current = [0, 0, 0, 0, 0]
        elif isKey or isLock:
            for i, c in enumerate(l):
                if c == "#":
                    current[i] += 1
        elif l == "#####":
            isLock = True
        elif l == ".....":
            isKey = True

fit = 0
for lock in locks:
    for key in keys:
        if checkFit(lock, key):
            fit += 1
print(fit)
