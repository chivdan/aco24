from enum import Enum
import heapq
import itertools
import math


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

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

def solve(max_cheats):
    m = [[v for v in line.strip()] for line in open("input.txt")]
    h = len(m)
    w = len(m[0])

    start = None
    end = None
    for i in range(h):
        for j in range(w):
            if m[i][j] == "S":
                start = (i, j)
                m[i][j] = "."
            elif m[i][j] == "E":
                end = (i, j) 
                m[i][j] = "."

    def dijkstra(s):
        d = [[math.inf for _ in range(len(m[0]))] for _ in range(len(m))]
        d[s[0]][s[1]] = 0
        q = []
        heapq.heappush(q, (0, s))
        visited = set()
        
        while q:
            _, (i, j) = heapq.heappop(q)
            if (i, j) in visited:
                continue

            visited.add((i, j))

            for dd in [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]:
                ni, nj = next_cell(i, j, dd)
                if ni < 0 or nj < 0 or ni >= len(m) or nj >= len(m[0]):
                    continue

                if m[ni][nj] != "#":
                    if d[i][j] + 1 <= d[ni][nj]:
                        d[ni][nj] = d[i][j] + 1
                        heapq.heappush(q, (d[ni][nj], (ni, nj)))

        return d


    d_start = dijkstra(start)
    d_end = dijkstra(end)

    fair_cost = d_start[end[0]][end[1]]

    result = 0    
    gain = 100
    for i in range(h):
        for j in range(w):
            for di in range(-max_cheats, max_cheats + 1):
                for dj in range(-max_cheats, max_cheats + 1):
                    if abs(di) + abs(dj) > max_cheats:
                        continue
                    ni = i + di
                    nj = j + dj
                    if ni < 0 or nj < 0 or ni >= len(m) or nj >= len(m[0]):
                        continue
                    if d_start[i][j] + d_end[ni][nj] + abs(di) + abs(dj) <= fair_cost - gain:
                        result += 1
    print(result)


if __name__ == '__main__':
    solve(2)
    solve(20)