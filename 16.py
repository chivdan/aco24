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

def solve_1():
    m = [[c for c in line.strip()] for line in open("input.txt")]

    start = None
    end = None
    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            if m[i][j] == "S":
                start = (i, j)
                m[i][j] = "."
            elif m[i][j] == "E":
                end = (i, j)

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
        for dd in [direction, direction.turn_left(), direction.turn_right()]:
            ni, nj = next_cell(i, j, dd)
            if m[ni][nj] != "#":
                cost_of_move = 1 if dd == direction else 1001
                if d[i][j] + cost_of_move < d[ni][nj]:
                    d[ni][nj] = d[i][j] + cost_of_move
                    heapq.heappush(q, (d[ni][nj], ((ni, nj), dd)))

    print(d[end[0]][end[1]]) 


def solve_2():
    m = [[c for c in line.strip()] for line in open("simple.txt")]

    start = None
    end = None
    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            if m[i][j] == "S":
                start = (i, j)
                m[i][j] = "."
            elif m[i][j] == "E":
                end = (i, j)

    def dijkstra(forbidden):
        d = [[math.inf for _ in range(len(m[0]))] for _ in range(len(m))]
        d[start[0]][start[1]] = 0
        q = []
        prev = {}
        heapq.heappush(q, (0, (start, Direction.EAST)))
        

        while q:
            _, ((i, j), direction) = heapq.heappop(q)
            for dd in [direction, direction.turn_left(), direction.turn_right()]:
                ni, nj = next_cell(i, j, dd)
                if ((ni, nj), dd) in forbidden:
                    continue
                if m[ni][nj] != "#":
                    cost_of_move = 1 if dd == direction else 1001
                    
                    if d[i][j] + cost_of_move <= d[ni][nj]:
                        d[ni][nj] = d[i][j] + cost_of_move
                        heapq.heappush(q, (d[ni][nj], ((ni, nj), dd)))

                        if (ni, nj) not in prev:
                            prev[(ni, nj)] = [((i, j, direction), cost_of_move)]
                        else:
                            prev[(ni, nj)].append(((i, j, direction), cost_of_move))
        return d, prev

    def dfs(i, j, path):
        if (i, j) == start:
            return [path]
        paths = []
        if (i, j) not in prev:
            return paths
        for p, cost in prev[(i, j)]:
            if (p, cost) in path:
                continue
            new_path = path.copy()
            new_path.append((p, cost))
            paths += dfs(p[0], p[1], new_path)
        return paths

    paths = []

    d, prev = dijkstra([])
    best = d[end[0]][end[1]]

    path= dfs(end[0], end[1], [(end, 0)])[0]
    paths.append(path)

    potential_forbidden = []
    for node in path[1:]:
        potential_forbidden.append(node[0])

    for (i, j, direction) in potential_forbidden:
        forbidden = [((i, j), direction)]
        d, prev = dijkstra(forbidden)
        for path in dfs(end[0], end[1], [(end, 0)]):
            if d[end[0]][end[1]] == best:
                paths.append(path)

    path_nodes = set()
    for path in paths:
        if sum(cost for _, cost in path) == d[end[0]][end[1]]:
            for p, cost in path:
                path_nodes.add((p[0], p[1]))

    for i in range(len(m)):
        for j in range(len(m[i])):
            if (i, j) in path_nodes:
                print("O", end="")
            else:
                print(m[i][j], end="")
        print()

    print(len(path_nodes))

if __name__ == '__main__':
    solve_1()
    solve_2()