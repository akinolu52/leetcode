

'''
Given an array of random numbers, 
Push all the zero’s of a given array to the end of the array. 
For example, 
if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, 
it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. 
The order of all other elements should be same.
Expected time complexity is O(n) and extra space is O(1).
'''


def moveZero(arr):
    zeroCount = 0

    for index, num in enumerate(arr):
        if num == 0:
            zeroCount += 1
            del arr[index]

    idx = 0

    while idx < zeroCount:
        arr.append(0)
        idx += 1

    return arr


arr = [5, 6, 0, 4, 6, 0, 9, 0, 8]
print(moveZero(arr))
