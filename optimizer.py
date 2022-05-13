# import enum

from operator import add


ADD_STACK_POINTER = ['add', 'rsp', ',', '8']


def optimize(prog: list[str]) -> dict:
    output = {
        'program': [],
        'lines_removed': 0,
        'static_references_removed': 0,
        'stack_pushes_removed': 0
    }
    optimized = prog.copy()
    # STACK PUSH OPTIMIZATION
    for i, line in enumerate(prog):
        if line[0] == 'push':
            register1 = line[1]
            register2 = ''
            next_line = prog[i+1]
            if next_line[0] == 'mov' and next_line[3] == '[rsp + 0]':
                register2 = next_line[1]
            if prog[i+2] == ADD_STACK_POINTER:
                print(f'line {i}: found unnecessary push')
                output['stack_pushes_removed'] += 1
                if register1 == register2:
                    del(optimized[i])
                    del(optimized[i])
                    del(optimized[i])
                    output['lines_removed'] -= 3
                else:
                    optimized[i] = ['mov', register1, ',', register2]
                    del(optimized[i+1])
                    del(optimized[i+1])
                    output['lines_removed'] -= 2
    # STATIC REFERENCE OPTIMIZATION:
    prog = optimized.copy()
    for i, line in enumerate(prog):
        if line[0] == 'push':
            register = line[1]
            next_line = prog[i+1]
            if next_line[0] == 'mov' and next_line[1] == register:
                if next_line[3] == '[rsp + 0]':
                    print(f'line {i+1}: detected unneccessary stack reference')
                    output['static_references_removed'] += 1
                    if next_line[1] == register:
                        output['lines_removed'] += 1
                        del(optimized[i+1])
                    else:
                        next_line[3] = register
                        optimized[i+1] = next_line
    # rsp pointer adds optimization
    prog = optimized.copy()
    for i, line in enumerate(prog):
        if line == ADD_STACK_POINTER:
            add_bits = 8
            while optimized[i+1] == ADD_STACK_POINTER:
                add_bits += 8
                del(optimized[i+1])
                del(prog[i+1])
                output['lines_removed'] += 1
            line[3] = str(add_bits)
            optimized[i] = line
            print(f'line {i}: added {add_bits} to stack pointer movement')
    # STATIC COMPUTE OPTIMIZATION
    prog = optimized.copy()
    for i, line in enumerate(prog):
        # find values directly being moved into registers
        if line[0] == 'mov' and line[3].isnumeric():
            register = line[1]
            val = line[3]
            print("line {}: found val {} being moved into {}".format(
                    i,
                    val,
                    register
                )
            )
            j = i + 1
            while j < len(optimized):
                curr_line = optimized[j]
                if curr_line[0] == 'add' and curr_line[3] == register:
                    print('found static compute optimization at: ' + str(j))
                j = j + 1

            # print('found static compute optimization at: ' + str(i))
            # prog[i] = static_compute()
            # del(prog[i+1])
    output['program'] = optimized
    return output


def static_compute():
    pass
