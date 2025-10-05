class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0 #pointer to place the next non-zero element
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]   #swap current element with element at index j
            
                j+=1 #move j to next index for placing non-zero
        