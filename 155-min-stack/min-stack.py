class MinStack:

    def __init__(self):
        self.stack = [0]*30000
        self.minStack = [0]*30000
        self.topV = -1
        self.minTop = -1

    def push(self, val: int) -> None:
        self.topV += 1
        self.stack[self.topV] = val

        if self.minTop == -1 or val <= self.minStack[self.minTop]:
            self.minTop += 1
            self.minStack[self.minTop] = val

    def pop(self) -> None:
        if self.stack[self.topV] == self.minStack[self.minTop]:
            self.minTop -= 1
        self.topV -= 1

    def top(self) -> int:
        return self.stack[self.topV]

    def getMin(self) -> int:
        return self.minStack[self.minTop]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()