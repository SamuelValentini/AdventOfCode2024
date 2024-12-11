with open("./input.txt") as f:
    l = [int(x) for x in next(f).strip().split()]
    print(l)

start = {x: 1 for x in l}

for i in range(75):
    counter = {}
    for k in start:
        n = start[k]
        if k == 0:
            if 1 in counter:
                counter[1] += n
            else:
                counter[1] = n
        elif (len(str(k)) % 2) == 0:
            e = str(k)
            mid = len(e) // 2
            firstHalf = int(e[:mid])
            secondHalf = int(e[mid:])

            if firstHalf in counter:
                counter[firstHalf] += n
            else:
                counter[firstHalf] = n

            if secondHalf in counter:
                counter[secondHalf] += n
            else:
                counter[secondHalf] = n
        else:
            res = k * 2024
            if res in counter:
                counter[res] += n
            else:
                counter[res] = n

    start = counter

res = 0
for k in start:
    res += start[k]

print(res)
