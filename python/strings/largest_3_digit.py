def largestGoodInteger(num: str) -> str:
    largest_number = ""
    num_len = len(num)

    for i in range(num_len):
        n = num[i: i+3]

        if len(n) < 3:
            break

        if int(n[0]) == int(n[1]) == int(n[2]):
            if largest_number == "" or int(n) > int(largest_number):
                largest_number = n

    return largest_number


num = "6777133339"
print(largestGoodInteger(num))

num = "2300019"
print(largestGoodInteger(num))

num = "42352338"
print(largestGoodInteger(num))
