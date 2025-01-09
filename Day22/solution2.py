from collections import defaultdict

PRUNE = 16777216


def nextNumber(n, steps=1):
    while steps:
        n = ((n * 64) ^ n) % PRUNE
        n = ((n // 32) ^ n) % PRUNE
        n = ((n * 2048) ^ n) % PRUNE

        steps -= 1
    return n


# secretNumbers = [1, 2, 3, 2024]
secretNumbers = []
with open("./input.txt") as f:
    for l in f:
        secretNumbers.append(int(l.strip()))

bananas = defaultdict(int)
for s in secretNumbers:
    seen = set()
    deltas = []
    for i in range(2000):
        n = nextNumber(s)
        deltas.append((n % 10) - (s % 10))
        s = n
        if i > 2:
            d = tuple(deltas)
            if d not in seen:
                bananas[d] += s % 10
                seen.add(d)
            deltas.pop(0)
m = 0
key = ""
for k in bananas:
    if bananas[k] > m:
        m = bananas[k]
        key = k
print(m)
print(k)
