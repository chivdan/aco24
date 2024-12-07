


def solve_1():
    def find_xmas(i, j):
        result = set()
        # left to right
        if j + 3 < len(m[i]) and m[i][j + 1] == "M" and m[i][j + 2] == "A" and m[i][j + 3] == "S":
            result.add((i, j, i, j + 3))
        # right to left
        if j - 3 >= 0 and m[i][j - 1] == "M" and m[i][j - 2] == "A" and m[i][j - 3] == "S":
            result.add((i, j, i, j - 3))
        # top to bottom
        if i + 3 < len(m) and m[i + 1][j] == "M" and m[i + 2][j] == "A" and m[i + 3][j] == "S":
            result.add((i, j, i + 3, j))
        # bottom to top
        if i - 3 >= 0 and m[i - 1][j] == "M" and m[i - 2][j] == "A" and m[i - 3][j] == "S":
            result.add((i, j, i - 3, j))
        # top-left to bottom-right
        if i + 3 < len(m) and j + 3 < len(m[i]) and m[i + 1][j + 1] == "M" and m[i + 2][j + 2] == "A" and m[i + 3][j + 3] == "S":
            result.add((i, j, i + 3, j + 3))
        # top-right to bottom-left
        if i + 3 < len(m) and j - 3 >= 0 and m[i + 1][j - 1] == "M" and m[i + 2][j - 2] == "A" and m[i + 3][j - 3] == "S":
            result.add((i, j, i + 3, j - 3))
        # bottom-left to top-right
        if i - 3 >= 0 and j + 3 < len(m[i]) and m[i - 1][j + 1] == "M" and m[i - 2][j + 2] == "A" and m[i - 3][j + 3] == "S":
            result.add((i, j, i - 3, j + 3))
        # bottom-right to top-left
        if i - 3 >= 0 and j - 3 >= 0 and m[i - 1][j - 1] == "M" and m[i - 2][j - 2] == "A" and m[i - 3][j - 3] == "S":
            result.add((i, j, i - 3, j - 3))
        return result

    m = [[v for v in line] for line in open("input.txt")]

    positions = set()

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "X":
                positions |= find_xmas(i, j)
    print(len(positions))

def solve_2():
    def find_x_mas(i, j):
        cnt = 0
        if i + 1 < len(m) and j + 1 < len(m[i]) and i - 1 >= 0 and j - 1 >= 0:
            diag_1 ="".join(sorted([m[i + 1][j + 1], m[i - 1][j - 1]]))
            diag_2 = "".join(sorted([m[i + 1][j - 1], m[i - 1][j + 1]]))
            if diag_1 == "MS":
                cnt += 1
            if diag_2 == "MS":
                cnt += 1
        return int(cnt == 2)

    m = [[v for v in line[:-1]] for line in open("input.txt")]

    result = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "A":
                result += find_x_mas(i, j)
    print(result)

if __name__ == '__main__':
    solve_1()
    solve_2()