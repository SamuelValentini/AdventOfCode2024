with open("./input.txt") as f:
    diskMap = f.readline().strip()


expandedMap = []
isBlock = True
id = 0

for n in diskMap:
    n = int(n)
    if isBlock:
        for _ in range(n):
            expandedMap.append(id)
        isBlock = False
        id += 1
    else:
        for _ in range(n):
            expandedMap.append(".")
        isBlock = True

print(expandedMap)

i = 0
j = len(expandedMap) - 1
while i < j:
    if expandedMap[i] == "." and expandedMap[j] == ".":
        j -= 1
    if expandedMap[i] != "." and expandedMap[j] == ".":
        j -= 1
        i += 1
    if expandedMap[i] == "." and expandedMap[j] != ".":
        expandedMap[i] = expandedMap[j]
        expandedMap[j] = "."
        i += 1
        j -= 1
    if expandedMap[i] != "." and expandedMap[j] != ".":
        i += 1

expandedMap = [x if x != "." else 0 for x in expandedMap]
checksum = 0
for i in range(len(expandedMap)):
    checksum += expandedMap[i] * i

print(checksum)
