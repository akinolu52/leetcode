
def groupAnagrams(strs):
    def rearrange_string(s):
        s = list(s)
        s.sort()

        return ''.join(s)

    # sortedString: [array of inputted string]
    lookup = {}

    for s in strs:
        _s = rearrange_string(s)

        if _s in lookup:
            lookup[_s] += [s]
        else:
            lookup[_s] = [s]

    return list(lookup.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))
