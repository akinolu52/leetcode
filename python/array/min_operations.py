def minimumOperations(nums) -> int:
    def filterNums(arr):
        return list(filter(lambda num: num != 0, arr))

    count = 0
    nums.sort()
    numsCopy = filterNums(nums)

    while True:
        if sum(nums) == 0:
            return count

        minVal = numsCopy[0]

        for idx, num in enumerate(nums):
            if num == 0:
                continue

            nums[idx] -= minVal

        numsCopy = filterNums(nums)
        count += 1


nums = [1, 5, 0, 3, 5]
print(minimumOperations(nums))
