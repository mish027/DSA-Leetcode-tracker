'''class MinStack:

    def __init__(self):
        self.myStack = []
          

    def push(self, val: int) -> None:

            
            if not self.myStack:
                self.myStack.append((val,val))
            else:
                minV=self.myStack[-1][1]
                self.myStack.append(min((val,val),(val,minV)))

                if val<minV:
                    self.myStack.append((val,val))
                else:
                    self.myStack.append((val,minV))  

    def pop(self) -> None:

        self.myStack.pop()
        
          
    def top(self) -> int:

        return self.myStack[-1][0]
        
    def getMin(self) -> int:

        return self.myStack[-1][1]'''

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#minV=self.myStack[-1][1] push fails when stack is empty
#return self.myStack.pop()[1] should no pop and not modify
'''if not self.myStack:
                self.myStack.append((val,val))

            minV=self.myStack[-1][1]

            if val<minV:
                self.myStack.append((val,val))
            else:
                self.myStack.append((val,minV))

    What happens when stack is empty?

You append (val, val) ✅
Then you continue execution ❌
minV becomes the same value
You append again ❌'''
#topV is unneccery basically


# using 2 stacks
class MinStack:

    def __init__(self):
        self.myStack = []
        self.myMinstack = []
          

    def push(self, val: int) -> None:

                self.myStack.append(val)
                if self.myMinstack:
                    self.myMinstack.append(min(val,self.myMinstack[-1]))
                else:
                    self.myMinstack.append(val)


    def pop(self) -> None:

        self.myStack.pop()
        self.myMinstack.pop()
        
          
    def top(self) -> int:

        return self.myStack[-1]
        
    def getMin(self) -> int:

        return self.myMinstack[-1]
