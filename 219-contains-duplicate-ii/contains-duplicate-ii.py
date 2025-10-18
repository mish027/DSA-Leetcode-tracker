class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict={}
        for i,num in enumerate(nums):

            if num in dict and abs(i-dict[num])<=k:
                return True
            else:
                dict[num]=i
        
        return False
                


            
                    
        