PRUNE = 16777216


def nextNumber(n, steps=2000):
    while steps:
        n = ((n * 64) ^ n) % PRUNE
        n = ((n // 32) ^ n) % PRUNE
        n = ((n * 2048) ^ n) % PRUNE

        steps -= 1
    return n


secretNumbers = []
with open("./input.txt") as f:
    for l in f:
        secretNumbers.append(int(l.strip()))

s = [x for x in map(nextNumber, secretNumbers)]
print(s)
print(sum(s))
