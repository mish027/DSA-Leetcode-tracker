class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:  

        i=0
        j=i+1

        while j<len(nums) and i<len(nums):
            if nums[i]%2==0:
                i+=2
            
            elif nums[j]%2!=0:
                j+=2
            
            else:
                nums[i],nums[j]=nums[j],nums[i]
                i+=2
                j+=2
        return nums
            
            

