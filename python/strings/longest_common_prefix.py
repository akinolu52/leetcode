
def longestCommonPrefix(strs) -> str:
    shortest_string = min(strs, key=len)

    strs.remove(shortest_string)
    print('shortest_string ', shortest_string, strs)

    for s in strs:
        while len(shortest_string) > 0:
            if s.startswith(shortest_string):
                break
            shortest_string = shortest_string[:-1]
    return shortest_string


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
