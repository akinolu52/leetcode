def isHappy(n: int) -> bool:
    if n == 1:
        return True

    def loopStr(nS):
        ret = ""
        for n in nS:
            ret = int(ret or 0) + (int(n) ** 2)
            # print('ret => ', ret)
            ret = str(ret)
        return ret

    nStr = str(n)
    seen = set()

    while True:
        nStr = loopStr(nStr)
        print('result => ', nStr)

        if int(nStr) == 1:
            return True
        
        if nStr in seen:
            return False
        else:
            seen.add(nStr)

# print(isHappy(4))
# print(isHappy(2))
# print(isHappy(19))
# print(isHappy(1111111))

# print(isHappy(2227))
