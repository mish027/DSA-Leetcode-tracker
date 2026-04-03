class Solution:
    def trap(self, height: List[int]) -> int:

        #optimal approach: water level is decided by leftMax if its lesser than rightMx and viceversa

        left=0
        right=len(height)-1
        leftMax=0
        rightMax=0
        trap=0
        while left<right:
        
            if height[left]<height[right]:
                leftMax=max(leftMax,height[left])
                trap+=leftMax-height[left]
                left+=1
            else:
                rightMax=max(rightMax,height[right])
                trap+=rightMax-height[right]
                right-=1
        return trap


        '''bruteforce
        k = len(height)
        trap=0
        
        for i in range(k):
            leftMax=0
            rightMax=0
            for j in range(i,-1,-1):
                leftMax=max(leftMax,height[j])
            
            for j in range(i,k):
                rightMax=max(rightMax,height[j])
            
            trap+=(min(rightMax,leftMax)) - height[i]

        return trap
        
        for j in range(i-1,-1): needs reverse step over
        for j in range(i-1,-1,-1):
        left and right indexes are not reset
        edges never hold water'''
        
        
        