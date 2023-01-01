
def twoSum(nums, target: int):
    if len(nums) == 2:
        if nums[0] + nums[1] == target:
            return [0, 1]
        else:
            return []

    lookup = {}

    for index, num in enumerate(nums):
        diff = target - num

        if diff in lookup:
            return [lookup[diff], index]

        lookup[num] = index
    return []


nums = [2, 7, 11, 15]
target = 9

# nums = [3, 2, 4]
# target = 6

print(twoSum(nums, target))
