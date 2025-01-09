
def solve_1():
    def convert(m):
        if m[0][0] == ".":
            # key
            key = []
            for j in range(len(m[0])):
                key.append(sum(m[i][j] == "#" for i in range(len(m))) - 1)
            keys.append(key)
        elif m[0][0] == "#":
            # lock
            lock = []
            for j in range(len(m[0])):
                lock.append(sum(m[i][j] == "#" for i in range(len(m))) - 1)
            locks.append(lock)


    locks = []
    keys = []

    m = []
    for line in open('input.txt'):
        line = line.strip()
        if line:
            m.append([c for c in line])

        if not line:
            convert(m)
            m = []
    
    if m:
        convert(m)

    result = set()
    for i, key in enumerate(keys):
        for j, lock in enumerate(locks):
            if all(key[k] + lock[k] <= 5 for k in range(len(key))):
                result.add((i, j))
    print(len(result))


if __name__ == '__main__':
    solve_1()
