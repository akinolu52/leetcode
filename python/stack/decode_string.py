
def decodeString(s: str) -> str:
    stack = []

    for ch in s:
        if ch != ']':
            stack.append(ch)
        else:
            charStack = []
            intStack = []
            numberSeen = False

            while stack:
                curr = stack.pop()
                if curr.isdigit():
                    numberSeen = True
                    intStack.append(curr)
                elif curr != '[' and numberSeen == False:
                    charStack.append(curr)

                if numberSeen:
                    break

            calc = ''.join(charStack)[::-1] * int(''.join(intStack)[::-1])
            stack.extend(list(calc))

    return ''.join(stack)


print(decodeString("3[a]2[bc]"))  # aaabcbc
print(decodeString("3[a2[c]]"))  # "accaccacc"
print(decodeString("2[abc]3[cd]ef"))  # abcabccdcdcdef
# print(decodeString("100[leetcode]"))  #
