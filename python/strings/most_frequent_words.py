import re

'''

find the word that occur most in a given text

'''

# s = 'Best item in category . lenovo samsung lenovo ? item'
s = "..Bob hit a ball, the hit BALL flew far after it was hit."
s = "Bob hit a ball, the hit BALL flew far after it was hit."
# s = "a, a, a, a, b,b,b,c, c"
s = "a."
s = "Bob. hIt, baLl"


s = re.sub("[!?',;.]+", ' ', s.lower())

print(s)

banned = ["hit"]
banned = ["bob", "hit"]

s_arr = s.split(' ')

# print(s_arr)

lookup = {}

for word in s_arr:
    print('word => ', word)
    if word in banned or word == '':
        continue

    lookup[word] = lookup[word] + 1 if lookup.get(word) else 1
values = lookup.values()
max_occurrences = max(values)

result = []
print(lookup)

for word in lookup:
    val = lookup.get(word)

    if val == max_occurrences:
        print(word)
        # result.append(word)

print(', '.join(result))
