import re

'''
get frequency of every word in a sentence
'''

s = "Best items in category are samsung and lenovo. Samsung items are cool. Lenovo items are cool"

s = re.sub('[\W+ ]', ' ', s.lower())

s_array = s.split(' ')

lookup = {}

for word in s_array:
    if word == '' or word == ' ':
        continue

    if lookup.get(word):
        lookup[word] = lookup[word] + 1
    else:
        lookup[word] = 1

    print(word)

keys = list(lookup.keys())

print(lookup, keys)
