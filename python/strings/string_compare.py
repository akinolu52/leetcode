

# compare if two strings are equal with backspace represented as #

# i.e. bcd##e is equal to bc#e

str1 = 'bcd##e'
str2 = 'bc#e'

s1 = ''
s2 = ''

for char in str1:

    if char == '#':
        # delete previous character
        s1 = s1[:-1]
    else:
        s1 += char

for char in str2:

    if char == '#':
        # delete previous character
        s2 = s2[:-1]
    else:
        s2 += char

result = 'equal ' if s1 == s2 else 'not equal'

print('{} and {} are {} '.format(str1, str2, result))
