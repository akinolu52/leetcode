
'''
Running Sum of 1d Array:

Given an array nums. 
We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''


def runningSum(nums):
    # initialize the result (with the first item in num)
    # and index of the loop to 1
    result = [nums[0]]
    index = 1

    # go through the nums in the nums list
    while index < len(nums):
        # get the previous value in result and add it to the current num
        result.append(nums[index] + result[index - 1])

        # increment the index
        index += 1

    return result


print(runningSum([1]))
print(runningSum([1, 2, 3, 4]))
print(runningSum([1, 1, 1, 1, 1]))
print(runningSum([3, 1, 2, 10, 1]))
