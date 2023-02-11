from infix_to_postfix import infixToPostfix


def infixToPrefix(s: str) -> str:
    result = infixToPostfix(s)

    return result[::-1]


s = 'A+B*C'  # +A*BC
print(infixToPostfix(s))

s = 'A*B+C/D'  # +*AB/CD
print(infixToPostfix(s))
