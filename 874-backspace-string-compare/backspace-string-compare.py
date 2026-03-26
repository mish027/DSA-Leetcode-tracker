class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        myStack1 = []
        myStack2= []
        for ch in s:
            if ch=='#':
                if myStack1:
                    myStack1.pop()
            else:
                myStack1.append(ch)

        for ch in t:
            if ch=='#':
                if myStack2:
                    myStack2.pop()
            else:
                myStack2.append(ch)
        
        if myStack1==myStack2:
            return True
        else:
            return False

        
        

