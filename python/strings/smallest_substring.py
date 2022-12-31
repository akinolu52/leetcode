'''
find the smallest substrings
which contains all characters of pattern
'''

s = 'badeaebcaae'
p = 'aabc'


def rearrange_string(str):
    str = list(str)
    str.sort()

    return ''.join(str)


p = rearrange_string(p)


for index in range(len(s)):
    substring = s[index: index + len(p)]

    if len(substring) != len(p):
        break

    if rearrange_string(substring) == p:
        print(substring)
