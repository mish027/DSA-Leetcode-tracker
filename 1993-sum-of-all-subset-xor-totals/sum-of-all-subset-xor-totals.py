class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        mainSum=0
        n=len(nums)
        for i in range(2**n):
            sumXOR=0
            for j in range(n):
                if (i>>j) & 1:    
                    sumXOR=sumXOR^nums[j]
            mainSum+=sumXOR
        return mainSum
        