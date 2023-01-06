
'''
Given a string s consisting of words and spaces, 
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

'''


def lengthOfLastWord(s: str) -> int:
    s = s.strip().split(' ')

    return len(s[:-1][0])


print('lengthOfLastWord ', lengthOfLastWord('Emmanuel Olumide'))
print('lengthOfLastWord ', lengthOfLastWord("Hello World"))
