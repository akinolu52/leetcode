
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def __str__(self):
        return ', '.join(map(str, self.stack))

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.isMinEmpty():
            print('exec')
            self.mins.append(val)
        else:
            self.mins.append(min(self.getMin(), val))

        return None
    
    def isEmpty(self) -> bool:
        return len(self.stack) == 0

    # extra function to check if min list is empty
    def isMinEmpty(self) -> bool:
        return len(self.mins) == 0

    def pop(self) -> None:
        if not self.isEmpty():
            self.stack.pop()
            self.mins.pop()
        return None

    def top(self) -> int:
        return -1 if self.isEmpty() else self.stack[-1]

    def getMin(self) -> int:
        print('get min -> ', self.mins)
        return self.mins[-1]
        # if self.isMinEmpty() else None
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(3)
# obj.push(0)
print('stack: ', obj)
print("getMin: ", obj.getMin())

obj.pop()
print('stack: ', obj)
print("getMin: ", obj.getMin())

# obj.pop()
# print('stack: ', obj)
# print("getMin: ", obj.getMin())

# obj.pop()
# print('stack: ', obj)
# print("getMin: ", obj.getMin())

# param_3 = obj.top()
# print("MinStack ", param_3)
# param_4 = obj.getMin()
# print("MinStack ", param_4)
