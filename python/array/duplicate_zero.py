def duplicateZeros(arr) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """

    temp = []

    for idx, value in enumerate(arr):
        if value == 0:
            temp.extend([0, 0])
        else:
            temp.append(value)

        tempValue = temp.pop(0)
        arr[idx] = tempValue

    print(arr)


arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicateZeros(arr)

# [1, 0, 2, 3, 0, 4, 5, 0]
# [1, 0, 2, 3, 0, 4, 5, 0]


# try:
#     curr = arr[left]

#     while left < len(arr) - 2:
#         print('left => ', left, arr, arr[left], arr[left + 1])
#         arr[left], arr[left + 1] = curr, arr[left]

#         curr = arr[left + 1]
#         left += 1
# except Exception:
#     continue
