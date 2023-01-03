
def letterCombinations(digits: str):
    if len(digits) == 0:
        return []
        
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }


    i = 0
    while i < len(digits):
        digit = digits[i]
        j = i + 1

        if digit in mapping:
            digit_mapping = mapping[digit]
            print('digit = {1}, digit_mapping = {0}'.format(
                digit_mapping, digit))

            while j < len(digits):
                inner_digit = digits[j]

                if inner_digit in mapping:
                    digit_inner_mapping = mapping[inner_digit]
                    print('digit = {}, inner digit = {}, digit_inner_mapping = {}'.format(
                        digit, inner_digit, digit_inner_mapping))

                j += 1
        i += 1


print(letterCombinations('234'))
# print(letterCombinations('23'))
# print(letterCombinations(''))
# print(letterCombinations('2'))
