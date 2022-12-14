from program import Program
from state import State

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    code   = "Uncompiled/2022/day1_2.wsc"
    comp     = "Compiled/2022/day1_2.ws"
    input       = "Input/2022/day1.in"
    output     = "Output/2022/day1.out"
    log          = "Logs/2022/day1.log"

    verbosity = []

    if True:
        prog = Program(open(code).read())
        prog.output(comp)
        state = State(prog, open(input).read(), open(output, "w"), open(log, "w"), verbosity)
        try:
            output = prog.run(state)
        except:
            print(f"Line number = {prog.origlines[state.lineNumber]}")
            print(f"Line = {prog.prog[state.lineNumber].text()}")
            raise
    else:
        print(whitespace(open(comp).read(),
                         open(input).read()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
