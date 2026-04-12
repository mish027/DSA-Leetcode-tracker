class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        g=len(nums)
        dist=float('inf')
        flag=0

        for i in range(g):
            for j in range(i+1,g):
                for k in range(j+1,g):
                    if nums[i]==nums[j]==nums[k]:
                        dist=min(dist,abs(i - j) + abs(j - k) + abs(k - i))
                        flag=1
                
        if flag==0:
            return -1
        else:
            return dist

        
        

#mistake 1 min of 0 and something always 0
#soting changes index