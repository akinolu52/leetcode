
def findTheDifference(s: str, t: str) -> str:
    for ch in t:
        if s.count(ch) != t.count(ch):
            return ch


s = "abcd"
t = "abcde"

print(findTheDifference(s, t))

s = "a"
t = "aa"

print(findTheDifference(s, t))
