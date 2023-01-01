def topKFrequent(nums, k: int):
    lookup = {}
    result = []

    for num in nums:
        if num in lookup:
            lookup[num] += 1
        else:
            lookup[num] = 1

    sorted_lookup = sorted(lookup.items(), key=lambda x: x[1], reverse=True)

    for value in sorted_lookup:
        if len(result) + 1 > k:
            break
        result.append(value[0])

    return result


nums = [1, 1, 1, 2, 2, 3]
k = 2
# nums = [1, 2]
# k = 2

# nums = [4, 1, -1, 2, -1, 2, 3]


print(topKFrequent(nums, k))
