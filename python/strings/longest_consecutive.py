
def longestConsecutive(nums):
    # remove duplicate as we dont handle successive numbers
    nums = sorted(set(nums))

    result = 0
    res = 1

    for index, value in enumerate(nums):
        # check if the difference between successive number are 1
        # check if the next index is not out of bound
        # if out of bound reset and continue
        if index + 1 < len(nums) and (nums[index + 1] - nums[index]) != 1:
            res = 1
            continue

        # check if the next index is not out of bound and update res
        if index + 1 < len(nums):
            res += 1

        # update result if it's the longest consecutive Sequence
        if result < res:
            result = res
            
    return result


# print('longestConsecutive = {} '.format(
#     longestConsecutive([100, 4, 200, 1, 3, 2])))

# print('longestConsecutive = {} '.format(
#     longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])))

print('longestConsecutive = {} '.format(
    longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6])))
