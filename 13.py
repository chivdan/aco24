def round_to_nearest_int(a):
    import math
    return math.floor(a) if a - math.floor(a) < 0.5 else math.ceil(a)

def solve(offset):
    data = []
    game = []
    for line in open('input.txt'):
        line = line.replace(",", "")
        if "Button A" in line:
            _, _, x, y = line.split()
            a_x = int(x.replace("X+", ""))
            a_y = int(y.replace("Y+", ""))
            game.append((a_x, a_y))
        elif "Button B" in line:
            _, _, x, y = line.split()
            b_x = int(x.replace("X+", ""))
            b_y = int(y.replace("Y+", ""))
            game.append((b_x, b_y))
        elif "Prize" in line:
            _, x, y = line.split()
            goal_x = int(x.replace("X=", ""))
            goal_y = int(y.replace("Y=", ""))
            goal_x += offset
            goal_y += offset
            game.append((goal_x, goal_y))
            data.append(game)
            game = []

    result = 0
    for game in data:
        a_x, a_y = game[0]
        b_x, b_y = game[1]
        g_x, g_y = game[2]

        if a_x == 0:
            raise ValueError("a_x == 0")

        if abs((b_y - b_x * a_y/a_x)) < 1e-6:
            raise ValueError("b_y - b_x * a_y/a_x == 0")

        n_b = (g_y - g_x * a_y/a_x) / (b_y - b_x * a_y/a_x)
        n_a = (g_x - n_b * b_x) / a_x

        int_n_a = round_to_nearest_int(n_a)
        int_n_b = round_to_nearest_int(n_b)

        if abs(a_x * int_n_a + b_x * int_n_b - g_x) < 1e-6 and abs(a_y * int_n_a + b_y * int_n_b - g_y) < 1e-6:
            result += int_n_a * 3 + int_n_b


    print(result)

if __name__ == '__main__':
    solve(0)
    solve(10000000000000)