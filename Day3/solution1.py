import re

expr = re.compile("mul\([0-9]{1,3},[0-9]{1,3}\)")

with open("./input.txt") as f:
    f = f.read()
    mulExpr = expr.findall(f)
    acc = 0
    for op in mulExpr:
        op = op.split(",")
        factor1 = int(op[0][4:])
        factor2 = int(op[1][:-1])
        acc += factor1 * factor2

print(acc)
