import itertools

def solve_1():
    def has_gaps():
        return any(m[i - 1] == '.' and m[i] != '.'
                   for i in range(1, len(m)))
    
    data = open("input.txt").read().strip()

    m = []
    cnt = 0
    for i, c in enumerate(list(data)):
        k = int(c)
        symbol = str(cnt) if i % 2 == 0 else '.'
        for j in range(k):
            m.append(symbol)
        if i % 2 == 0:
            cnt += 1
        
    i = 0
    j = len(m) - 1
    while has_gaps():
        if i >= j:
            break
        while m[i] != '.':
            i += 1
        while m[j] == '.':
            j -= 1
        m[i] = m[j]
        m[j] = '.'
    
    result = 0
    for i, c in enumerate(m):
        if c == '.':
            break
        result += i * int(c)
    print(result)
    
def solve_2():
    data = open("input.txt").read().strip()
    gaps = {}
    nums = {}

    pos = 0
    cnt = 0
    for i, c in enumerate(list(data)):
        length = int(c) 
        if i % 2 == 0:
            # create new id
            nums[cnt] = (pos, length)
            cnt += 1
        elif length > 0:
            # create new gap
            gaps[pos] = length
        pos += length

    # go over the nums in descending order
    ids = sorted(nums.keys(), reverse=True)

    for num in ids:
        num_start, num_len = nums[num]

        # try to move to the leftmost fitting gap
        for gap_start in sorted(gaps.keys()):
            # do not move right
            if gap_start > num_start:
                break
            gap_len = gaps[gap_start]
            if gap_len >= num_len:
                # move the num to the beginning of the gap
                nums[num] = (gap_start, num_len)
 
                # add a gap where the num had been
                gaps[num_start] = num_len
                
                # adjust the gap where we moved the num

                # remove the old gap
                gaps.pop(gap_start)

                # create a new gap if needed
                if gap_len > num_len:
                    new_gap_start = gap_start + num_len 
                    assert new_gap_start not in gaps
                    new_gap_len = gap_len - num_len
                    gaps[new_gap_start] = new_gap_len

                # merge consecutive gaps
                while True:
                    merged = False
                    for gap1, gap2 in itertools.pairwise(sorted(gaps.keys())):
                        if gap1 + gaps[gap1] == gap2:
                            gaps[gap1] += gaps[gap2]
                            gaps.pop(gap2)
                            merged = True
                            break
                    if not merged: 
                        break
                break

    result = 0
    for num in list(sorted(nums.keys())):
        num_start, num_len = nums[num]
        for pos in range(num_start, num_start + num_len):
            result += pos * num

    print(result)

if __name__ == '__main__':
    solve_1()
    solve_2()