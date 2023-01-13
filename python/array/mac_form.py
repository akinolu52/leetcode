
# m is 0 count
# n is 1 count
def findMaxForm(strs, m: int, n: int) -> int:
    res = 0
    for s in strs:
        count0 = len(s.replace('1', ''))
        count1 = len(s.replace('0', ''))
        print('str -> ', s, count0, count1)

        # check if count0 is m or count1 is n and skip
        if count0 == m and count1 == n:
            print('skip this')
            continue
        
        if count0 > m or count1 > n:
            continue

        if count0 <= m and count1 <= n:
            # continue
            res += 1

    return res


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(findMaxForm(strs, m, n))


strs = ["10","0","1"]
m = 1
n = 1
print(findMaxForm(strs, m, n))
