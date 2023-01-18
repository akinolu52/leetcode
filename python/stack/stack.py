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
        if self.isEmpty():
            return None
        return self.stack.pop()
