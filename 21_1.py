import itertools

def solve_1():
    directional_paths = {
        ("A", "^"): ["<"],
        ("A", "v"): ["<", "v"],
        ("A", "<"): ["v", "<", "<"],
        ("A", ">"): ["v"],
        ("A", "A"): [],

        ("^", "A"): [">"],
        ("^", "<"): ["v", "<"],
        ("^", ">"): ["v", ">"],
        ("^", "v"): ["v"],
        ("^", "^"): [],

        ("<", "A"): [">", ">", "^"],
        ("<", ">"): [">", ">"],
        ("<", "^"): [">", "^"],
        ("<", "v"): [">"],
        ("<", "<"): [],

        (">", "A"): ["^"],
        (">", "<"): ["<", "<"],
        (">", "^"): ["<", "^"],
        (">", "v"): ["<"],
        (">", ">"): [],

        ("v", "A"): ["^", ">"],
        ("v", "<"): ["<"],
        ("v", ">"): [">"],
        ("v", "^"): ["^"],
        ("v", "v"): [],
    }

    m = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
    symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A"]
    coord = {}
    for symbol in symbols:
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == symbol:
                    coord[symbol] = (i, j)


    code_nums = {
        "083A": 83,
        "935A": 935,
        "964A": 964,
        "149A": 149,
        "789A": 789
    }

    codes = {
        "083A": "<A^^^Avv>AvA",  #66
        "935A": "^^^AvvA<^Avv>A",   #70
        "964A": "^^^AvA<<A>>vvA",  #72
        "149A": "^<<A^A^>>AvvvA", #76
        "789A": "^^^<<A>A>AvvvA"   #65
    }

    result = 0
    for numerical_code, first_directional_code in codes.items(): 
        second_directional = []
        for c1, c2 in itertools.pairwise(["A"] + [c for c in first_directional_code]):
            second_directional.extend(directional_paths[(c1, c2)])
            second_directional.append("A")
        
        third_directional = []
        for c1, c2 in itertools.pairwise(["A"] + second_directional):
            third_directional.extend(directional_paths[(c1, c2)])
            third_directional.append("A")

        result += code_nums[numerical_code] * len(third_directional)
    print(result)

if __name__ == '__main__':
    solve_1()