class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #bruteforce approach TC:O(n^sq) and SC:O(1)
        '''for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                diff=prices[i]-prices[j]
                if diff>0 and diff>maxProt'''
        

        #optimised approach TC:O(n) and SC:O(1)
        low=float('inf')
        maxProfit=0
        for price in prices:                        
            if price<low:
                low=price
            elif price-low>maxProfit:
                maxProfit=price-low
        
        return maxProfit



        
            
            


