

def singleNumber(nums) -> int:
    # check if nums list contain one item and return
    if len(nums) == 1:
        return nums[0]

    lookup = {}

    # create a lookup dictionary based on occurrence
    for num in nums:
        if num in lookup:
            lookup[num] = lookup[num] + 1
        else:
            lookup[num] = 1

    # return the value equals 1
    for key, val in lookup.items():
        if val == 1:
            return key

    return -1


nums = [2, 2, 1]
Output: 1
print('nums = {}, single number = {},'.format(nums, singleNumber(nums)))

nums = [4, 1, 2, 1, 2]
# Output: 4
print('nums = {}, single number = {},'.format(nums, singleNumber(nums)))

nums = [1]
Output: 1
print('nums = {}, single number = {},'.format(nums, singleNumber(nums)))
