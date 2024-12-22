from functools import cache
import itertools

def solve_2():
    directional_paths = {
        ("A", "^"): "<",
        ("A", "v"): "<v",
        ("A", "<"): "v<<",
        ("A", ">"): "v",
        ("A", "A"): "",

        ("^", "A"): ">",
        ("^", "<"): "v<",
        ("^", ">"): "v>",
        ("^", "v"): "v",
        ("^", "^"): "",

        ("<", "A"): ">>^",
        ("<", ">"): ">>",
        ("<", "^"): ">^",
        ("<", "v"): ">",
        ("<", "<"): "",

        (">", "A"): "^",
        (">", "<"): "<<",
        (">", "^"): "<^",
        (">", "v"): "<",
        (">", ">"): "",

        ("v", "A"): "^>",
        ("v", "<"): "<",
        ("v", ">"): ">",
        ("v", "^"): "^",
        ("v", "v"): "",

        (">", "A"): "^",
        (">", "<"): "<<",
        (">", "^"): "<^",
        (">", "v"): "<",
        (">", ">"): "",

        ("v", "A"): "^>",
        ("v", "<"): "<",
        ("v", ">"): ">",
        ("v", "^"): "^",
        ("v", "v"): ""
    }
  
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

    @cache
    def expand_p(sequence, pad_num):
        n = len(sequence)
        if n <= 4:
            if pad_num == 0:
                return len(sequence[1:])
            result = "A".join([directional_paths[(c1, c2)] for c1, c2 in itertools.pairwise(sequence)]) + "A"

            next_result = expand_p("A" + result, pad_num - 1)
            if isinstance(next_result, int):
                return next_result
            return len(next_result)
        else:
            l = sequence[:n // 2]
            m = sequence[n//2 - 1] + sequence[n//2]
            r = sequence[n // 2:]
            return expand_p(l, pad_num) + expand_p(m, pad_num) + expand_p(r, pad_num)

    result = 0
    for numerical_code, first_directional_code in codes.items(): 
        sequence = first_directional_code
        sequence = expand_p("A" + sequence, 25)
        result += code_nums[numerical_code] * sequence
    print(result)

if __name__ == '__main__':
    solve_2()
