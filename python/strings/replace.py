
# replace all 'l' with y

str = 'Hello World'
result = ''

for index in range(0, len(str)):
    if str[index] == 'l':
        result += 'y'
    else:
        result += str[index]

print(result)
