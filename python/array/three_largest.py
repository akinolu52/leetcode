import sys

'''
Given an array with all distinct elements, 
find the largest three elements. 
Expected time complexity is O(n) and extra space is O(1). 
'''


def print3largest(values):

    first = second = third = -sys.maxsize

    for val in values:
        if val > first:
            third = second
            second = first
            first = val
        elif val > second and val != first:
            third = second
            second = val
        elif val > third and val != second:
            third = val

    return (first, second, third)


print(print3largest([-1, -2, -3]))
print(print3largest([10, 4, 3, 50, 23, 90]))
print(print3largest([12, 13, 1, 10, 34, 1]))
print(print3largest([12, 45, 1, -1, 45, 54, 23, 5, 0, -10]))
print(print3largest([11, 65, 193, 36, 209, 664, 32]))
