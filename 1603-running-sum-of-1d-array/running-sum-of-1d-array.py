class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        result=[]
        sumBefore=0
        for i in range(len(nums)):
            sumBefore+=nums[i]
            result.append(sumBefore)
        
        return result
        