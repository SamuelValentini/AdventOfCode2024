from collections import Counter

firstList = []
secondList = []

with open("./input.txt") as f:
    for l in f:
        l = l.strip().split()
        firstList.append(int(l[0]))
        secondList.append(int(l[1]))

secondList = Counter(secondList)

result = 0
for k in firstList:
    result += k * secondList[k]

print(result)
