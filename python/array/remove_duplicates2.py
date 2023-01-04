
'''
Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, 
remove some duplicates in-place such that each unique element appears at most 
twice. The relative order of the elements should be kept the same.
'''


def removeDuplicates(nums) -> int:
    occurrences = {}

    for index, num in enumerate(nums):
        if num in occurrences:
            occurrences[num] = occurrences[num] + 1
        else:
            occurrences[num] = 1

    for key, value in occurrences.items():
        to_remove = value - 2 if value - 2 > 0 else 0

        index = 0
        while (index < to_remove):
            nums.remove(key)
            index += 1

    return len(nums)


print(removeDuplicates([1, 1, 1, 2, 2, 3]))
print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
