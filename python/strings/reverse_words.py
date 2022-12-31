
# reverse the string in each words


str = 'hello world' # returns olleh dlrow 

str = str[::-1]

str = str.split(' ')

result = ''

for index in range(len(str) - 1, -1, -1):
    result += str[index] + " "

print(result)
