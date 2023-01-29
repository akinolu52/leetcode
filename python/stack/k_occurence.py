
'''
Input: arr[] = {3, 1, 4, 4, 5, 2, 6, 1}, K = 2
Output: 4 1
Explanation:
Frequency of 4 = 2, Frequency of 1 = 2
These two have the maximum frequency and 4 is larger than 1.

Input: arr[] = {7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9}, K = 4
Output: 5 11 7 10
Explanation: 
Frequency of 5 = 3, Frequency of 11 = 2, Frequency of 7 = 2, Frequency of 10 = 1
These four have the maximum frequency and 5 is largest among rest.
'''


def mostFrequentNumber(arr, k: int):
    result = []
    occurrence = {}

    # freq = [[] for _ in range(len(arr) + 1)]
    freq = [None] * (len(arr) + 1)

    print('freq = ', freq)

    for val in arr:
        if val in occurrence:
            occurrence[val] += 1
        else:
            occurrence[val] = 1

    for n in occurrence:
        freq.append(n)

    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == K:
                return result[-1::-1]
    print('freq = ', freq)


    print(occurrence)
    # print(arr, k)


arr = [3, 1, 4, 4, 5, 2, 6, 1]
K = 2
print(mostFrequentNumber(arr, K))
