class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        res=[]
        hashSet=set()

        for num in nums:
            hashSet.add(num)

        for i in range(1,len(nums)+1):
            if i not in hashSet:
                res.append(i)
        
        return res
        