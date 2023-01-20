
def reverseParentheses(s: str) -> str:
    # uevoli
    stack = []
    bracketIdx = []

    for idx, ch in enumerate(s):

        if ch == '(':
            bracketIdx.append(len(stack))
            stack.append(ch)

        elif ch == ')':
            index = bracketIdx.pop()

            # reverse the stack
            prev = stack[index + 1: idx]
            prev.reverse()

            print('index:', index, prev, stack)
            stack[index + 1: idx] = list(prev)
            # remove the the bracket '(' in stack
            if len(stack) != 0:
                stack.pop(index)

            # print('index:', index, prev, stack)
            # stack.append(list(prev))

        else:
            stack.append(ch)

    return ''.join(stack)


# s = "(abcd)"  # dcba
# print(reverseParentheses(s))

# # uevoli

s = "(u(love)i)"
print(reverseParentheses(s))

s = "(ed(et(oc))el)"
print(reverseParentheses(s), '\n')

s = "ta()usw((((a))))"
print(reverseParentheses(s))
