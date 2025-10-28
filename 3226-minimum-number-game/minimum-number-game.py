class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        res=[]
        while nums:
            second=nums.pop(nums.index(min(nums)))
            first=nums.pop(nums.index(min(nums)))
            res.append(first)
            res.append(second)
        return res