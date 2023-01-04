
'''
Remove Element

Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.
'''


def removeElement(nums, val: int):
    pop_index = []

    for index, num in enumerate(nums):
        if num == val:
            pop_index.append(index)

    pop_index.reverse()

    for index in pop_index:
        nums.pop(index)

    return nums


print(removeElement([3, 2, 2, 3], 3))
print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
