from stack import Stack


def postFixEvaluation(s) -> int:
    # def postFixEvaluation(s: str) -> int:
    stack = Stack()

    operators = ['-', '+', '*', '/']

    for ch in s:
        if ch in operators:
            val1 = stack.pop()
            val2 = stack.pop()

            if val1 == None or val2 == None:
                return -1
            else:
                result = None

                if ch == '-':
                    result = val2 - val1
                elif ch == '+':
                    result = val2 + val1
                elif ch == '*':
                    result = val2 * val1
                else:
                    result = val2 / val1

                stack.push(int(result))

        else:
            stack.push(int(ch))

    return stack.pop()


# print(postFixEvaluation("235*+8-"))

print(postFixEvaluation(["10", "6", "9", "3", "+",
      "-11", "*", "/", "*", "17", "+", "5", "+"]))
# print(postFixEvaluation("10693+-11*/*17+5+"))
