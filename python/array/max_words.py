
def mostWordsFound(sentences):
    max_len = 0

    for words in sentences:
        words_len = len(words.split(' '))

        if words_len > max_len:
            max_len = words_len

    return max_len


sentences = ["alice and bob love leetcode",
             "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))  # 6
