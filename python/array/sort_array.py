
from collections import Counter


def frequencySort(nums):
    r = Counter(nums)
    print('r => ', r)
    return sorted(nums, key=lambda x: (r[x], -x))


nums = [1, 1, 2, 2, 2, 3]
print(frequencySort(nums), '\n')

nums = [2, 3, 1, 3, 2]
print(frequencySort(nums), '\n')

nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
print(frequencySort(nums), '\n')
