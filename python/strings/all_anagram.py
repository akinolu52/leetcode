
'''
find the substrings
check if the sorted substring is equal to the sorted pattern

'''


def rearrange_string(s):
    s.sort()

    return ''.join(s)


s = "bcdcbabcbd"

pattern = "abc"

# rearrange the given pattern
pattern = rearrange_string(pattern)

all_anagrams = []

for index in range(len(s)):
    substring = s[index: index + len(pattern)]

    if len(substring) != len(pattern):
        break

    if rearrange_string(substring) == pattern:
        all_anagrams.append(substring)

print("All the anagram of '{}' present in '{}' are: {}".format(
    pattern, s, ', '.join(all_anagrams)))
