class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closest_sum=float('inf')
        for i in range(len(nums)-2):

            j=i+1
            k=len(nums)-1
            
            while j<k:
                cursum=nums[i]+nums[j]+nums[k]
                if abs(target-cursum)<abs(target-closest_sum):
                    closest_sum=cursum
                
                if cursum<target:
                    j+=1
                elif cursum>target:
                    k-=1
                else:
                    return target #perfect match
        return closest_sum
        