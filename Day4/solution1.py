def checkUpper(i, j, text):
    if text[i - 1][j] == "M" and text[i - 2][j] == "A" and text[i - 3][j] == "S":
        return 1
    else:
        return 0


def checkUpperRight(i, j, text):
    if (
        text[i - 1][j + 1] == "M"
        and text[i - 2][j + 2] == "A"
        and text[i - 3][j + 3] == "S"
    ):
        return 1
    else:
        return 0


def checkRight(i, j, text):
    if text[i][j + 1] == "M" and text[i][j + 2] == "A" and text[i][j + 3] == "S":
        return 1
    else:
        return 0


def checkBottomRight(i, j, text):
    if (
        text[i + 1][j + 1] == "M"
        and text[i + 2][j + 2] == "A"
        and text[i + 3][j + 3] == "S"
    ):
        return 1
    else:
        return 0


def checkBottom(i, j, text):
    if text[i + 1][j] == "M" and text[i + 2][j] == "A" and text[i + 3][j] == "S":
        return 1
    else:
        return 0


def checkBottomLeft(i, j, text):
    if (
        text[i + 1][j - 1] == "M"
        and text[i + 2][j - 2] == "A"
        and text[i + 3][j - 3] == "S"
    ):
        return 1
    else:
        return 0


def checkLeft(i, j, text):
    if text[i][j - 1] == "M" and text[i][j - 2] == "A" and text[i][j - 3] == "S":
        return 1
    else:
        return 0


def checkUpperLeft(i, j, text):
    if (
        text[i - 1][j - 1] == "M"
        and text[i - 2][j - 2] == "A"
        and text[i - 3][j - 3] == "S"
    ):
        return 1
    else:
        return 0


def checkSolutions(i, j, text):
    acc = 0
    maxHeight = len(text) - 1
    maxWidth = len(text[0]) - 1
    if i >= 3:
        acc += checkUpper(i, j, text)
    if i >= 3 and maxWidth - j >= 3:
        acc += checkUpperRight(i, j, text)
    if maxWidth - j >= 3:
        acc += checkRight(i, j, text)
    if maxHeight - i >= 3 and maxWidth - j >= 3:
        acc += checkBottomRight(i, j, text)
    if maxHeight - i >= 3:
        acc += checkBottom(i, j, text)
    if maxHeight - i >= 3 and j >= 3:
        acc += checkBottomLeft(i, j, text)
    if j >= 3:
        acc += checkLeft(i, j, text)
    if i >= 3 and j >= 3:
        acc += checkUpperLeft(i, j, text)
    return acc


with open("./input.txt") as f:
    file = f.readlines()
    text = [list(x.strip()) for x in file]

results = 0
for i in range(len(text)):
    for j in range(len(text[0])):  # assume all string have the same length
        if text[i][j] == "X":
            results += checkSolutions(i, j, text)
print(results)
