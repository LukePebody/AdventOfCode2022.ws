class ws:
    def __init__(self, inp, output, log, verbosity):
        self.stack = []
        self.memory = {}
        self.input = inp
        self.output = output
        self.log = log
        self.cloc = 0
        self.verbosity = verbosity

    def push(self, n):
        self.stack += [n]
        if ("stack" in self.verbosity):
            self.log.writelines([f"{n} pushed.\n"])
            self.log.writelines([f"Stack = {self.stack}\n"])

    def pop(self):
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        if ("stack" in self.verbosity):
            self.log.writelines([f"{val} popped.\n"])
            self.log.writelines([f"Stack = {self.stack}\n"])
        return val

    def dup(self):
        self.stack += [self.stack[-1]]
        if ("stack" in self.verbosity):
            self.log.writelines([f"Duplicated.\n"])
            self.log.writelines([f"Stack = {self.stack}\n"])

    def grab(self, n):
        self.stack += [self.stack[-n]]
        if ("stack" in self.verbosity):
            self.log.writelines([f"Element {n} Grabbed.\n"])
            self.log.writelines([f"Stack = {self.stack}\n"])

    def swap(self):
        self.stack = self.stack[:-2] + [self.stack[-1], self.stack[-2]]
        if ("stack" in self.verbosity):
            self.log.writelines([f"Swapped.\n"])
            self.log.writelines([f"Stack = {self.stack}\n"])

    def drop(self):
        self.stack = self.stack[:-1]
        if ("stack" in self.verbosity):
            self.log.writelines([f"Dropped.\n"])
            self.log.writelines([f"Stack = {self.stack}\n"])

    def add(self):
        (l, r) = (self.stack[-2], self.stack[-1])
        self.stack = self.stack[:-2] + [l + r]
        if ("stack" in self.verbosity or "arithmetic" in self.verbosity):
            self.log.writelines([f"{l} + {r} = {l + r}\n"])
            if "stack" in self.verbosity:
                self.log.writelines([f"Stack = {self.stack}\n"])

    def subtract(self):
        (l, r) = (self.stack[-2], self.stack[-1])
        self.stack = self.stack[:-2] + [l - r]
        if ("stack" in self.verbosity or "arithmetic" in self.verbosity):
            self.log.writelines([f"{l} - {r} = {l - r}\n"])
            if "stack" in self.verbosity:
                self.log.writelines([f"Stack = {self.stack}\n"])

    def multiply(self):
        (l, r) = (self.stack[-2], self.stack[-1])
        self.stack = self.stack[:-2] + [l * r]
        if ("stack" in self.verbosity or "arithmetic" in self.verbosity):
            self.log.writelines([f"{l} * {r} = {l * r}\n"])
            if "stack" in self.verbosity:
                self.log.writelines([f"Stack = {self.stack}\n"])

    def divide(self):
        (l, r) = (self.stack[-2], self.stack[-1])
        self.stack = self.stack[:-2] + [l // r]
        if ("stack" in self.verbosity or "arithmetic" in self.verbosity):
            self.log.writelines([f"{l} / {r} = {l // r}\n"])
            if "stack" in self.verbosity:
                self.log.writelines([f"Stack = {self.stack}\n"])

    def modulo(self):
        (l, r) = (self.stack[-2], self.stack[-1])
        self.stack = self.stack[:-2] + [l % r]
        if ("stack" in self.verbosity or "arithmetic" in self.verbosity):
            self.log.writelines([f"{l} * {r} = {l % r}\n"])
            if "stack" in self.verbosity:
                self.log.writelines([f"Stack = {self.stack}\n"])

    def readCharacter(self):
        self.push(ord(self.input[self.cloc]))
        self.cloc += 1
        self.store()

    def readNumber(self):
        x = ord(self.input[self.cloc])
        sgn = 1
        if (x == ord('-')):
            self.cloc += 1
            sgn = -1
            x = ord(self.input[self.cloc])
        if ((x < 48) or (x >= 58)):
            raise "Couldn't read number"
        k = ((x - 48))
        self.cloc += 1
        x = ord(self.input[self.cloc])
        while x >= 48 and x < 58:
            k = (10*k)+(x-48)
            self.cloc += 1
            x = ord(self.input[self.cloc])
        self.push(k)
        self.store()

    def store(self):
        location = self.stack[-2]
        value = self.stack[-1]
        self.stack = self.stack[:-2]
        self.memory[location] = value
        if ("stack" in self.verbosity or "memory" in self.verbosity or location in self.verbosity):
            self.log.writelines([f"Stored {value} at {location}.\n"])
            if ("stack" in self.verbosity):
                self.log.writelines([f"Stack = {self.stack}\n"])

    def retrieve(self):
        location = self.stack[-1]
        self.stack[-1] = self.memory[location]
        if ("stack" in self.verbosity or "memory" in self.verbosity or location in self.verbosity):
            self.log.writelines([f"Read {self.stack[-1]} from {location}.\n"])
            if ("stack" in self.verbosity):
                self.log.writelines([f"Stack = {self.stack}\n"])

    def printcharacter(self):
        self.output.write(chr(self.stack[-1]))
        self.drop()

    def printnumber(self):
        self.output.write(str(self.stack[-1]))
        self.drop()

    def splurge(self):
        self.log.writelines([f"Stack={self.stack}\n"])
        if True:
            for (u, v) in sorted(self.memory.items()):
                if u >= 100 and u < self.memory[2]:
                    continue
                if u >= self.memory[2] and u < self.memory[9]:
                    continue
                vc = f" '{chr(v)}'" if (v >= 32 and v <= 126) else ""
                self.log.writelines([f"Memory[{u}]={v}{vc}\n"])
        if 9 in self.memory:
            for i in range(self.memory[8]):
                self.log.writelines("".join(
                    ".+#o"[self.memory[k]]
                    for k in range(self.memory[2]+self.memory[7]*i,
                                   self.memory[2]+self.memory[7]*(i+1)))+"\n")
        self.log.writelines(["\n"])