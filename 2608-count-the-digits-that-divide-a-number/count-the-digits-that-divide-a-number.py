class Solution:
    def countDigits(self, num: int) -> int:

        count=0
        x=num
        while x>0:

            la_digit=x%10
            if (num%la_digit)==0:
                count+=1
            x=x//10

        return count
        