import sys

'''
Given an array of integers, 
our task is to write a program that efficiently 
finds the second-largest element present in the array. 
'''


def secondLargest(values) -> int:
    first = second = -sys.maxsize

    for val in values:

        if val > first:
            second = first
            first = val
        elif val > second and val != first:
            second = val

    return second


print(secondLargest([10, 4, 3, 50, 23, 90]))
print(secondLargest([10, 4, 3, 50, 23, 90, 90]))
