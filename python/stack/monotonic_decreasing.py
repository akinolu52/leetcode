
def monotonicDecreasingStack(arr):
    result = [arr[0]]

    for num in arr[1:]:
        while len(result) and num > result[-1]:
            result.pop()

        result.append(num)

    return result


print(monotonicDecreasingStack([15, 17, 12, 13, 14, 10]))
