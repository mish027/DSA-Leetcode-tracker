class Solution:
    def isValid(self, s: str) -> bool:

        myDict = {')':'(', '}':'{',']':'['}
        myStack = []
        for ch in s:
            if ch in myDict.values():
                myStack.append(ch)
            else:
                if myStack and myStack[-1]==myDict[ch]:
                    myStack.pop()
                else:
                    return False
        return len(myStack)==0

        #take edge case s = "]"

        