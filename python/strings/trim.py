
# program to trim a string
str = "  Hello user!!! welcome "

frontSpaceCount = 0
backSpaceCount = 0

for char in str:
    if char.isalpha():
        break
    else:
        frontSpaceCount += 1

for char in reversed(str):
    if char.isalpha():
        break
    else:
        backSpaceCount += 1


str = str[frontSpaceCount:]
str = str[:-(backSpaceCount)]

print(str)
