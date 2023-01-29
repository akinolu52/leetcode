
def decodeString(s: str) -> str:
    stack = []
    intStack = []
    sIndex = []

    for idx, ch in enumerate(s):
        if ch == ']':
            # loop forward till you get the last number
            numIdxStart = i = intStack.pop()
            print('numIdxStart ', numIdxStart)
            multiplierArr = []

            # while i < idx:
            #     multiplierArr.append(s[i])
            #     i += 1

            # multiplier = ''.join(map(str,multiplierArr))

            # print('stack -> ', stack, multiplier)

        else:
            if ch.isdigit():
                intStack.append(ch)
            stack.append(ch)

    return ''.join(stack)


# print(decodeString("3[a]2[bc]"))
# print(decodeString("3[a2[c]]"))  # "accaccacc"
# print(decodeString("2[abc]3[cd]ef"))  # abcabccdcdcdef
print(decodeString("100[leetcode]"))  # abcabccdcdcdef
