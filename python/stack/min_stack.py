import sys

class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
        # self.secondMinVal = sys.maxsize

    def __str__(self):
        return ', '.join(map(str, self.stack))

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minVal):
            self.minVal.append(val)
        else:
            # check if smaller than the last element in the stack
            if val < self.minVal[-1]:
                self.minVal.appen
        return None
    
    def isEmpty(self) -> bool:
        return len(self.stack) == 0

    def pop(self) -> None:
        if self.isEmpty():
            return None
        else:
            poppedVal = self.stack.pop()
            # print('pop:', poppedVal, self.minVal, self.secondMinVal)

            if self.minVal == poppedVal:
                self.minVal = self.secondMinVal

            return None

    def top(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
print('stack: ', obj)
print("getMin: ", obj.getMin())

obj.pop()
print('stack: ', obj)
print("getMin: ", obj.getMin())

obj.pop()
print('stack: ', obj)
print("getMin: ", obj.getMin())

obj.pop()
print('stack: ', obj)
print("getMin: ", obj.getMin())
# param_3 = obj.top()
# print("MinStack ", param_3)
# param_4 = obj.getMin()
# print("MinStack ", param_4)
