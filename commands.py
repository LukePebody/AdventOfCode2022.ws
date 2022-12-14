def encode(number):
    x = []
    if number >= 0:
        x.append(" ")
    else:
        x.append("\t")
        number = -number
    i = 1
    while (i + i) <= number:
        i += i
    while i >= 1:
        if (number & i):
            x.append("\t")
        else:
            x.append(" ")
        i //= 2
    x.append("\n")
    return x


class Label:
    def __init__(self, n):
        self.n = n

    def do(self, state):
        pass

    def text(self):
        return f"LABEL {self.n}"

    def code(self):
        return ["\n", " ", " "] + encode(self.n)


class Goto:
    def __init__(self, n):
        self.n = n

    def do(self, state):
        state.lineNumber = state.program.findLabel(self.n)

    def text(self):
        return f"GOTO {self.n}"

    def code(self):
        return ["\n", " ", "\n"] + encode(self.n)


class Gosub:
    def __init__(self, n):
        self.n = n

    def do(self, state):
        state.returnPoints.append(state.lineNumber)
        state.lineNumber = state.program.findLabel(self.n)

    def text(self):
        return f"GOSUB {self.n}"

    def code(self):
        return ["\n", " ", "\t"] + encode(self.n)


class GotoIfZero:
    def __init__(self, n):
        self.n = n

    def do(self, state):
        val = state.ws.pop()
        if (val == 0):
            state.lineNumber = state.program.findLabel(self.n)

    def text(self):
        return f"GOTOIFZERO {self.n}"

    def code(self):
        return ["\n", "\t", " "] + encode(self.n)


class GotoIfNegative:
    def __init__(self, n):
        self.n = n

    def do(self, state):
        val = state.ws.pop()
        if (val < 0):
            state.lineNumber = state.program.findLabel(self.n)

    def text(self):
        return f"GOTOIFNEG {self.n}"

    def code(self):
        return ["\n", "\t", "\t"] + encode(self.n)


class Return:
    def __init__(self):
        pass

    def do(self, state):
        state.lineNumber = state.returnPoints[-1]
        state.returnPoints = state.returnPoints[:-1]

    def text(self):
        return f"RETURN"

    def code(self):
        return ["\n", "\t", "\n"]


class End:
    def __init__(self):
        pass

    def do(self, state):
        state.finished = True

    def text(self):
        return f"END"

    def code(self):
        return ["\n", "\n", "\n"]


class Push:
    def __init__(self, n):
        self.n = n

    def do(self, state):
        state.ws.push(self.n)

    def text(self):
        return f"PUSH {self.n}"

    def code(self):
        return [" ", " "] + encode(self.n)


class Duplicate:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.dup()

    def text(self):
        return f"DUP"

    def code(self):
        return [" ", "\n", " "]


class Grab:
    def __init__(self, n):
        self.n = n

    def do(self, state):
        state.ws.grab(self.n)

    def text(self):
        return f"GRAB {self.n}"

    def code(self):
        return [" ", "\t", " "] + encode(self.n)

class Swap:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.swap()

    def text(self):
        return f"SWAP"

    def code(self):
        return [" ", "\n", "\t"]


class Drop:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.drop()

    def text(self):
        return f"DROP"

    def code(self):
        return [" ", "\n", "\n"]


class ReadCharacter:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.readCharacter()

    def text(self):
        return f"READC"

    def code(self):
        return ["\t", "\n", "\t", " "]


class ReadNumber:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.readNumber()

    def text(self):
        return f"READN"

    def code(self):
        return ["\t", "\n", "\t", "\t"]


class Retrieve:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.retrieve()

    def text(self):
        return f"RETRIEVE"

    def code(self):
        return ["\t", "\t", "\t"]


class Store:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.store()

    def text(self):
        return f"STORE"

    def code(self):
        return ["\t", "\t", " "]


class PrintChar:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.printcharacter()

    def text(self):
        return f"PRINTC"

    def code(self):
        return ["\t", "\n", " ", " "]


class PrintNumber:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.printnumber()

    def text(self):
        return f"PRINTN"

    def code(self):
        return ["\t", "\n", " ", "\t"]


class Add:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.add()

    def text(self):
        return f"ADD"

    def code(self):
        return ["\t", " ", " ", " "]


class Subtract:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.subtract()

    def text(self):
        return f"SUB"

    def code(self):
        return ["\t", " ", " ", "\t"]


class Multiply:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.multiply()

    def text(self):
        return f"MUL"

    def code(self):
        return ["\t", " ", " ", "\n"]

class Divide:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.divide()

    def text(self):
        return f"DIV"

    def code(self):
        return ["\t", " ", "\t", " "]

class Modulo:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.modulo()

    def text(self):
        return f"MOD"

    def code(self):
        return ["\t", " ", "\t", "\t"]

class Splurge:
    def __init__(self):
        pass

    def do(self, state):
        state.ws.splurge()

    def text(self):
        return f"SPLURGE"

    def code(self):
        return []

