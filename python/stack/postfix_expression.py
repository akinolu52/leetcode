from stack import Stack


def postFixEvaluation(s: str) -> int:
    stack = Stack()

    operators = ['-', '+', '*', '/']

    for ch in s:
        if ch.isdigit():
            stack.push(ch)
        else:
            if ch in operators:
                val1 = stack.pop()
                val2 = stack.pop()

                if val1 == None or val2 == None:
                    return -1
                else:
                    result = None

                    val1 = int(val1)
                    val2 = int(val2)

                    if ch == '-':
                        result = val2 - val1
                    elif ch == '+':
                        result = val2 + val1
                    elif ch == '*':
                        result = val2 * val1
                    else:
                        result = val2 / val1

                    stack.push(result)

    return stack.pop()


print(postFixEvaluation("235*+8-"))
