class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        res=[]
        if len(nums)==0:
            return res

        minValue=nums[0]
        
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                continue
            else:
                if minValue==nums[i-1]:
                    res.append(f"{minValue}")
                else:
                    res.append(f"{minValue}->{nums[i-1]}")
                
                
                minValue=nums[i]

        if minValue==nums[-1]:
            res.append(f"{minValue}")
        else:
            res.append(f"{minValue}->{nums[-1]}")
        
        return res

                
