class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        '''low=float('inf')
        maxProfit=0
        

        for i in range(len(prices)):
            if prices[i]<low:
                low=prices[i]
            else:
                profit=prices[i]-low
                if profit>0:
                    maxProfit+=profit
                low=prices[prices.index()+1]
        return maxProfit'''
        
        j=1
        maxProfit=0
        for i in range(len(prices)-1):
            profit=prices[j]-prices[i]
            if profit>0:
                maxProfit+=profit
            j+=1
        return maxProfit
        