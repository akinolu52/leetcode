'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].

'''


def solution(N):
    binN = bin(N).replace('0b', '')

    oneArr = [index for index, char in enumerate(binN) if int(char) == 1]

    maxDiff = 0
    for index in range(len(oneArr)):
        if index + 1 < len(oneArr):
            x = oneArr[index]
            y = oneArr[index+1]
            maxDiff = max(y - x, maxDiff)

    return 0 if maxDiff == 1 else maxDiff - 1
    # pass


print('solution (1041) => ', solution(1041))
print('solution (529) => ', solution(529))
print('solution (15) => ', solution(15))
print('solution (32) => ', solution(32))
