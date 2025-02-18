firstList = []
secondList = []

with open("./input.txt") as f:
    for l in f:
        l = l.strip().split()
        firstList.append(int(l[0]))
        secondList.append(int(l[1]))

firstList.sort()
secondList.sort()

result = 0
for x, y in zip(firstList, secondList):
    result += abs(x - y)

print(result)
