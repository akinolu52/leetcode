'''
 - Explanation by Denigma (check vs-code extension)
 - The code iterates over the list of strings, and creates a dictionary called lookup.
 - The keys in this dictionary are the string names, and the values are lists of all possible anagrams for that word.
 - The code then iterates through each string in turn, creating a new list with just one item: its anagram.
 - If it already exists in lookup, it adds itself to that list; otherwise it creates a new list with just one item: its anagram.
 - The code attempts to return a list of all the words in strs that are anagrams of each other.
 - The code first creates a lookup dictionary that will be used to store the anagrams.
 - The lookup dictionary is created with two keys, one for each word in strs .
 - The value associated with each key is a list of every possible combination of letters for that word.
'''

def groupAnagrams(strs):
    lookup = {}

    for s in strs:
        sortedStr = ''.join(sorted(s))

        if sortedStr in lookup:
            lookup[sortedStr] += [s]
        else:
            lookup[sortedStr] = [s]

    return lookup.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))
