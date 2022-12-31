
def rearrange_string(str):
    str = list(str)
    str.sort()

    return ''.join(str)


str = "bcdcbabcbd"

pattern = "abc"

# rearrange the given pattern
pattern = rearrange_string(pattern)

all_anagrams = []

'''
find the substrings
check if the sorted substring is equal to the sorted pattern

'''
for index in range(len(str)):
    substring = str[index: index + len(pattern)]

    if len(substring) != len(pattern):
        break

    if rearrange_string(substring) == pattern:
        all_anagrams.append(substring)

print("All the anagram of '{}' present in '{}' are: {}".format(
    pattern, str, ', '.join(all_anagrams)))
