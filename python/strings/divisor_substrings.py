def divisorSubstrings(num: int, k: int) -> int:

    index = 0
    num_str = str(num)
    divisor_count = 0

    while index < len(num_str):
        n = num_str[index: index + k]

        if len(n) < k:
            break

        if int(n) != 0 and num % int(n) == 0:
            divisor_count += 1
        index += 1

    return divisor_count


num = 430043
k = 2
print(divisorSubstrings(num, k))

num = 240
k = 2
print(divisorSubstrings(num, k))
