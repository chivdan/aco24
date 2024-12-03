import re

def solve_1():
    MUL_PATTERN = re.compile(f"mul\\(([0-9]+),\\s*([0-9]+)\\)")
    result = sum(sum(int(a) * int(b) for a, b in MUL_PATTERN.findall(line))
                      for line in open("input.txt"))
    print(result)

def calc_str(line):
    return sum(int(a) * int(b) for a, b in MUL_PATTERN.findall(line))

def solve_2():
    result = 0
    pattern = re.compile("do\\(\\)|don't\\(\\)|mul\\(([0-9]+),\\s*([0-9]+)\\)")
    do = True
    for line in open("input.txt"):
        for m in pattern.finditer(line):
            if m.group(0) == "do()":
                do = True
                continue
            elif m.group(0) == "don't()":
                do = False
                continue
            elif do:
                result += int(m.group(1)) * int(m.group(2))
    print(result)


if __name__ == '__main__':
    solve_1()
    solve_2()