class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        #bruteforce approach:
        res=[]
        hashMap={}
        for num in nums:
            if num not in hashMap:
                hashMap[num]=0
            hashMap[num]+=1
        
        for item,count in hashMap.items():
            if count>(len(nums)//3):
                res.append(item)
        return res





        
        