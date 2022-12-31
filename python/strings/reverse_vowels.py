
'''

find the vowels in a given string 
i.e equation contains euaio vowels it should return oqiatuen

'''

s = 'aA'
s_len = len(s)

vowels = ['a', 'e', 'i', 'o', 'u']

result = list(s)

# create two pointer to point to the start and end of the string
left = 0
right = s_len - 1

while (left < s_len):
    l_char = s[left]
    r_char = s[right]

    # check if the both left and right characters are vowels and swap
    if l_char.lower() in vowels and r_char.lower() in vowels:
        result[left] = r_char
        result[right] = l_char
        left += 1
        right -= 1

    # if right is not a vowel decrement right index to the next character
    elif l_char.lower() in vowels and r_char.lower() not in vowels:
        right -= 1

    # if right is not a vowel increment left index to the next character
    elif l_char.lower() not in vowels and r_char.lower() in vowels:
        left += 1

    # if both right and left are not vowels then
    # increment left index to the next character
    # decrement right index to the next character
    else:
        left += 1
        right -= 1


print('result => ', ''.join(result))
