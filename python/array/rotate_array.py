
'''
Given an array arr[] of size N, 
the task is to rotate the array by d position to the left.

EX

Input:  arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
Output: 3, 4, 5, 6, 7, 1, 2
Explanation: If the array is rotated by 1 position to the left, 
it becomes {2, 3, 4, 5, 6, 7, 1}.
When it is rotated further by 1 position,
it becomes: {3, 4, 5, 6, 7, 1, 2}

Input: arr[] = {1, 6, 7, 8}, d = 3
Output: 8, 1, 6, 7
'''

# stop = arr[0: n]
# start = arr[n: len(arr)]

# print(arr)

# return start + stop


# [1, 6, 7, 8]


def rotate(arr, k):
    if k != 0:

        # right rotate
        # arrLen = len(arr)
        # arr[arrLen-k:], arr[:arrLen-k] = arr[:arrLen-k], arr[arrLen-k:]

        # left rotate
        k = k % len(arr)
        arr[k:], arr[:k] = arr[:k], arr[k:]

        return arr


print(rotate([1, 6, 7, 8], 3))  # [8, 1, 6, 7]
# print(rotate([1, 2, 3, 4, 5, 6, 7], 2)) # 3, 4, 5, 6, 7, 1, 2
