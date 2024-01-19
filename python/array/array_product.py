
'''
Given an integer array nums,
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
'''


def productExceptSelf(nums):

    result = []

    product = 1

    if 0 not in nums:
        for num in nums:
            product *= num

        result.extend(int(product / num) for num in nums)
    else:
        zero_index = []
        for index, num in enumerate(nums):
            if num == 0:
                zero_index.append(index)
                continue

            product *= num

        if len(zero_index) > 1:
            return [0] * len(nums)

        for index, num in enumerate(nums):
            if index in zero_index:
                result.append(product)
                continue

            result.append(0)

    return result


nums = [1, 2, 3, 4]

print(productExceptSelf(nums))


nums = [-1, 1, 0, -3, 3]

print(productExceptSelf(nums))

nums = [-1, 1, 0, 0, 3]

print(productExceptSelf(nums))

nums = [0, 0]

print(productExceptSelf(nums))
