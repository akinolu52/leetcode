
str = 'I am Emmanuel'  # Emmanuel am I

str = str.split(' ')

result = ''

for index in range(len(str) - 1, -1, -1):
    result += str[index] + " "

print(result)
