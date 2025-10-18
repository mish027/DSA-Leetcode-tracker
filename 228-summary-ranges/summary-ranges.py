class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        res=[]
        if len(nums)==0:
            return res
        if len(nums)==1:
            return [f"{nums[0]}"]
        minValue=nums[0]
        
        maxValue=float('-inf')
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                maxValue=nums[i]
            else:
                if minValue==nums[i-1]:
                    res.append(f"{minValue}")
                else:
                    res.append(f"{minValue}->{maxValue}")
                
                
                minValue=nums[i]

        if minValue==nums[i]:
            res.append(f"{minValue}")
        else:
            res.append(f"{minValue}->{maxValue}")
        
        return res

                
