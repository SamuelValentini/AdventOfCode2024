from functools import cache
import numpy as np

offset = 10000000000000

machines = []
currentMachine = [0, 0, 0]
with open("./input.txt") as f:
    for l in f:
        if l.startswith("Button A"):
            l = l.strip().split(" ")
            x = int(l[2][2:][:-1])
            y = int(l[3][2:])
            currentMachine[0] = (x, y)

        elif l.startswith("Button B"):
            l = l.strip().split(" ")
            x = int(l[2][2:][:-1])
            y = int(l[3][2:])
            currentMachine[1] = (x, y)

        elif l.startswith("Prize"):
            l = l.strip().split(" ")
            x = offset + int(l[1][2:][:-1])
            y = offset + int(l[2][2:])
            currentMachine[2] = (x, y)
        elif l == "\n":
            machines.append(currentMachine)
            currentMachine = [0, 0, 0]


cost = 0
for machine in machines:
    X = [[machine[0][0], machine[1][0]], [machine[0][1], machine[1][1]]]
    y = [machine[2][0], machine[2][1]]
    solution = np.linalg.solve(X, y)
    print(solution)

    if all(np.isclose(np.round(solution), solution, rtol=0, atol=1e-4)):
        cost += 3 * solution[0] + solution[1]
print(cost)
