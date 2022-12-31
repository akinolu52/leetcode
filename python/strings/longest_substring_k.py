'''
find the longest substrings length
if 'k' characters can be replaced
'''

# s = 'bccbababd'
# k = 2

# s = 'ABAB'
# k = 2

s = 'AABABBA'
k = 1

check = k
unique_list = []
longest = 0

index_pointer = 0
# substring = ''
unique_char_count = 0

while index_pointer < len(s):
    slider_pointer = index_pointer
    substring = ''

    unique_list.append(s[index_pointer])
    print('index_pointer ', index_pointer, 'slider_pointer ', slider_pointer)

    while slider_pointer < len(s):
        slider_char = s[slider_pointer]
        # print('slider_char ', slider_char, s[0], '\n')

        if slider_char not in unique_list and k != 0:
            unique_list.append(slider_char)
            k -= 1

        # l = len(set(unique_list))
        print('unique_list ', unique_list, 'k ', k)

        if k < 0:
            break

        slider_pointer += 1

        substring += slider_char
        # print('slider_pointer ', slider_pointer, slider_char, substring, k)

    longest = longest if longest > len(substring) else len(substring)
    index_pointer += 1
    k = check
    unique_list = []

print('longest substring length is {}'.format(longest))
