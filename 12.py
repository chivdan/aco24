
def solve_1():
    m = [[v for v in line.strip()] for line in open('input.txt')]

    n_colors = 0
    color = {}

    cnt = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            cnt += 1
            if (i, j) in color:
                continue            
            # start bfs
            q = [(i, j)]
            while q:
                x, y = q.pop(0)
                if (x, y) not in color:
                    color[x, y] = n_colors
                for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    if 0 <= x + dx < len(m) and 0 <= y + dy < len(m[x]) and m[x + dx][y + dy] == m[x][y] and (x + dx, y + dy) not in color and (x + dx, y + dy) not in q:
                        q.append((x + dx, y + dy))
            n_colors += 1
    
    area = {c: 0 for c in range(n_colors)}
    perimeter = {c: 0 for c in range(n_colors)}
    for (i, j), c in color.items():
        area[c] += 1

        if i == 0 or i == len(m) - 1:
            perimeter[c] += 1
        if j == 0 or j == len(m[i]) - 1:
            perimeter[c] += 1
        if i > 0 and color[i - 1, j] != c:
            perimeter[c] += 1
        if j > 0 and color[i, j - 1] != c:
            perimeter[c] += 1
        if i < len(m) - 1 and color[i + 1, j] != c:
            perimeter[c] += 1
        if j < len(m[i]) - 1 and color[i, j + 1] != c:
            perimeter[c] += 1

    result = 0
    for c in range(n_colors):
        result += area[c] * perimeter[c]
    print(result)


def solve_2():
    m = [[v for v in line.strip()] for line in open('input.txt')]

    n_colors = 0
    color = {}

    cnt = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            cnt += 1
            if (i, j) in color:
                continue            
            # start bfs
            q = [(i, j)]
            while q:
                x, y = q.pop(0)
                if (x, y) not in color:
                    color[x, y] = n_colors
                for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    if 0 <= x + dx < len(m) and 0 <= y + dy < len(m[x]) and m[x + dx][y + dy] == m[x][y] and (x + dx, y + dy) not in color and (x + dx, y + dy) not in q:
                        q.append((x + dx, y + dy))
            n_colors += 1
    
    area = {c: 0 for c in range(n_colors)}
    sides = {c: {'top': set(),
                                            'bottom': set(),
                                            'left': set(), 
                                            'right': set()} for c in range(n_colors)}
    
    nsides = {c: 0 for c in range(n_colors)}
    
    for (i, j), c in color.items():
        area[c] += 1

        if i == 0:
            sides[c]['top'].add((i, j))
        if i == len(m) - 1:
            sides[c]['bottom'].add((i, j))
        if j == 0:
            sides[c]['left'].add((i, j))
        if j == len(m[i]) - 1:
            sides[c]['right'].add((i, j))
        if i > 0 and color[i - 1, j] != c:
            sides[c]['top'].add((i, j))
        if j > 0 and color[i, j - 1] != c:
            sides[c]['left'].add((i, j))
        if i < len(m) - 1 and color[i + 1, j] != c:
            sides[c]['bottom'].add((i, j))
        if j < len(m[i]) - 1 and color[i, j + 1] != c:
            sides[c]['right'].add((i, j))

    for c in range(n_colors):
        for side_group in sides[c].values():
            # split the side group into connected components: this will give us the number of sides
            side_group = sorted(side_group)
            components = []
            for (i, j) in side_group:
                found = False
                for component in components:
                    for (i2, j2) in component:
                        if abs(i - i2) + abs(j - j2) == 1:
                            component.add((i, j))
                            found = True
                            break
                    if found:
                        break
                if not found:
                    components.append({(i, j)})

            nsides[c] += len(components)
                
    result = sum(area[c] * nsides[c] for c in range(n_colors))
    print(result)

if __name__ == '__main__':
    solve_1()
    solve_2()