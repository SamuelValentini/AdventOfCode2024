def checkSolutions(i, j, text):
    maxHeight = len(text) - 1
    maxWidth = len(text[0]) - 1
    acc = 0

    if i - 1 >= 0 and j - 1 >= 0 and i < maxHeight and j < maxWidth:
        if (text[i - 1][j - 1] == "M" and text[i + 1][j + 1] == "S") and (
            text[i - 1][j + 1] == "M" and text[i + 1][j - 1] == "S"
        ):
            acc += 1
        if (text[i - 1][j - 1] == "S" and text[i + 1][j + 1] == "M") and (
            text[i - 1][j + 1] == "M" and text[i + 1][j - 1] == "S"
        ):
            acc += 1

        if (text[i - 1][j - 1] == "S" and text[i + 1][j + 1] == "M") and (
            text[i - 1][j + 1] == "S" and text[i + 1][j - 1] == "M"
        ):
            acc += 1

        if (text[i - 1][j - 1] == "M" and text[i + 1][j + 1] == "S") and (
            text[i - 1][j + 1] == "S" and text[i + 1][j - 1] == "M"
        ):
            acc += 1
    return acc


with open("./input.txt") as f:
    file = f.readlines()
    text = [list(x.strip()) for x in file]

results = 0
for i in range(len(text)):
    for j in range(len(text[0])):  # assume all string have the same length
        if text[i][j] == "A":
            results += checkSolutions(i, j, text)
print(results)
