from collections import Counter


def createFreeBlockSizeMap(expandedMap):
    freespaces = {}
    freeBlockSize = 0
    startingIndex = None
    for i in range(len(expandedMap)):
        if expandedMap[i] == ".":
            freeBlockSize += 1
            if startingIndex is None:
                startingIndex = i
        else:
            if freeBlockSize > 0:
                freespaces[startingIndex] = freeBlockSize
            freeBlockSize = 0
            startingIndex = None

    return freespaces


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

i = 0
j = len(expandedMap) - 1

freeBlock = createFreeBlockSizeMap(expandedMap)
sizes = Counter(expandedMap)
del sizes["."]

currentFile = max([x for x in expandedMap if x != "."])

while currentFile > 0:
    currentFileSize = sizes[currentFile]
    currentFileStart = expandedMap.index(currentFile)
    for index in sorted(freeBlock):
        if freeBlock[index] >= currentFileSize and currentFileStart > index:
            i = index
            expandedMap = [x if x != currentFile else "." for x in expandedMap]
            for j in range(currentFileSize):
                expandedMap[i + j] = currentFile
            freeBlock = createFreeBlockSizeMap(expandedMap)
            break
    currentFile -= 1

expandedMap = [x if x != "." else 0 for x in expandedMap]
checksum = 0
for i in range(len(expandedMap)):
    checksum += expandedMap[i] * i

print(checksum)
