
# TODO:
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

    index = 0
    for word in s_arr:
        first_char = word[0]
        key = pattern[index]

        # print('first_char = {}, key = {}'.format(first_char, key))

        # if key not in lookup and first_char not in lookup.values():
        if key not in lookup:
            lookup[key] = first_char
            # pattern_dict[first_char] = key
        index += 1

    pattern_keys = list(lookup.keys())
    pattern_values = list(lookup.values())

    print('lookup = {}, pattern_keys = {}, pattern_values = {}'.format(lookup, pattern_keys, pattern_values))
    # print('lookup = {}, pattern_dict = {}'.format(lookup, pattern_dict))

    # for index, word in enumerate(s_arr):
    #     first_char = word[0]

    #     if first_char not in pattern_dict:
    #         return False
    #     else:
    #         val = pattern_dict[first_char]
    #         pattern_value = pattern[index]

    #         if pattern_value != val:
    #             return False
    # # print('key = {}, value = {}, p_value = {}'.format(
    #     first_char, val, pattern_value))


    for index, word in enumerate(s_arr):
        first_char = word[0]
        print(index, first_char)

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
