# import enum

def optimize(prog: list[str]) -> list[str]:
    optimized = prog.copy()
    for i, line in enumerate(prog):
        print("line 0: {} | line: {}".format(line[0], line))
        # find values directly being moved into registers
        if line[0] == 'mov' and line[3].isnumeric():
            register = line[1]
            val = line[3]
            print("line {}: found val {} being moved into {}".format(i, val, register))
            j = i + 1
            while j < len(optimized):
                curr_line = optimized[j]
                if curr_line[0] == 'add' and curr_line[3] == register:
                    print('found static compute optimization at: ' + str(j))
                j = j + 1

            # print('found static compute optimization at: ' + str(i))
            # prog[i] = static_compute()
            # del(prog[i+1])
    return optimized


def static_compute():
    pass
