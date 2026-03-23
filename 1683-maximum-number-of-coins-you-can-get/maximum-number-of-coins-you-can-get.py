class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        k = len(piles)
        sumMedian=0

        for i in range(k-2,(k//3)-1,-2):
            sumMedian+=piles[i]
        return sumMedian
        