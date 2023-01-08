def largestOddNumber(num: str) -> str:
    if int(num) % 2 != 0:
        return num

    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 0:
            num = num[0: i]
        else:
            break

    return num


num = "4206"
print('result => ', largestOddNumber(num))

num = "52"
print('result => ', largestOddNumber(num))

num = "35427"
print('result => ', largestOddNumber(num))

num = "10133890"  # "113389" - "1013389"
print('result => ', largestOddNumber(num))
