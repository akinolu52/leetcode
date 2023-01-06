

def plusOne(digits):
    # get the last digit
    last_digit = digits[-1]

    # check if the last digit is not 9 (cause of overflow since 9 + 1 = 10)
    # if not 9 add one then return
    if last_digit != 9:
        plus_one = last_digit + 1
        digits[-1] = plus_one

        return digits
    
    # convert list to integer then add one then convert back to a list
    else:
        digits_int = int(''.join(map(str, digits)))
        plus_one = digits_int + 1

        return list(map(int, str(plus_one)))


digits = [1, 2, 3]
# Output: [1,2,4]
print('digits = {}, plusOne = {}'.format(digits, plusOne(digits)))

digits = [4, 3, 2, 1]
# Output: [4,3,2,2]
print('digits = {}, plusOne = {}'.format(digits, plusOne(digits)))

digits = [9]
# Output: [1,0]
print('digits = {}, plusOne = {}'.format(digits, plusOne(digits)))
