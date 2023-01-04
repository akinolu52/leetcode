
'''
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
'''


def removeDuplicates(nums) -> int:

    pop_index = []

    for index, num in enumerate(nums):
        if (index < 1 or index >= len(nums)):
            continue

        if num == nums[index - 1]:
            pop_index.append(index)

    pop_index.reverse()

    for index in pop_index:
        nums.pop(index)

    return len(nums)


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
