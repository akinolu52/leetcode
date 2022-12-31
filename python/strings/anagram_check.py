
# check if the pattern given is a valid anagram for the string

def rearrange_string(str):
    str = list(str)
    str.sort()

    return ''.join(str)


str = 'bcdcbaba'

pattern = 'bac'

rearranged_pattern = rearrange_string(pattern)
is_anagram = False

for index in range(len(str)):
    substring = str[index: index + len(pattern)]

    if len(substring) != len(pattern):
        break

    if rearranged_pattern == rearrange_string(substring):
        is_anagram = True
        break

print("Pattern {} {} an anagram of {}".format(
    pattern, "is" if is_anagram else "is not", str))
