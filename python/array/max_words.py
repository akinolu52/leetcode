
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

sentences = ["please wait", "continue to fight", "continue to win"]
print(mostWordsFound(sentences))

sentences = ["w jrpihe zsyqn l dxchifbxlasaehj", "nmmfrwyl jscqyxk a xfibiooix xolyqfdspkliyejsnksfewbjom", "xnleojowaxwpyogyrayfgyuzhgtdzrsyococuqexggigtberizdzlyrdsfvryiynhg", "krpwiazoulcixkkeyogizvicdkbrsiiuhizhkxdpssynfzuigvcbovm",
             "rgmz rgztiup wqnvbucfqcyjivvoeedyxvjsmtqwpqpxmzdupfyfeewxegrlbjtsjkusyektigr", "o lgsbechr lqcgfiat pkqdutzrq iveyv iqzgvyddyoqqmqerbmkxlbtmdtkinlk", "hrvh efqvjilibdqxjlpmanmogiossjyxepotezo", "qstd zui nbbohtuk", "qsdrerdzjvhxjqchvuewevyzlkyydpeeblpc"]
print(mostWordsFound(sentences))
