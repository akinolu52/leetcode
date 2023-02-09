from itertools import pairwise


def isMonotonic(num: int) -> bool:
    isIncreasing = True
    isDecreasing = True

    for pair in pairwise(str(num)):
        pair0 = int(pair[0])
        pair1 = int(pair[1])

        if pair1 > pair0:
            isDecreasing = False
        if pair1 < pair0:
            isIncreasing = False

    return isIncreasing or isDecreasing


print(isMonotonic(10))


