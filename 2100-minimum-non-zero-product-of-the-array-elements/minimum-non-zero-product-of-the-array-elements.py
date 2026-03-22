class Solution:
    def minNonZeroProduct(self, p: int) -> int:
      
      MOD = 1000000007
      maxVal = (1<<p)-1
      secondMax = maxVal - 1 
      power = (1<<(p-1))- 1

      return (maxVal * pow(secondMax,power, MOD))%MOD