class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        nums2=[]
        o=True
        e=True
        for num in nums1:
            nums2.append(num)

        #check for all odd
        flag=0
        for num in nums2:
            if (num%2==0):
                flag=1
        if (flag==0):
            o=True
        
        #check for all even
        flag1=0
        for num in nums2:
            if (num%2==1):
                flag1=1
        if (flag==0):
            e=True

        return o or e
