def longestPalindrome(s: str) -> int:

    lookup = {}

    for ch in s:
        if ch in lookup:
            lookup[ch] += 1
        else:
            lookup[ch] = 1

    result = 0
    largestOddNumber = 0
    foundOdd = False

    for value in lookup.values():
        if value % 2 == 0:
            result += value
        else:
            result += (value - 1)
            foundOdd = True

    return result + largestOddNumber + (1 if foundOdd else 0)
