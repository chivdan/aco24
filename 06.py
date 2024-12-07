from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

    def move(self, pos):
        i, j = pos
        if self == Direction.NORTH:
            return (i - 1, j)
        elif self == Direction.SOUTH:
            return (i + 1, j)
        elif self == Direction.WEST:
            return (i, j - 1)
        elif self == Direction.EAST:
            return (i, j + 1)

    def turn(self):
        if self == Direction.NORTH:
            return Direction.EAST
        elif self == Direction.EAST:
            return Direction.SOUTH
        elif self == Direction.SOUTH:
            return Direction.WEST
        elif self == Direction.WEST:
            return Direction.NORTH

def parse():
    m = [[c for c in line.strip()] for line in open('input.txt')]    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '^':
                pos = (i, j)
                break
    return m, pos

def simulate_loop(m, pos):
    m[pos[0]][pos[1]] = '.'
    positions = set()
    direction = Direction.NORTH
    while True:
        positions.add(pos)
        next_pos = direction.move(pos)
        i_next, j_next = next_pos

        # out of bounds
        if i_next < 0 or i_next >= len(m) or j_next < 0 or j_next >= len(m[i_next]):
            break

        if m[i_next][j_next] == '.':
            pos = next_pos
        elif m[i_next][j_next] == '#':
            direction = direction.turn()
            next_pos = direction.move(pos)
            pos = next_pos

    return positions

def detect_loop(m, start_pos):
    pos = start_pos
    m[pos[0]][pos[1]] = '.'
    positions_visits = {}
    direction = Direction.NORTH
    while True:
        assert m[pos[0]][pos[1]] == '.'

        if (pos[0], pos[1], direction) in positions_visits:
            positions_visits[pos[0], pos[1], direction] += 1
            return None
        else:
            positions_visits[pos[0], pos[1], direction] = 1

        next_pos = direction.move(pos)
        i_next, j_next = next_pos

        # out of bounds
        if i_next < 0 or i_next >= len(m) or j_next < 0 or j_next >= len(m[i_next]):
            break

        if m[i_next][j_next] == '.':
            pass
        else: 
            cnt = 0
            while m[i_next][j_next] == '#' and cnt < 4:
                direction = direction.turn()
                next_pos = direction.move(pos)
                i_next, j_next = next_pos
                cnt += 1
            if cnt == 4:
                return None
        pos = next_pos

    return positions_visits

def solve_1():
    m, pos = parse()
    return simulate_loop(m, pos)
    


def solve_2():
    m, start_pos = parse()
    positions = set()
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '.':
                positions.add((i, j))

    result = 0
    for n, pos in enumerate(positions):
        print(f"{n}/{len(positions)}, result={result}")
        i, j = pos
        m[i][j] = "#"
        if detect_loop(m, start_pos) is None:
            result += 1
        m[i][j] = "."
    print(result)


if __name__ == '__main__':
    print(len(solve_1()))
    solve_2()