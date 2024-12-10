import math

def solve_1():
    def generate_antinodes(a, b):
        i1, j1 = a
        i2, j2 = b

        dx = i2 - i1
        dy = j2 - j1

        return [(i1 - dx, j1 - dy), (i2 + dx, j2 + dy)]

    def in_bounds(a):
        i, j = a
        return 0 <= i < len(m) and 0 <= j < len(m[i])

    m = [[v for v in line.strip()] for line in open("input.txt")]
    freqs = {}
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == ".":
                continue
            if m[i][j] not in freqs:
                freqs[m[i][j]] = [(i, j)]
            else:
                freqs[m[i][j]].append((i, j))

    result = set()
    for freq, positions in freqs.items():
        if len(positions) == 1:
            continue
        for i in range(len(positions)):
            for j in range(i):
                a = positions[i]
                b = positions[j]

                for antinode in generate_antinodes(a, b):
                    if in_bounds(antinode):
                        result.add(antinode)
    print(len(result))

        

def solve_2():
    def round_to_nearest_int(a):
        return math.floor(a) if a - math.floor(a) < 0.5 else math.ceil(a)

    def generate_antinodes(a, b):
        i1, j1 = a
        i2, j2 = b

        dx = i2 - i1
        dy = j2 - j1

        if dx == 0:
            return {(i1, j) for j in range(len(m[0]))}
        if dy == 0:
            return {(i, j1) for i in range(len(m))}

        k = dy / dx

        antinodes = set()
        antinodes.add((i1, j1))

        for i in range(len(m)):
            for j in range(len(m[i])):
                if i == i1 or j == j1:
                    continue
                k1 = (j - j1) / (i - i1)
                if abs(k1 - k) < 0.0001:
                    antinodes.add((i, j))
        return antinodes

    def in_bounds(a):
        i, j = a
        return 0 <= i < len(m) and 0 <= j < len(m[0])

    m = [[v for v in line.strip()] for line in open("input.txt")]
    freqs = {}
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == ".":
                continue
            if m[i][j] not in freqs:
                freqs[m[i][j]] = [(i, j)]
            else:
                freqs[m[i][j]].append((i, j))

    result = set()
    for freq, positions in freqs.items():
        if len(positions) == 1:
            continue
        for i in range(len(positions)):
            for j in range(i):
                a = positions[i]
                b = positions[j]

                for antinode in generate_antinodes(a, b):
                    result.add(antinode)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (i, j) in result:
                print("#", end="")
            else:
                print(m[i][j], end="")
        print()
    print(len(result))

if __name__ == '__main__':
    solve_1()
    solve_2()
