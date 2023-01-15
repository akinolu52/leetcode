def isPerfectSquare(num: int) -> bool:
    if num == 1:
        return num

    return True if (num ** 0.5) % 1 == 0 else False


print(isPerfectSquare(16))
print(isPerfectSquare(14))
# print(isPerfectSquare(2000105819))
