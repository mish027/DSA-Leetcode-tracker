class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #bruteforce approach O(n^2)
        '''for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return i+1,j+1'''
        #approach two: hashMap TC:O(n) and SC:O(n)
        '''hashMap={}
        for i,num in enumerate(numbers):
            diff=target-num
            if diff in hashMap:
                return hashMap[diff],i+1
            hashMap[num]=i+1'''
        #optimised approach TC:O(n) and SC:O(1)
        i=0
        j=len(numbers)-1

        while i<j:
            if numbers[i]+numbers[j]==target:
                return i+1,j+1
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1


        