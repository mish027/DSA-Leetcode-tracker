class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        max1=float('-inf')
        max2=float('-inf')
        max3=float('-inf')
        for i in range(len(nums)):
            if nums[i]!=max1 and nums[i]!=max2  and nums[i]!=max3:
                if nums[i]>max1:
                    max3=max2
                    max2=max1
                    max1=nums[i]
                elif nums[i]>max2:
                    max3=max2
                    max2=nums[i]
                elif nums[i]>max3:
                    max3=nums[i]
        if max3==float('-inf'):
            return max1
        else:
            return max3
                

        