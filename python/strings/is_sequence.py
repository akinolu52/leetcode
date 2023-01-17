def isSubsequence(s: str, t: str) -> bool:
    # check = True

    lastIndex = -1

    if t.find(s) != -1:
        return True

    for ch in s:
        chIndex = t.find(ch)
        print(ch, chIndex)

        if chIndex == -1:
            return False
        if lastIndex > chIndex:
            return False

        # remove that current index from the string
        t = t.replace(ch, '#', 1)
        lastIndex = chIndex

    return True


def isSubsequence2(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    i = j = c = 0
    while i < len(s) and j < len(t):
        if (s[i] == t[j]):
            i += 1
            j += 1
            c += 1
        else:
            j += 1
    return True if c == len(s) else False


s = "leeeeetcode"
t = "leeeeeetcode"

print(isSubsequence(s, t), t.replace('y', ''))
print(isSubsequence2(s, t))

# leeeeetcode
# leeeeeetcode