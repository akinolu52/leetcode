
def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


def strStr2(haystack: str, needle: str) -> int:
    for index in range(0, len(haystack)):
        sub_str = haystack[index: len(needle) + index]

        if len(sub_str) < len(needle):
            return -1
        print(sub_str, index, haystack)
        if (sub_str == needle):
            return index

    return -1


haystack = "sadbutsad"
needle = "sad"
print(strStr2(haystack, needle))

haystack = "leetcode"
needle = "leeto"
print(strStr2(haystack, needle))

haystack = "hello"
needle = "ll"
print(strStr2(haystack, needle))
