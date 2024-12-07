
def parse():
    before = {}
    updates = []
    for line in open("input.txt"):
        line = line.strip()
        if "|" in line:
            x, y = [int(v) for v in line.split("|")]
            if x in before:
                before[x].append(y)
            else:
                before[x] = [y]
        elif line:
            updates.append([int(v) for v in line.split(",")])
    return before, updates

def in_order(update, before) -> bool:
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] in before and update[i] in before[update[j]]:
                return False
    return True

def middle_page(update) -> int:
    assert len(update) % 2 == 1
    return update[len(update) // 2]

def solve_1():
    before, updates = parse()
    result = 0
    for update in updates:
        if in_order(update, before):
            result += middle_page(update)
    print(result)

        

def solve_2():
    class Page:
        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            if other.value in before and self.value in before[other.value]:
                return True
            return False


    before, updates = parse()
    result = 0
    for update in updates:
        if not in_order(update, before):
            update = sorted([Page(v) for v in update])
            result += middle_page([v.value for v in update])
    print(result)

if __name__ == '__main__':
    solve_1()
    solve_2()