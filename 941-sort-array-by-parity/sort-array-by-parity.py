class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]%2==0: #use nums[i]&1 for faster computation
                i+=1
            elif nums[j]%2!=0:
                j-=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
        return nums

        