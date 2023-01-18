

class Stack:

    def __init__(self):
        self.stack = []

    def __str__(self):
        return ', '.join(map(str, self.stack))

    def getSize(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

    def push(self, element):
        self.stack.append(element)
        return True

    def pop(self):
        return self.stack.pop()


stack = Stack()

print('stack size: ', stack.getSize())

print('stack push 1: ', stack.push(1))
print('stack push 2: ', stack.push(2))
print('stack push 3: ', stack.push(3))
print('stack push 4: ', stack.push(4))

print('stack contains: ', stack)

print('stack size: ', stack.getSize())

print('stack pop: ', stack.pop())
print('stack pop: ', stack.pop())

print('stack contains: ', stack)


print('stack size: ', stack.getSize())
