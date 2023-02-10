from itertools import pairwise


def isMonotonic(nums) -> bool:
    isIncreasing = True
    isDecreasing = True

    for pair in pairwise(nums):

        if pair[1] > pair[0]:
            isDecreasing = False
        if pair[1] < pair[0]:
            isIncreasing = False

    return isDecreasing or isIncreasing


nums = [1, 2, 2, 3]
print(isMonotonic(nums))

nums = [6, 5, 4, 3]
print(isMonotonic(nums))

nums = [1, 5, 2]
print(isMonotonic(nums))

nums = [5, 15, 20, 10]
print(isMonotonic(nums))

