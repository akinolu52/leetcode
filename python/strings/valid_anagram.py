s = "anagram"
t = "nagaram"


def rearrangeString(_s: str):
    _s = list(_s)
    _s.sort()

    return ''.join(_s)


if len(s) != len(t):
    print(False)
    # return False

print(True if rearrangeString(s) == rearrangeString(t) else False)
