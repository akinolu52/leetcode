
def isAnagram(s: str, t: str) -> bool:
    def rearrangeString(_s: str):
        # re-arrange in ascending order
        newString = sorted(_s)
        # convert to string and return the re-arranged string
        return ''.join(newString)

    # an anagram string must have the same length
    return False if len(s) != len(t) else rearrangeString(s) == rearrangeString(t)


print(isAnagram(s="anagram", t="nagaram"))
