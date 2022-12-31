
s = 'bccbababd'

# split string
s = list(s)

# convert to set
s = set(s)

# convert to string
s = ''.join(s)

print(s)


# approach 2

arr = []

for char in s:
    if char in arr:
        continue
    arr.append(char)


print(''.join(arr))