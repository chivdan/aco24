from enum import Enum
import heapq
import math


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def turn_left(self):
        if self == Direction.NORTH:
            return Direction.WEST
        elif self == Direction.EAST:
            return Direction.NORTH
        elif self == Direction.SOUTH:
            return Direction.EAST
        elif self == Direction.WEST:
            return Direction.SOUTH
        
    def turn_right(self):
        if self == Direction.NORTH:
            return Direction.EAST
        elif self == Direction.EAST:
            return Direction.SOUTH
        elif self == Direction.SOUTH:
            return Direction.WEST
        elif self == Direction.WEST:
            return Direction.NORTH
        
    def __lt__(self, other):
        return self.value < other.value


def next_cell(i, j, direction):
    if direction == Direction.NORTH:
        return (i - 1, j)
    elif direction == Direction.EAST:
        return (i, j + 1)
    elif direction == Direction.SOUTH:
        return (i + 1, j)
    elif direction == Direction.WEST:
        return (i, j - 1)

def solve(n_bytes):
    data = [[int(v) for v in line.split(",")] for line in open("input.txt")]
    
    w = 71
    h = 71
    
    m = [["." for i in range( w)] for j in range(h)]

    for n in range(n_bytes):
        m[data[n][1]][data[n][0]] = "#"

    start = (0, 0)
    end = (h - 1, w - 1)

    d = [[math.inf for _ in range(len(m[0]))] for _ in range(len(m))]
    d[start[0]][start[1]] = 0
    q = []
    heapq.heappush(q, (0, (start, Direction.EAST)))
    visited = set()
    
    while q:
        _, ((i, j), direction) = heapq.heappop(q)
        if (i, j, direction) in visited:
            continue
        visited.add((i, j, direction))
        for dd in [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]:
            ni, nj = next_cell(i, j, dd)
            if ni < 0 or nj < 0 or ni >= len(m) or nj >= len(m[0]):
                continue
            if m[ni][nj] != "#":
                cost_of_move = 1
                if d[i][j] + cost_of_move < d[ni][nj]:
                    d[ni][nj] = d[i][j] + cost_of_move
                    heapq.heappush(q, (d[ni][nj], ((ni, nj), dd)))

    return d[end[0]][end[1]] 


def solve_1():
    print(solve(1024))

def solve_2():
    data = [[int(v) for v in line.split(",")] for line in open("input.txt")]
    for i in range(1024, len(data)):
        if solve(i) == math.inf:
            print(i)
            print(data[i - 1])
            break

if __name__ == '__main__':
    solve_1()
    solve_2()