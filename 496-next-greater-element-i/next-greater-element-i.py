class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res=[]
        
        for num in nums1:
            flag=0
            if num in nums2:
                index_in_nums2=nums2.index(num)
            for i in range(index_in_nums2+1,len(nums2)):
                if nums2[i]>nums2[index_in_nums2]:
                    res.append(nums2[i])
                    flag=1
                    break
            if flag==0:
                res.append(-1)
            
            
                

            
        return res

        