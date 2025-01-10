def XOR(b1, b2):
    if b1 == b2:
        return 0
    else:
        return 1


def AND(b1, b2):
    if b1 == b2 == 1:
        return 1
    else:
        return 0


def OR(b1, b2):
    if b1 or b2:
        return 1
    else:
        return 0


values = {}
computations = []

with open("./input.txt") as f:
    for l in f:
        l = l.strip()
        if ":" in l:
            l = l.split(": ")
            values[l[0]] = int(l[1])
        elif "->" in l:
            l = l.split(" ")
            computations.append((l[0], l[1], l[2], l[4]))

while len(computations) > 0:
    missing = []
    for rule in computations:
        b1 = rule[0]
        op = rule[1]
        b2 = rule[2]
        res = rule[3]

        if b1 in values and b2 in values:
            b1 = values[b1]
            b2 = values[b2]
            if op == "XOR":
                val = XOR(b1, b2)
            if op == "AND":
                val = AND(b1, b2)
            if op == "OR":
                val = OR(b1, b2)

            values[res] = val
        else:
            missing.append(rule)

    computations = missing


bitlist = []
for k in sorted(values):
    if "z" in k:
        bitlist.append(values[k])

bitlist.reverse()
out = 0
for bit in bitlist:
    out = (out << 1) | bit
print(out)
