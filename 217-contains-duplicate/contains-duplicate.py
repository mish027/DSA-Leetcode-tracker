class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #bruteforce approach TC:o(n^2) SC:O(1)
        '''for i,num in enumerate(nums):
            if num in nums[i+1:]:
                return True
        
        return False'''

        #better bruteforce approach TC: O(n) SC:O(n)
        set_nums=set(nums)
        if len(set_nums)==len(nums):
            return False
        else:
            return True

        #optimised approach using bit manipulation TC:O(n) SC:O(1)      
        res=0
        for num in nums:
            res=res^num
        if res==0:
            return False
        else:
            return True 
        


        