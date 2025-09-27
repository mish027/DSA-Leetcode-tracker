class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low=float('inf')
        maxProfit=0

        for price in prices:

            if price<low:
                low=price
            elif price-low>maxProfit:
                maxProfit=price-low
        
        return maxProfit



        
            
            


