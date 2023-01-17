
def findReplaceString(s: str, indices, sources, targets) -> str:
    sList = temp = list(s)

    a = []

    idx = -1
    while idx < len(s) - 1:
        idx += 1
        ch = s[idx]

        if idx in indices:
            src = sources[idx]
            tgt = targets[idx]

            print('replace ', src, ' with ', tgt)
            continue

        print('ch => ', ch)
        a.append(ch)

    # for idx, ch in enumerate(s):

    #     if idx in indices:
    #         print('replace ', idx, ch)
    #         continue

    #     print('ch => ', ch)
    #     a.append(ch)

    # for counter, idx in enumerate(indices):
    #     srcChar = sources[counter]
    #     tgtChar = targets[counter]

    #     ch = sList[idx: idx + len(srcChar)]
    #     # s = tempS
    #     # temp[idx: idx + len(srcChar)] = list(tgtChar)
    #     temp[idx: idx + len(srcChar)] = list('#' * len(srcChar))

    #     print('indices => ', idx)
    #     print('srcChar => ', srcChar)
    #     print('tgtChar => ', tgtChar)
    #     print('char => ', ch)
    #     print('temp => ', temp)
    #     print()

    # for idx, ch in enumerate(s):
    #     if idx in indices:
    #         position = indices.index(idx)

    #         srcLen = len(sources[position])

    #         sList[position: srcLen] = targets[position]

    #         print('change idx ', idx, position, sList, ch)

    print(a)
    return ''.join(temp)


s = "vmokgggqzp"
indices = [3, 5, 1]
sources = ["kg", "ggq", "mo"]
targets = ["s", "so", "bfr"]

# v#######zp
# v####g##p
# vbfrssozp
print(findReplaceString(s, indices, sources, targets))


# s = "abcd"
# indices = [0, 2]
# sources = ["a", "cd"]
# targets = ["eee", "ffff"]
# # eeebffff

# print(findReplaceString(s, indices, sources, targets))

# # str = 'Python'
# # indexes = [2, 4, 5]
# # new_character = 'a'
# # result = ''
# # for i in indexes:
# #     str = str[:i] + new_character + str[i+1:]
# # print(str)

# s = "abcd"
# indices = [0, 2]
# sources = ["ab", "ec"]
# targets = ["eee", "ffff"]

# print(findReplaceString(s, indices, sources, targets))
