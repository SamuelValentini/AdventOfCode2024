precedence = {}
printing = []

with open("input.txt") as f:
    for l in f:
        if "|" in l:
            l = l.strip().split("|")
            if l[0] not in precedence:
                precedence[l[0]] = [l[1]]
            else:
                precedence[l[0]].append(l[1])
        elif "," in l:
            l = l.strip().split(",")
            printing.append(l)

print(precedence)
print(printing)


def checkOrder(k, e, p):
    if k in p and e in p:
        i = p.index(k)
        j = p.index(e)
        if i > j:
            return False
        else:
            return True
    else:
        return True


def checkPrinting(precedence, p):
    for k in precedence:
        for e in precedence[k]:
            if not checkOrder(k, e, p):
                return False
    return True


sum = 0
for p in printing:
    if checkPrinting(precedence, p):
        print(p)
        print(len(p) // 2)
        print(int(p[len(p) // 2]))
        sum += int(p[len(p) // 2])
print(sum)
