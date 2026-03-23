class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        
        nums.sort()
        k= len(nums)

        sumMed=0
        for i in range(k-2,(k//3)-1,-2):
            sumMed+=nums[i]
        return sumMed
