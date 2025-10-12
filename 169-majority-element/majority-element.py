class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashMap={}
        #better bruteforce approach:
        for num in nums:
            if num in hashMap:
                hashMap[num]+=1
            else:
                hashMap[num]=1
        for num,count in hashMap.items():
            if count>len(nums)//2:
                return num
            


        #optimised approach: 
        '''res=0
        majority=0

        for num in nums:
            if majority==0:
                res=num

            if res==num:
                majority+=1
            else:
                majority-=1

        return res'''