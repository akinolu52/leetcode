
def fullJustify(words, maxWidth: int):
    result = []

    newStr = ''

    for index, s in enumerate(words):
        sLen = len(s)
        newStrLen = len(newStr)

        if (newStrLen + sLen) < maxWidth:
            newStr += s + ' '
        elif (newStrLen + sLen) > maxWidth:
            result.append(newStr)
            newStr = s + ' '
            # index -= 1

        print(s, newStr, result)

    # return result


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

print(fullJustify(words, maxWidth))
