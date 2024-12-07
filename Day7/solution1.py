import itertools

equations = {}
CHOICES = ["*", "+"]

with open("./test.txt") as txt:
    for l in txt:
        l = l.strip().split(":")
        result = int(l[0])
        numbers = [int(x) for x in l[1].strip().split()]
        equations[result] = numbers


correct = 0
for result in equations:
    operators = itertools.product(CHOICES, repeat=(len(equations[result]) - 1))

    remaining = equations[result][1:]
    for op in operators:
        acc = equations[result][0]
        for o, n in zip(op, remaining):
            if o == "*":
                acc *= n
            if o == "+":
                acc += n
        if acc == result:
            correct += result
            break
print(correct)
