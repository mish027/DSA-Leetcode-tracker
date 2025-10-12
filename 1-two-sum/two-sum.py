class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force approach:
        '''for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j'''
        
        #optimised approach:
        hashMap={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in hashMap:
                return i,hashMap[diff]
            hashMap[num]=i
        