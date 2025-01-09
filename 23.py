import copy
import itertools


def solve_1():
    g = {}
    for line in open("input.txt"):
        l, r = line.strip().split("-")
        if l not in g:
            g[l] = set()
        g[l].add(r)
        if r not in g:
            g[r] = set()
        g[r].add(l)
    
    result = set()
    for node in g:
        for n1, n2 in itertools.combinations(g[node], 2):
            if not any(name.startswith("t") for name in [node, n1, n2]):
                continue
            if n1 in g and n2 in g[n1]:
                result.add(tuple(sorted([node, n1, n2])))
    print(len(result))

def solve_2():
    def clique(C, P, ans):
        if len(C) > len(ans):
            ans = C
        if len(C) + len(P) > len(ans):
            for node in copy.deepcopy(P):
                P.remove(node)
                Cprime = C.union({node})
                Prime = P.intersection(g[node])
                ans = clique(Cprime, Prime, ans)
        return ans
    
    g = {}
    for line in open("input.txt"):
        l, r = line.strip().split("-")
        if l not in g:
            g[l] = set()
        g[l].add(r)
        if r not in g:
            g[r] = set()
        g[r].add(l)

    ans = clique(set(), set(g.keys()), set())
    print(",".join(sorted(ans)))

if __name__ == '__main__':
    solve_1()
    solve_2()