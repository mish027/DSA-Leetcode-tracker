class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #bruteforce approach TC:o(n^2) SC:O(1)
        '''for i,num in enumerate(nums):
            if num in nums[i+1:]:
                return True
        
        return False'''

        #better bruteforce approach 
        set_nums=set(nums)
        if len(set_nums)==len(nums):
            return False
        else:
            return True

        