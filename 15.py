from importlib import simple


def find_start(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "@":
                return (i, j)
    return None, None

def can_move_simple(m, robot_pos, direction):
    r_i, r_j = robot_pos

    if direction == "^":
        found_space_before_wall = False
        for i in range(r_i - 1, -1, -1):
            if m[i][r_j] == "#":
                break
            if m[i][r_j] == ".":
                found_space_before_wall = True
                break
        return found_space_before_wall
    elif direction == "v":
        found_space_before_wall = False
        for i in range(r_i + 1, len(m)):
            if m[i][r_j] == "#":
                break
            if m[i][r_j] == ".":
                found_space_before_wall = True
                break
        return found_space_before_wall
    elif direction == "<":
        found_space_before_wall = False
        for j in range(r_j - 1, -1, -1):
            if m[r_i][j] == "#":
                break
            if m[r_i][j] == ".":
                found_space_before_wall = True
                break
        return found_space_before_wall
    elif direction == ">":
        found_space_before_wall = False
        for j in range(r_j + 1, len(m[0])):
            if m[r_i][j] == "#":
                break
            if m[r_i][j] == ".":
                found_space_before_wall = True
                break
        return found_space_before_wall

def solve_1():
    def move(robot_pos, direction):
        r_i, r_j = robot_pos
        if direction == "^":
            if m[r_i - 1][r_j] == "O":
                for i in range(r_i - 1, -1, -1):
                    if m[i][r_j] == "#":
                        break
                    if m[i][r_j] == ".":
                        m[i][r_j] = "O"
                        break
                    else:
                        m[i][r_j] = "O"
            m[r_i - 1][r_j] = "@"
            m[r_i][r_j] = "."
            robot_pos = (r_i - 1, r_j)

        elif direction == "v":
            if m[r_i + 1][r_j] == "O":
                for i in range(r_i + 1, len(m)):
                    if m[i][r_j] == "#":
                        break
                    if m[i][r_j] == ".":
                        m[i][r_j] = "O"
                        break
                    else:
                        m[i][r_j] = "O"
            m[r_i + 1][r_j] = "@"
            m[r_i][r_j] = "."
            robot_pos = (r_i + 1, r_j)
        elif direction == "<":
            if m[r_i][r_j - 1] == "O":
                for j in range(r_j - 1, -1, -1):
                    if m[r_i][j] == "#":
                        break
                    if m[r_i][j] == ".":
                        m[r_i][j] = "O"
                        break
                    else:
                        m[r_i][j] = "O"
            m[r_i][r_j - 1] = "@"
            m[r_i][r_j] = "."
            robot_pos = (r_i, r_j - 1)
        elif direction == ">":
            if m[r_i][r_j + 1] == "O":
                for j in range(r_j + 1, len(m[0])):
                    if m[r_i][j] == "#":
                        break
                    if m[r_i][j] == ".":
                        m[r_i][j] = "O"
                        break
                    else:
                        m[r_i][j] = "O"
            m[r_i][r_j + 1] = "@"
            m[r_i][r_j] = "."
            robot_pos = (r_i, r_j + 1)
        return robot_pos

    m = []
    directions = []
    for line in open("input.txt"):
        if "#" in line:
            m.append([v for v in line.strip()])
        elif line:
            directions.extend([v for v in line.strip()])

    robot_pos = find_start(m)

    for d in directions:
        will_move = can_move_simple(m, robot_pos, d)
        if will_move:
            robot_pos = move(robot_pos, d)

    result = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "O":
                result += 100*i + j
    print(result)

def solve_2():
    def can_move(robot_pos, direction):
        if not can_move_simple(m, robot_pos, direction):
            return False

        r_i, r_j = robot_pos
        if direction == "^":
            if m[r_i - 1][r_j] == "[":
                return can_move((r_i - 1, r_j), direction) and can_move((r_i - 1, r_j + 1), direction)
            elif m[r_i - 1][r_j] == "]":
                return can_move((r_i - 1, r_j), direction) and can_move((r_i - 1, r_j - 1), direction)
        elif direction == "v":
            if m[r_i + 1][r_j] == "[":
                return can_move((r_i + 1, r_j), direction) and can_move((r_i + 1, r_j + 1), direction)
            elif m[r_i + 1][r_j] == "]":
                return can_move((r_i + 1, r_j), direction) and can_move((r_i + 1, r_j - 1), direction)
        return True

    def move_robot(robot_pos, direction):
        r_i, r_j = robot_pos
        if direction == "^":
            m[r_i - 1][r_j] = "@"
            m[r_i][r_j] = "."
            robot_pos = (r_i - 1, r_j)
        elif direction == "v":
            m[r_i + 1][r_j] = "@"
            m[r_i][r_j] = "."
            robot_pos = (r_i + 1, r_j)
        elif direction == "<":
            m[r_i][r_j - 1] = "@"
            m[r_i][r_j] = "."
            robot_pos = (r_i, r_j - 1)
        elif direction == ">":
            m[r_i][r_j + 1] = "@"
            m[r_i][r_j] = "."
            robot_pos = (r_i, r_j + 1)
        return robot_pos
    
    def move(pos, direction):
        r_i, r_j = pos
        if direction == "^":
            if m[r_i - 1][r_j] == "[":
                move((r_i - 1, r_j), direction)
                move((r_i - 1, r_j + 1), direction)
            elif m[r_i - 1][r_j] == "]":
                move((r_i - 1, r_j), direction)
                move((r_i - 1, r_j - 1), direction)
            if m[r_i - 1][r_j] == ".":
                m[r_i - 1][r_j] = m[r_i][r_j]
                m[r_i][r_j] = "."
        elif direction == "v":
            if m[r_i + 1][r_j] == "[":
                move((r_i + 1, r_j), direction)
                move((r_i + 1, r_j + 1), direction)
            elif m[r_i + 1][r_j] == "]":
                move((r_i + 1, r_j), direction)
                move((r_i + 1, r_j - 1), direction)
            if m[r_i + 1][r_j] == ".":
                m[r_i + 1][r_j] = m[r_i][r_j]
                m[r_i][r_j] = "."
        elif direction == "<":
            if m[r_i][r_j - 1] in ["[", "]"]:
                move((r_i, r_j - 1), direction)
            if m[r_i][r_j - 1] == ".":
                m[r_i][r_j - 1] = m[r_i][r_j]
                m[r_i][r_j] = "."
        elif direction == ">":
            if m[r_i][r_j + 1] in ["[", "]"]:
                move((r_i, r_j + 1), direction)
            if m[r_i][r_j + 1] == ".":
                m[r_i][r_j + 1] = m[r_i][r_j]
                m[r_i][r_j] = "."


    m = []
    directions = []
    for line in open("input.txt"):
        if "#" in line:
            row = []
            for c in line.strip():
                if c == "@":
                    row.extend(["@", "."])
                elif c == "O":
                    row.extend(["[", "]"])
                else:
                    row.extend([c]*2)
            m.append(row)
        elif line:
            directions.extend([v for v in line.strip()])

    robot_pos = find_start(m)


    for d in directions:
        will_move = can_move(robot_pos, d)
        if will_move:
            move(robot_pos, d)
            robot_pos = move_robot(robot_pos, d)
    
    result = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "[":
                result += 100*i + j
    print(result)

if __name__ == '__main__':
    solve_1()
    solve_2()