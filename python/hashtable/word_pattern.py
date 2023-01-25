
'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''


def wordPattern(pattern: str, s: str) -> bool:
    lookup = {}
    pattern_dict = {}

    s_arr = s.split(' ')
    pattern_len = len(pattern)

    if len(s_arr) != pattern_len:
        return False

    for index, word in enumerate(s_arr):
        first_char = word[0]
        key = pattern[index]

        if key not in lookup:
            lookup[key] = word
            pattern_dict[word] = key

    for index, word in enumerate(s_arr):
        if word not in pattern_dict:
            return False

        val = pattern_dict[word]
        pattern_value = pattern[index]
        if pattern_value != val:
            return False
    return True


pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s), '\n')

# pattern = "abba"
# s = "dog cat cat fish"
# print(wordPattern(pattern, s), '\n')

pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s), '\n')

# pattern = "abba"
# s = "dog dog dog dog"
# print(wordPattern(pattern, s), '\n')

# pattern = "aba"
# s = "cat cat cat dog"
# print(wordPattern(pattern, s), '\n')

pattern = "ab"
s = "hap hac"
print(wordPattern(pattern, s), '\n')
