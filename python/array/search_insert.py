

'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

'''


def searchInsert(nums, target: int) -> int:
    # check if the target is present in the nums list and return the index
    if target in nums:
        return nums.index(target)

    # if it does not exist add it to the list and return the index
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)


nums = [1, 3, 5, 6]
target = 2
print('search ', searchInsert(nums, target))

nums = [1, 3, 5, 6]
target = 7
print('search ', searchInsert(nums, target))

nums = [1, 3, 5, 6]
target = 5
print('search ', searchInsert(nums, target))
