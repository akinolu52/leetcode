
"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""

"""
    @param: s: A string
    @return: decodes a single string to a list of strings
"""


def decode(s):
    result = []
    i = 0

    while i < len(s):
        j = i
        # loop to get the length of the string
        while s[j] != '#':
            j += 1

        # convert the calculated length to an integer
        length = int(s[i: j])

        # slice the string from the initial to the end of the length + 1 and push into result
        result.append(s[j + 1: j + 1 + length])

        # update the pointer to the next character after the end of the previous string
        i = j + 1 + length

    return result


strs = ['akin', 'olu']

encoding = encode(strs)

print('encoding: %s' % encoding)

decoding = decode(encoding)

print('decoding: %s' % decoding)
