import itertools


def solve_1():
    lhs, rhs = [], []
    for line in open('simple.txt'):
        l, r = line.strip().split(':')
        lhs.append(int(l.strip()))
        rhs.append([int(v) for v in r.split()])

    ops = ["+", "*"]

    result = 0
    for l, r in zip(lhs, rhs):
        n = len(r)
        for op_comb in itertools.product(ops, repeat=n - 1):  
            expr = "("*(n - 1) + str(r[0])
            for i in range(1,n):
                expr += op_comb[i - 1] + str(r[i]) + ")"
            x = eval(expr, globals(), locals())
            if x == l:
                result += l
                break    
    print(result)


def solve_2():
    lhs, rhs = [], []
    for line in open('input.txt'):
        l, r = line.strip().split(':')
        lhs.append(int(l.strip()))
        rhs.append([int(v) for v in r.split()])

    ops = ["+", "*", ""]

    result = 0
    for k, (l, r) in enumerate(zip(lhs, rhs)):
        print(f"{k}/{len(lhs)}")
        n = len(r)
        for op_comb in itertools.product(ops, repeat=n - 1):
            expr = r[0]
            for i in range(1,n):
                op = op_comb[i - 1]
                if op == "+":
                    expr += r[i]
                elif op == "*":
                    expr *= r[i]
                else:
                    expr = int(str(expr) + str(r[i]))
            if expr == l:
                result += l
                break            
    print(result)


if __name__ == '__main__':
    solve_1()
    solve_2()
