def twoOutOfThree(nums1, nums2, nums3):
    res1 = set(nums1) & set(nums2)
    res2 = set(nums1) & set(nums3)
    res3 = set(nums2) & set(nums3)

    return list(res1.union(list(res2)).union(list(res3)))


nums1 = [1, 1, 3, 2]
nums2 = [2, 3]
nums3 = [3]

print(twoOutOfThree(nums1, nums2, nums3))
