
def monotonicIncreasingStack(arr):
    result = [arr[0]]

    for num in arr[1:]:
        while len(result) and num < result[-1]:
            result.pop()

        result.append(num)

    return result


print(monotonicIncreasingStack([1, 4, 5, 3, 12, 10]))
