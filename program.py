from commands import Add, Divide, Drop, Duplicate, End, Gosub, Goto, GotoIfNegative, GotoIfZero, Grab, Label, Modulo, Multiply, PrintChar, PrintNumber
from commands import Push, ReadCharacter, ReadNumber, Retrieve, Return, Splurge, Store, Subtract, Swap

class Program:
    def __init__(self, code):
        prog = []
        labels = {}
        self.origlines = {}
        o = 0
        for line in code.split("\n"):
            o += 1
            line = line.split("#")[0].strip()
            if len(line) == 0:
                continue
            self.origlines[len(prog)] = o
            if line.startswith("LABEL"):
                v = int(line.split()[-1])
                if v in labels:
                    raise Exception(f"Repeated label {v}")
                labels[v] = len(prog)
                prog.append(Label(v))
            elif line == "END":
                prog.append(End())
            elif line == "RETURN":
                prog.append(Return())
            elif line.startswith("GOSUB "):
                prog.append(Gosub(int(line.split()[-1])))
            elif line.startswith("GOTO "):
                prog.append(Goto(int(line.split()[-1])))
            elif line.startswith("GOTOIFZERO "):
                prog.append(GotoIfZero(int(line.split()[-1])))
            elif line.startswith("GOTOIFNEG "):
                prog.append(GotoIfNegative(int(line.split()[-1])))
            elif line.startswith("PUSH"):
                prog.append(Push(int(line.split()[-1])))
            elif line == "DUP":
                prog.append(Duplicate())
            elif line.startswith("GRAB"):
                prog.append(Grab(int(line.split()[-1])))
            elif line == "SWAP":
                prog.append(Swap())
            elif line == "DROP":
                prog.append(Drop())
            elif line == "READC":
                prog.append(ReadCharacter())
            elif line == "READN":
                prog.append(ReadNumber())
            elif line == "RETRIEVE":
                prog.append(Retrieve())
            elif line == "STORE":
                prog.append(Store())
            elif line == "PRINTC":
                prog.append(PrintChar())
            elif line == "PRINTN":
                prog.append(PrintNumber())
            elif line == "ADD":
                prog.append(Add())
            elif line == "SUB":
                prog.append(Subtract())
            elif line == "MUL":
                prog.append(Multiply())
            elif line == "DIV":
                prog.append(Divide())
            elif line == "MOD":
                prog.append(Modulo())
            elif line == "SPLURGE":
                prog.append(Splurge())
            else:
                raise Exception(f"Parse error: {line}")
        self.prog = prog
        self.labels = labels

    def findLabel(self, n):
        return self.labels[n]

    def run(self, state):
        while not state.finished:
            line = self.prog[state.lineNumber]
            if "code" in state.verbosity:
                state.ws.log.writelines([f"{state.lineNumber} {line.text()}\n"])
            line.do(state)
            state.lineNumber += 1
        if "final" in state.verbosity:
            state.ws.splurge()
        return state.ws.output

    def output(self, file):
        f = open(file, "w")
        f.write(".".join(k for line in self.prog
                         for k in line.code()))