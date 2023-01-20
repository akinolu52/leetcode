
'''
Given an array A of n elements, 
sort the array according to the following relations :  

A[i] >= A[i-1], if i is even,  ∀ 1 <= i <= n
A[i] <= A[i-1], if i is odd ,  ∀ 1 <= i <= n
'''


def rearrange(arr):
    index = 0

    while index < len(arr):
        curr = arr[index]
        _next = arr[index + 1]

        if curr > _next:
            arr[index + 1], arr[index] = curr, _next

        index += 2

    return arr


print('rearrange => ', rearrange([1, 2, 2, 1]))
