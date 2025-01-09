import copy

class BinaryGate:
    def __init__(self, operands):
        self.operands = operands
    
    def is_computable(self, values):
        return all(operand in values for operand in self.operands)

    def evaluate(self, values):
        pass

class AndGate(BinaryGate):
    def __init__(self, operands):
        super().__init__(operands)

    def evaluate(self, values):
        return values[self.operands[0]] and values[self.operands[1]]
    
class OrGate(BinaryGate):
    def __init__(self, operands):
        super().__init__(operands)

    def evaluate(self, values):
        return values[self.operands[0]] or values[self.operands[1]]
    
class XorGate(BinaryGate):
    def __init__(self, operands):
        super().__init__(operands)

    def evaluate(self, values):
        return values[self.operands[0]] ^ values[self.operands[1]]

def solve_1():
    values = {}
    wires = []
    for line in open("input.txt"):
        if ":" in line:
            wire, value = line.strip().split(": ")
            values[wire] = bool(int(value))
        elif "->" in line:
            lhs, rhs = line.strip().split(" -> ")
            gate = None
            if "AND" in lhs:
                gate = AndGate(lhs.split(" AND "))
            elif "XOR" in lhs:
                gate = XorGate(lhs.split(" XOR "))
            elif "OR" in lhs:
                gate = OrGate(lhs.split(" OR "))
            wires.append((gate, rhs))

    while len(wires) > 0:
        computed_wires = []
        for gate, wire in wires:
            if gate.is_computable(values):
                values[wire] = gate.evaluate(values)
                computed_wires.append((gate, wire))
        for computed_wire in computed_wires:
            wires.remove(computed_wire)

    zs = set()
    for wire in values:
        if wire.startswith("z"):
            zs.add(wire)
    
    ans = "".join([str(int(values[z])) for z in sorted(zs, reverse=True)])
    ans = int(ans, 2)
    print(ans)

def solve_2():
    values = {}
    wires = []
    for line in open("input.txt"):
        if ":" in line:
            wire, value = line.strip().split(": ")
            values[wire] = bool(int(value))
        elif "->" in line:
            lhs, rhs = line.strip().split(" -> ")
            gate = None
            if "AND" in lhs:
                gate = AndGate(lhs.split(" AND "))
            elif "XOR" in lhs:
                gate = XorGate(lhs.split(" XOR "))
            elif "OR" in lhs:
                gate = OrGate(lhs.split(" OR "))
            wires.append([gate, rhs])


    def calc(wires, values, x_dec, y_dec):
        computed = [False] * len(wires)
        while len(values) < 312:
            to_compute = len(values)
            for i, (gate, wire) in enumerate(wires):
                if computed[i]:
                    continue
                if gate.is_computable(values):
                    values[wire] = gate.evaluate(values)
                    computed[i] = True
            if to_compute == len(values):
                return 1000000

        ans = "".join([str(int(values[z])) for z in zs_sorted])
        while len(ans) < 46:
            ans = "0" + ans

        right_ans = bin(x_dec + y_dec)[2:]

        while len(right_ans) < 46:
            right_ans = "0" + right_ans

        return 1 if right_ans != ans else 0
    
    def create_data(k):
        L = 45

        xys = []

        if k == L - 1:        
            # 00
            x_00 = [0] * L
            y_00 = [0] * L
            xys.append((x_00, y_00, 0, 0))

        # 01
        x_01 = [0] * L
        y_01 = [0] * L
        y_01[k] = 1
        xys.append((x_01, y_01, 0, 2**(L - 1 - k)))

        # 10
        x_10 = [0] * L
        y_10 = [0] * L
        x_10[k] = 1
        xys.append((x_10, y_10, 2**(L - 1 - k), 0))
        
        # 11
        x_11 = [0] * L
        y_11 = [0] * L
        x_11[k] = 1
        y_11[k] = 1
        xys.append((x_11, y_11, 2**(L - 1 - k), 2**(L - 1 - k)))


        x_names = sorted([k for k in values if k.startswith("x")], reverse=True)
        y_names = sorted([k for k in values if k.startswith("y")], reverse=True)

        result = []
        for x_m, y_m, x_dec, y_dec in xys:
            values_changed = copy.deepcopy(values)
            for i in range(len(x_m)):
                values_changed[x_names[i]] = bool(int(x_m[i]))
            for i in range(len(y_m)):
                values_changed[y_names[i]] = bool(int(y_m[i]))
            result.append((values_changed, x_dec, y_dec))
        return result

    xs = set()
    ys = set()
    zs = set()
    for wire in values:
        if wire.startswith("x"):
            xs.add(wire)
        elif wire.startswith("y"):
            ys.add(wire)

    for gate, rhs in wires:
        if rhs.startswith("z"):
            zs.add(rhs)

    zs_sorted = sorted(zs, reverse=True)

    individual = (copy.deepcopy(wires), [])

    def do_skip(i, j, swaps):
        for old_swap in swaps:
            if i == old_swap[0][0] or i == old_swap[0][1]:
                return True
            if j == old_swap[0][1] or j == old_swap[0][0]:
                return True
        return False

    test_data = {k: create_data(k) for k in range(45)}

    candidates = {}

    def find(individual, start):
        def swap_num(i1, i2):
            tmp = mutant[i1][1]
            mutant[i1][1] = mutant[i2][1]
            mutant[i2][1] = tmp
            return ((i1, i2), (mutant[i1][1], mutant[i2][1]))
        
        def foo(x, k):
            for i in range(k, 45):
                for td, x_dec, y_dec in test_data[i]:
                    if calc(x, copy.deepcopy(td), x_dec, y_dec) > 0:
                        return 1
            return 0

        if len(individual[1]) > 4:
            return None

        for k in range(start, 0, -1):
            result = foo(individual[0], k)

            if result == 0:
                print(k, "is okay")
                if k == 0:
                    return individual
                continue
            elif len(individual[1]) >= 4:
                print("backtracking")
                return None
            print("fixing", k)

            if k in candidates:
                for swap in candidates[k]:
                    mutant, swaps = copy.deepcopy(individual)
                    swaps.append(swap)
                    if foo(mutant, k) == 0:
                        print(k, "is okay", "with", swaps)
                        result = find(copy.deepcopy((mutant, swaps)), k - 1)
                        if result is None:
                            print("backtracking to", k)
                            continue
                        else:
                            return result

            cnt = 0
            for i in range(len(wires)):
                for j in range(i):
                    cnt += 1
                    if cnt % 100 == 0:
                        print(f"{k}: {cnt}")
                    if do_skip(i, j, individual[1]):
                        continue

                    mutant, swaps = copy.deepcopy(individual)
                    swaps.append(swap_num(i, j))

                    if foo(mutant, k) == 0:
                        print(k, "is okay", "with", swaps)
                        if k not in candidates:
                            candidates[k] = set()
                        candidates[k].add(swaps[-1])
                        result = find(copy.deepcopy((mutant, swaps)), k - 1)
                        if result is None:
                            print("backtracking to", k)
                            continue
                        else:
                            return result
            return None
        return individual

    individual = find(individual, 44)

    swaps = individual[1]
    print("number of swaps =", len(swaps))
    result = set()
    for swap in swaps:
        result.add(swap[1][0])
        result.add(swap[1][1])
    print("number of unique wires =", len(result))
    print(",".join(sorted(result)))

if __name__ == '__main__':
    # solve_1()
    solve_2()