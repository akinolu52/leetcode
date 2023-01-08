
def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    nums_len = len(nums)
    if nums_len != 0:
        insert_pos = 0

        for index, num in enumerate(nums):

            if num != 0:
                nums[index], nums[insert_pos] = nums[insert_pos], nums[index]
                insert_pos += 1


nums = [0, 1, 0, 3, 12]  # [1, 3, 12, 0, 0]
print('nums = {}'.format(nums, moveZeroes(nums)))

# nums = [0]
# print('nums = {}'.format(moveZeroes(nums)))
