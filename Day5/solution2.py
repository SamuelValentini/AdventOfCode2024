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


def checkOrder(k, e, p):
    if k in p and e in p:
        i = p.index(k)
        j = p.index(e)
        if i > j:
            tmp = p[j]
            p[j] = p[i]
            p[i] = tmp
            return True
        else:
            return False
    else:
        return False


def checkPrinting(precedence, p):
    wronglyOrdered = False
    for k in precedence:
        for e in precedence[k]:
            if checkOrder(k, e, p):
                wronglyOrdered = True

    if wronglyOrdered:
        # WHAT? Actually just recheck if you have other wrong orders and reorder
        checkPrinting(precedence, p)
        return int(p[len(p) // 2])
    else:
        return 0


sum = 0
for p in printing:
    sum += checkPrinting(precedence, p)
print(sum)
