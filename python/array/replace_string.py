def findReplaceString(s: str, indices, sources, targets) -> str:
    def replaceStr(_str, start, end, replacer=None):
        replacerString = replacer if replacer else '#' * (end - start)

        temp = list(_str)
        temp[start: end] = replacerString
        new_str = ''.join(temp)

        return new_str

    # check if sources[i] occurs at indices[i] in s
    # if it occur replace with targets[i]
    newStr = s

    for index, indexValue in enumerate(indices):
        start = indexValue
        # end = start + indexValue
        end = len(sources[index])

        # print(start, end)

        subStrAtIndex = s[start: start + end]

        # print(index, indexValue, subStrAtIndex, s, end)
        # print(subStrAtIndex, s, end, sources[index], len(sources[index]))

        if sources[index] == subStrAtIndex:
            # end = end + start
            print('match found', sources[index], s, start, end)

            s = replaceStr(s, start, end)

            # newStr[index: end] = targets[index]
            newStr = replaceStr(newStr, start, end, targets[index])

        # print(newStr, subStrAtIndex, end, s, newStr)

        # print(index, subStrAtIndex, replacedNewStr)

    return newStr


s = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]

print(findReplaceString(s, indices, sources, targets))


# s = "abcd"
# indices = [0, 2]
# sources = ["ab", "ec"]
# targets = ["eee", "ffff"]

# print(findReplaceString(s, indices, sources, targets))
