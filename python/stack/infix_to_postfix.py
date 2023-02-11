

def infixToPostfix(s: str) -> str:
    stack = []
    operatorStack = []
    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    for ch in s:
        if ch.isalpha() or ch.isdigit():
            stack.append(ch)
        elif operatorStack:
            top = operatorStack[-1]

            if priority[ch] == priority[top]:
                operatorStack.pop(-1)
                stack.append(top)
                operatorStack.append(ch)
            elif priority[ch] < priority[top]:
                print('incomming less', ch, top)
                stack.append(top)
                
                temp = []

                while operatorStack:
                    operator = operatorStack.pop(-1)

                    if priority[operator] > priority[ch]:
                        break


                # operatorStack.pop(-1)
                # stack.append(top)
                # operatorStack.append(ch)

                # stack.extend([top, ch])

            else:
                operatorStack.append(ch)
        else:
            operatorStack.append(ch)

        print(stack, operatorStack, ch)

    if operatorStack:
        stack += operatorStack[::-1]

    return ''.join(stack)


# s = 'A+B*C'  # ABC*+
# print(infixToPostfix(s))

# s = 'A*B+C/D'  # AB*CD/+
# print(infixToPostfix(s))

s = 'x+y*z/w+u'  # xyz*w/+u+
print(infixToPostfix(s))
