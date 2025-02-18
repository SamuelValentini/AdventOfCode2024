MINDIFF = 1
MAXDIFF = 3
reports = []


def checkSafety(report):
    up = True
    down = True

    for i in range(len(report) - 1):
        if report[i] > report[i + 1]:
            down = False
        if report[i] < report[i + 1]:
            up = False
        res = abs(report[i] - report[i + 1])
        if res < MINDIFF or res > MAXDIFF:
            return False

    return up or down


with open("./input.txt") as f:
    for l in f:
        l = [int(x) for x in l.strip().split()]
        reports.append(l)

safe = 0
for r in reports:
    safe += checkSafety(r)

print(safe)
