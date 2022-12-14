from ws import ws

class State:
    def __init__(self, program, input, output, log, verbosity):
        self.program = program
        self.lineNumber = 0
        self.ws = ws(input, output, log, verbosity)
        self.verbosity = verbosity
        self.returnPoints = []
        self.finished = False