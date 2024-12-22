from functools import cache


def solve_1():
    def possible(s):
        result = False
        if len(s) == 0:
            return True
        for comb in combinations:
            if s.startswith(comb):
                if possible(s[len(comb):]):
                    result = True
                    break   
        return result
    
    combinations = None
    strings = []
    for line in open("input.txt"):
        if not line.strip():
            continue
        if combinations is None:
            combinations = [v.strip() for v in line.strip().split(",")]
        else:
            strings.append(line.strip())

    result = sum(1 for s in strings if possible(s))
    print(result)


def solve_2():
    @cache
    def count_possible_combinations(s):
        if len(s) == 0:
            return 1
        total_count = 0
        for comb in combinations:
            if s.startswith(comb):
                count = count_possible_combinations(s[len(comb):])
                total_count += count
        return total_count


    combinations = None
    strings = []
    for line in open("input.txt"):
        if not line.strip():
            continue
        if combinations is None:
            combinations = [v.strip() for v in line.strip().split(",")]
        else:
            strings.append(line.strip())

    result = sum(count_possible_combinations(s) for s in strings)
    print(result)

if __name__ == '__main__':
    solve_1()
    solve_2()