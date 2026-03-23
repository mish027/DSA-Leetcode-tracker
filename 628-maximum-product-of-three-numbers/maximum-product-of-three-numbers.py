class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()
        k= len(nums)

        return max(nums[0]*nums[1]*nums[k-1],nums[k-1]*nums[k-2]*nums[k-3])

        '''if nums[0]>=0 or nums[k-1]<0:
            return nums[k-1]*nums[k-2]*nums[k-3]
        else:
            return max(nums[0]*nums[1]*nums[k-1],nums[k-1]*nums[k-2]*nums[k-3])'''
        

        
        


        