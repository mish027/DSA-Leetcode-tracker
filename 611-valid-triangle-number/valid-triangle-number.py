class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

       
        nums.sort()
        l = len(nums)
        i=0
        j=l-1
        
        count = 0
        for k in range(l - 1, 1, -1):   # fix largest side
            i = 0
            j = k - 1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    count+=j-i
                    j-=1
                else:
                    i+=1
        return count

        

        


















































































































































        