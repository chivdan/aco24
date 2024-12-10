def solve(part1):
    def count_arrowheads(i, j):
        q = [(i, j)]
        if part1:
            result = set()
        else:
            result = []
        while q:
            x, y = q.pop(0)
            value = m[x][y]
            if value == 9:
                if part1:
                    result.add((x, y))
                else:
                    result.append((x, y))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if x + dx < 0 or x + dx >= len(m) or y + dy < 0 or y + dy >= len(m[x]):
                    continue 
                if m[x + dx][y + dy] == value + 1:
                    q.append((x + dx, y + dy))
        return len(result)

    m = [[int(v) for v in line.strip()] for line in open("input.txt")]
    result = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                result += count_arrowheads(i, j)
    print(result)

if __name__ == '__main__':
    solve(part1=True)
    solve(part1=False)