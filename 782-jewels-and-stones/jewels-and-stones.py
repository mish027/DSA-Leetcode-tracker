class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        count=0
        jewelsSet=set(jewels)  
        for stone in stones:
            if stone in jewelsSet:
                count+=1
        return count

    