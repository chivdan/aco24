import math

def solve(reg_a_value=None):
    reg = {}
    program = []
    for line in open("input.txt"):
        if "Register" in line:
            _, register, value = line.strip().split()
            register = register.replace(":", "")
            reg[register] = int(value)
        elif "Program" in line:
            program = [int(v) for v in line.strip().split()[1].split(",")]

    if reg_a_value is not None:
        reg["A"] = reg_a_value

    ptr = 0

    def combo(arg):
        if 0 <= arg <= 3:
            return arg
        elif arg == 4:
            return reg["A"]
        elif arg == 5:
            return reg["B"]
        elif arg == 6:
            return reg["C"]
        elif arg == 7:
            raise Exception(f"Invalid operand {arg}")

    def adv(arg):
        nonlocal ptr
        result = reg["A"] / 2**combo(arg)
        reg["A"] = math.trunc(result)
        ptr += 2

    def bxl(arg):
        nonlocal ptr
        reg["B"] = reg["B"] ^ arg
        ptr += 2

    def bst(arg):
        nonlocal ptr
        reg["B"] = combo(arg) % 8
        ptr += 2

    def jnz(arg):
        nonlocal ptr

        if reg["A"] == 0:
            ptr += 2
            return
        ptr = arg

    def bxc(arg):
        nonlocal ptr
        reg["B"] = reg["B"] ^ reg["C"]
        ptr += 2

    def out(arg):
        nonlocal ptr
        ptr += 2
        return combo(arg) % 8
        
    def bdv(arg):
        nonlocal ptr
        result = reg["A"] / 2**combo(arg)
        reg["B"] = math.trunc(result)
        ptr += 2

    def cdv(arg):
        nonlocal ptr
        result = reg["A"] / 2**combo(arg)
        reg["C"] = math.trunc(result)
        ptr += 2

    op = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}    

    results = []
    while ptr < len(program):
        instruction = program[ptr]
        arg = program[ptr + 1]
        result = op[instruction](arg)
        if result is not None:
            results.append(str(result))
    
    return(",".join(results))

def solve_1():
    print(solve())

MAX_LEN = 0

def find_id(regA, program, program_str):
    global MAX_LEN

    initial_regA = regA

    ptr = 0

    regB = 0
    regC = 0

    def combo(arg):
        nonlocal regA, regB, regC
        if 0 <= arg <= 3:
            return arg
        elif arg == 4:
            return regA
        elif arg == 5:
            return regB
        elif arg == 6:
            return regC
        elif arg == 7:
            raise Exception(f"Invalid operand {arg}")

    def adv(arg):
        nonlocal ptr, regA
        result = regA / 2**combo(arg)
        regA = math.trunc(result)
        ptr += 2

    def bxl(arg):
        nonlocal ptr, regB
        regB = regB ^ arg
        ptr += 2

    def bst(arg):
        nonlocal ptr, regB
        regB = combo(arg) % 8
        ptr += 2

    def jnz(arg):
        nonlocal ptr, regA

        if regA == 0:
            ptr += 2
            return
        ptr = arg

    def bxc(arg):
        nonlocal ptr, regB, regC
        regB = regB ^ regC
        ptr += 2

    def out(arg):
        nonlocal ptr
        ptr += 2
        return combo(arg) % 8
        
    def bdv(arg):
        nonlocal ptr, regA, regB
        result = regA / 2**combo(arg)
        regB = math.trunc(result)
        ptr += 2

    def cdv(arg):
        nonlocal ptr, regA, regC
        result = regA / 2**combo(arg)
        regC = math.trunc(result)
        ptr += 2

    op = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}    

    results = []
    while ptr < len(program):
        instruction = program[ptr]
        arg = program[ptr + 1]
        result = op[instruction](arg)
        if result is not None:	    
            results.append(result)
    return results

def solve_2():
    program = []
    for line in open("input.txt"):
        if "Program" in line:
            program = [int(v) for v in line.strip().split()[1].split(",")]

    program_str = "".join([str(v) for v in program]) 
    print(program_str)
    #program
    #2413754703155530, len =  16
    for i in range(236555997347840, int(1e20), 1):
        result = find_id(i, program, program_str)
        if len(result) > 16:
            print("result len > 16")
            break
        result_str = "".join([str(v) for v in result])
        if result_str == program_str:
            print(i, result)
            break

        if result is None:
            continue
        if "".join([str(v) for v in result]) == program_str:
            print(f"Found solution: {i}")
            return

if __name__ == '__main__':
    solve_1()
    solve_2()