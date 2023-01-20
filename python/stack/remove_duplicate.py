
def removeDuplicates(s: str) -> str:
    def empty(_stack):
        return len(_stack) == 0

    stack = []

    # print(empty(_stack=stack), len(stack))

    for ch in s:
        prev = ''
        # print(stack, ch, prev)
        if not empty(_stack=stack):
            prev = stack[-1]

        if ch == prev:
            if not empty(_stack=stack):
                stack.pop()
        else:
            stack.append(ch)

        

    return ''.join(stack)


print(removeDuplicates("abbaca"))
print(removeDuplicates("aaaaaaaa"))
print(removeDuplicates("aaaaaaaaa"))


