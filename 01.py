def solve_1():
    data = [[int(v) for v in line.split()] for line in open("input.txt")]
    first = sorted([v[0] for v in data])
    second = sorted([v[1] for v in data])
    print(sum(abs(first[i] - second[i]) for i in range(len(first))))

def solve_2():
    data = [[int(v) for v in line.split()] for line in open("input.txt")]
    first = [v[0] for v in data]
    second = [v[1] for v in data]

    result = sum(number * second.count(number) for number in first)
    print(result)

if __name__ == '__main__':
    solve_1()
    solve_2()