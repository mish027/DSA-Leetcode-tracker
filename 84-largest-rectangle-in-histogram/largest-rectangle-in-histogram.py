class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        n=len(heights)
        ps=[-1]*n
        ns=[n]*n
        myStack = []

        #prevSmaller
        for i in range(n):
            while myStack and heights[myStack[-1]]>=heights[i]:
                myStack.pop()
            if myStack:
                ps[i]=myStack[-1]
            else:
                ps[i]=-1
            myStack.append(i)

        myStack = [] #important to clear stack

        #nextsmaller
        for i in range(n-1,-1,-1):
            while myStack and heights[myStack[-1]]>=heights[i]:
                myStack.pop()
            if myStack:
                ns[i]=myStack[-1]
            else:
                ns[i]=n
            myStack.append(i)


        #calculate max area
        maxArea=0
        for i in range(n):  
            width = ns[i]-ps[i]-1
            area = width*heights[i]
            maxArea = max(maxArea,area)

        return maxArea
    
        #mistake: forgot to clear stack, make concept more clear
