class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        i=0
        j=0
        maxLength=0
        curLength=0
        while j<len(nums):

            if nums[j]!=1: 
                curLength=0
                i+=j+1
            else:
                curLength+=1

            if curLength>maxLength:
                    maxLength=curLength
           

            j+=1

        return maxLength

        