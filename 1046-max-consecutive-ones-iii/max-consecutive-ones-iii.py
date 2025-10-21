class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zerocount=0
        length=float('-inf')
        i=0
        j=0
        while j<len(nums):

            if nums[j]==0:
                zerocount+=1

            while zerocount>k:
                if nums[i]==0:
                    zerocount-=1
                i+=1
            
            length=max(j-i+1,length)

            j+=1

        return length


        