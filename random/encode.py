
def reverse_encode(s: str) -> str:
    s_list = s[::-1]

    result_array = [str(ord(ch))[::-1] for ch in s_list]

    return ''.join(result_array)


print(reverse_encode('HackerRank'))
