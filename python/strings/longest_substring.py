
# find the length of the longest unique substring

s = 'abcabcbb'

# for the loops
arr = []

# used to keep unique substrings
longest_substring = ""

for index in range(len(s)):
    char = s[index]

    # check if string is in array
    # remove the last occurrence of the character to index 0
    # store the array value in the longest substring string
    if char in arr:
        occurrence_index = arr.index(char) + 1

        if len(longest_substring) < len(arr):
            longest_substring = ''.join(arr)
        del arr[:occurrence_index]

    arr.append(char)


print('length of longest substring is: {1}, characters in longest substring are: {0}'.format(
    ', '.join(list(longest_substring)), len(longest_substring)))
