class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        i=0
        j=0
        maxLength=0
        curLength=0
        while j<len(nums):

            if nums[j]!=1:
                
                curLength=0
            else:
                curLength+=1
            j+=1
            
            maxLength=max(maxLength,curLength) 
        return maxLength

        