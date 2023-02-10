
def duplicate(nums):
    result = []

    for num in nums:
        index = abs(num) - 1

        if nums[index] < 0:
            result.append(abs(num))

        nums[index] = -nums[index]

    return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(duplicate(nums))

nums = [1, 1, 2]
print(duplicate(nums))

nums = [1]
print(duplicate(nums))
