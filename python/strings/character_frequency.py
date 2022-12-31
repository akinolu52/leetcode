
'''
Sort Characters By Frequency
'''

s = "tree"
# s = "cccaaa"
# s = "Aabb"

s_array = list(s)

lookup = {}

for word in s_array:
    if word == '' or word == ' ':
        continue

    if lookup.get(word):
        lookup[word] = lookup[word] + 1
    else:
        lookup[word] = 1

sorted_lookup = sorted(lookup.items(), key=lambda x: x[1], reverse=True)

result = ''
for word in sorted_lookup:
    char = word[0]
    occurrence = word[1]

    result += char * occurrence

print(result)
