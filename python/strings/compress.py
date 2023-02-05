def compress(chars) -> int:

    left = 0
    idx = 1

    count = 1

    while idx <= len(chars):
        leftChar = chars[left]
        idxChar = None if idx == len(chars) else chars[idx]

        if leftChar == idxChar:
            # chars[idx] = '#'
            count += 1
        else:
            print('curr ', leftChar, count)
            index = left + 1
            if count > 1:
                countStr = str(count)
                countStrIndex = 0
                while index < idx:
                    value = countStr[countStrIndex]
                    chars[index] = countStr[countStrIndex]

                    index += 1
                    countStrIndex += 1

            left = idx
            count = 1

        idx += 1

    # chars = list(''.join(chars).replace('#', ''))

    print(chars)


# left = 0, idx = 3
    # 0    1    2    3    4
chars = ["c", "c", "c", "a", "a"]
# chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
# chars = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars))
