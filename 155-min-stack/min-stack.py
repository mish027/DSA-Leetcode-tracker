class MinStack:

    def __init__(self):
        self.myStack = []
        self.topV = -1
        

    def push(self, val: int) -> None:

            self.topV +=1
            self.myStack.append(val)
        
        

    def pop(self) -> None:

        self.myStack.pop()
        self.topV-=1
          
    def top(self) -> int:

        return self.myStack[self.topV]
        

    def getMin(self) -> int:

        return min(self.myStack)

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()