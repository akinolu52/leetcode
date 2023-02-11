
'''
Given an array arr[] of N integers and an integer K, 
the task is to find whether the given array elements can be made 0 if the given operation is applied exactly K times. 
In a single operation, the smallest element from the array will be subtracted from all the non-zero elements of the array.
'''


def reduceToZero(nums, k) -> str:

    return 'yes' if len(set(nums)) == k else 'no'


nums = [1, 1, 2, 3]
k = 3
print(reduceToZero(nums, k))

nums = [11, 2, 3, 4]
k = 3
print(reduceToZero(nums, k))
