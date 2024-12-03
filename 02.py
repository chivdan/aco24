import itertools

def is_increasing_and_safe(report):
    return all(a < b <= a + 3 for a, b in itertools.pairwise(report))

def is_safe(report):
    return is_increasing_and_safe(report) or is_increasing_and_safe(reversed(report))

def solve_1():
    data = [[int(v) for v in line.split()] for line in open("input.txt")]
    n_safe_reports= sum(is_safe(report) for report in data)
    print(n_safe_reports)        

def is_safe_tolerate_one(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def solve_2():
    data = [[int(v) for v in line.split()] for line in open("input.txt")]
    n_safe_reports= sum(is_safe_tolerate_one(report) for report in data)
    print(n_safe_reports)        

if __name__ == '__main__':
    solve_1()
    solve_2()