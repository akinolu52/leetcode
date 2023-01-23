'''
Given a sorted array of positive integers, 
rearrange the array alternately 
i.e 
first element should be a maximum value, at second position minimum value, 
at third position second max, at fourth position second min, and so on. 
'''


def rearrange(arr):
    result = []

    left = 0
    right = len(arr) - 1

    checkLargest = True

    for _ in arr:
        if checkLargest:
            result.append(arr[right])

            right -= 1
        else:
            result.append(arr[left])

            left += 1
        checkLargest = False
    return result


print(rearrange([1, 2, 3, 4, 5, 6, 7]))
print(rearrange([1, 2, 3, 4, 5, 6]))
