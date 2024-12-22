def mix(value, number):
    return value ^ number

def prune(number):
    return number % 16777216

def next_number(number):
    number = prune(mix(number * 64, number))
    number = prune(mix(number // 32, number))
    return prune(mix(number * 2048, number))

def solve_1():
    data = [int(line.strip()) for line in open('input.txt').readlines()]

    result = 0
    for number in data:
        for _ in range(2000):
            number = next_number(number)
        result += number
    print(result)


def solve_2():
    data = [int(line.strip()) for line in open('input.txt').readlines()]

    buyers = {}
    for number in data:
        bananas = []
        changes = []
        bananas.append(number % 10)
        changes.append(None)
        for _ in range(2000):
            number = next_number(number)
            bananas.append(number % 10)
            changes.append(bananas[-1] - bananas[-2])
        buyers[number] = {"bananas": bananas, "changes": changes}

    quadruples = set()
    cnt = 0
    for buyer in buyers:
        print("preprocessing", f"{cnt + 1}/{len(buyers)}")
        cnt += 1
        quadruples_buyer = set()
        bananas_buyer = {}
        bananas = buyers[buyer]["bananas"]
        changes = buyers[buyer]["changes"]
        for i in range(1, len(changes) - 4):
            seq = (changes[i], changes[i + 1], changes[i + 2], changes[i + 3])
            if seq not in quadruples_buyer:
                quadruples_buyer.add(seq)
                bananas_buyer[seq] = bananas[i + 3]
        quadruples = quadruples.union(quadruples_buyer)
        buyers[buyer]["bananas_seq"] = bananas_buyer
        buyers[buyer]["quadruples"] = quadruples_buyer

    max_bananas = 0
    cnt = 0
    for seq in quadruples:
        print(f"{cnt + 1}/{len(quadruples)}")
        cnt += 1
        result_seq = 0
        for buyer in buyers:
            bananas_seq = buyers[buyer]["bananas_seq"]
            quadruples_buyer = buyers[buyer]["quadruples"]
            if seq in quadruples_buyer:
                result_seq += bananas_seq[seq]
        if result_seq > max_bananas:
            max_bananas = result_seq
    print(max_bananas)

if __name__ == '__main__':
    solve_1()
    solve_2()