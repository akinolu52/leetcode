

# TODO: finish up

def minDeletionSize(strs):
    result = 0
    index = 0
    str_len = len(strs[0])

    str_array = []
    for s in strs:
        s_array = list(s)
        print('str => ', s_array)

    return result


print(minDeletionSize(["abc", "bce", "cae"]))
print(minDeletionSize(["cba", "daf", "ghi"]))
print(minDeletionSize(["a", "b"]))
print(minDeletionSize(["zyx", "wvu", "tsr"]))
