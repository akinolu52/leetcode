

def getCharIndex(char, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # find the position of the character
    index = alphabet.find(char)

    # add the shift to the character position and limit it the alphabet range (0 - 26)
    return alphabet[(index + shift) % len(alphabet)]


'''
    - if you look at the problem statement this's what you'll see
    # a => 3 + 5 + 9
    # b => 5 + 9
    # c => 9
    - so the idea is to get the sum of the shift
    - then add the sum to the character index 
    - and then reduce the shift sum while running the loop forward
'''


def shiftingLetters(s: str, shifts) -> str:
    # check if the length are equal (this is a fail fast concept)
    if len(s) != len(shifts):
        return -1

    # this variable will hold the sum of all the shit
    shiftSum = sum(shifts)
    # this variable will hold the result
    result = ''
    # this variable will hold the shit counter (for the loop)
    shiftCounter = 0

    # loop through each character in the string - get the character and its index
    for index, char in enumerate(s):
        # get the number of shift needed for the current index
        shift = shifts[shiftCounter]

        # start decrementing the shiftSum and incrementing the shiftCounter once the loop index is not zero
        if index != 0:
            shiftSum -= shift
            shiftCounter += 1

        # append the shift value to the result string
        result += getCharIndex(char, shiftSum)

    return result
