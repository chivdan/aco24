import copy


def solve_1():
    m = [int(v) for v in open("input.txt").read().strip().split()]

    for blink in range(25):
        m_new = []
        for stone in m:
            stone_str = str(stone)
            L = len(stone_str)
            if stone == 0:
                m_new.append(1)
            elif L % 2 == 0:
                m_new.append(int(stone_str[:L // 2]))
                m_new.append(int(stone_str[L // 2:]))
            else:
                m_new.append(stone * 2024)
        m = m_new
    print(len(m))

def add(stone, count, d):
    if stone not in d:
        d[stone] = count
    else:
        d[stone] += count

def solve_2():
    m = [int(v) for v in open("input.txt").read().strip().split()]

    d = {}
    for stone in m:
        add(stone, 1, d)

    for blink in range(75):
        d_new = {}
        for stone in d:
            stone_str = str(stone)
            L = len(stone_str)
            count = d[stone]
            if stone == 0:                
                add(1, count, d_new)
            elif L % 2 == 0:
                add(int(stone_str[:L // 2]), count, d_new)
                add(int(stone_str[L // 2:]), count, d_new)
            else:
                add(stone * 2024, count, d_new)
        d = d_new
    print(sum(d.values()))

if __name__ == '__main__':
    solve_1()
    solve_2()