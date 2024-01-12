
from itertools import product

def letterCombinations2(digits: str):
    if not digits:
        return []

    letters = [
        None,
        None,
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz"
    ]

    res = [letters[int(n)] for n in digits]
    return [''.join(i) for i in product(*res)]


def letterCombinations(digits: str):
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    if not digits:  # edge case
        return []
    chars = [dic[c] for c in digits]
    code = product(*chars)
    return [''.join(k) for k in code]

#  dic={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
#     if digits=="":# edge case
#         return []
#     chars=[]
#     for c in digits:
#         chars.append(dic[c])
#     code=product(*chars)
#     list1=[]
#     for k in code:
#         list1.append(''.join(k))
#     return list1;


# Example 1:

digits = "23"
print(letterCombinations2(digits))
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# digits = ""
# Output: []
# Example 3:

# digits = "2"
# Output: ["a","b","c"]
