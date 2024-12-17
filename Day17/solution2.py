class Computer:
    def __init__(self, registerA, registerB, registerC, program) -> None:
        self.registerA = registerA
        self.registerB = registerB
        self.registerC = registerC
        self.program = program
        self.ip = 0
        self.output = []

    def getCombo(self, op):
        if op == 0:
            return 0
        elif op == 1:
            return 1
        elif op == 2:
            return 2
        elif op == 3:
            return 3
        elif op == 4:
            return self.registerA
        elif op == 5:
            return self.registerB
        elif op == 6:
            return self.registerC
        elif op == 7:
            print("ERROR")
            quit()

    def executeProgram(self):
        while self.ip < len(self.program) - 1:
            instruction = self.program[self.ip]
            operand = self.program[self.ip + 1]
            if instruction == 0:
                num = self.registerA
                den = 2 ** (self.getCombo(operand))
                self.registerA = num // den
            if instruction == 1:
                self.registerB = self.registerB ^ operand
            if instruction == 2:
                operand = self.getCombo(operand)
                self.registerB = operand % 8
            if instruction == 3:
                if self.registerA != 0:
                    self.ip = operand - 2
            if instruction == 4:
                self.registerB = self.registerB ^ self.registerC
            if instruction == 5:
                operand = self.getCombo(operand) % 8
                self.output.append(operand)
                if len(self.output) > len(self.program):
                    break
            if instruction == 6:
                num = self.registerA
                den = 2 ** (self.getCombo(operand))
                self.registerB = num // den
            if instruction == 7:
                num = self.registerA
                den = 2 ** (self.getCombo(operand))
                self.registerC = num // den
            self.ip += 2

    def printOutput(self):
        print(self.output)


with open("./input.txt") as f:
    for l in f:
        if l.startswith("Register A"):
            l = l.strip().split(" ")
            registerA = int(l[-1])
        elif l.startswith("Register B"):
            l = l.strip().split(" ")
            registerB = int(l[-1])
        elif l.startswith("Register C"):
            l = l.strip().split(" ")
            registerC = int(l[-1])
        elif l.startswith("Program"):
            l = l.strip().split(" ")
            program = [int(x) for x in l[-1].split(",")]

bits = [(1, 0)]
for i, a in bits:
    for a in range(a, a + 8):
        computer = Computer(a, 0, 0, program)
        computer.executeProgram()
        if computer.output == program[-i:]:
            bits += [(i + 1, a * 8)]
            if i == len(program):
                print(a)
