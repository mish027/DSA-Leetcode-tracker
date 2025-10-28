class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        sumElements=sum(nums)
        sumDigits=0
        for num in nums:
            while num>0:
                ladigit=num%10
                sumDigits+=ladigit
                num=num//10
            sumElements+=num

        return abs(sumElements-sumDigits)
        