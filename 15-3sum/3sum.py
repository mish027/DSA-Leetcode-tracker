class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #bruteforce approach TC:O(n^6) SC:O(n^3)
        '''res=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet=sorted(([nums[i],nums[j],nums[k]]))
                        if triplet not in res:
                            res.append(triplet)
                        
        return res'''
        #optimised approach 
        i=0
        
        res=[]
        nums.sort()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                    
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
                
        
        return res


