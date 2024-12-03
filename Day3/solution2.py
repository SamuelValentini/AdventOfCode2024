import re

expr = re.compile("(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don't\(\))")


def getToken(token):
    if token[0] != "":
        op = token[0].split(",")
        factor1 = int(op[0][4:])
        factor2 = int(op[1][:-1])
        return factor1 * factor2
    elif token[1] != "":
        return "DO"
    elif token[2] != "":
        return "DONT"


with open("./input.txt") as f:
    acc = 0
    do = True
    f = f.read()
    mulExpr = expr.findall(f)
    for op in mulExpr:
        token = getToken(op)
        if token == "DO":
            do = True
        elif token == "DONT":
            do = False
        elif do:
            acc += token

print(acc)
