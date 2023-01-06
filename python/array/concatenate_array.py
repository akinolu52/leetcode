
def getConcatenation(nums):
    nums_len = len(nums)
    result = list('_' * nums_len * 2)

    for index, num in enumerate(nums):
        result[index] = num
        result[index + nums_len] = num
    return result


nums = [1, 2, 1]
print('getConcatenation ', getConcatenation(nums))
