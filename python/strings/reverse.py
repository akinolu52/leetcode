
# reverse a given string


str = 'hello world'

result = ''

for char in reversed(str):
    result += char

print(result)

result = ''

for index in range(len(str) - 1, -1, -1):
    result += str[index]

print(result)


print(str[::-1])
