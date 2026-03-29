class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #using stack
        myStack=[]
        for ch in s:
            myStack.append(ch)

        k=len(myStack)
        for i in range(k):
                s[i]=myStack.pop()
        return s


        # using two pointer swap
        '''l=0
        h=len(s)-1
        while l<h:
            s[l],s[h]=s[h],s[l]
            l+=1
            h-=1
        return "".join(s)'''