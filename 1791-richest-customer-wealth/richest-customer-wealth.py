class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth=float('-inf')
        
        for i in range(len(accounts)):
            custMoney=0
            for j in range(len(accounts[0])):
                custMoney+=accounts[i][j]
            if custMoney>maxWealth:
                maxWealth=custMoney
            
        
        return maxWealth