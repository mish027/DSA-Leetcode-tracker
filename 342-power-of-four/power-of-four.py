class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n>0 and n&(n-1)==0:
            if (0x55555555 & n)!=0:    
                return True
        return False        
        