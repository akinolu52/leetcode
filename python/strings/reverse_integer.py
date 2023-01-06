'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
then return 0.

'''


def reverse(x: int) -> int:
    # calculate the unsigned bound
    bound = 2 ** 31

    # get the sign from the input value
    sign = -1 if x < 0 else 1

    # strip sign away from the input value
    if sign == -1:
        x *= sign

    # calculate the reverse
    # by converting it to string and reversing it
    # then add sign to the result
    num = sign * (int(str(x)[::-1]))

    # return 0 if it's within the integer range
    # else return value
    if sign == 1 and num > bound:
        return 0
    elif sign == -1 and num < (sign * bound):
        return 0

    return num


# print('reverse(123) => ', reverse(123))
# print('reverse(-123) => ', reverse(-123))
# print('reverse(120) => ', reverse(120))
print('reverse(1534236469) => ', reverse(1534236469))
