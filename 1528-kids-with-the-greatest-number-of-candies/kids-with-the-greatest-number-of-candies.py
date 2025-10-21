class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        res=[]
        maxValue=max(candies)
        for candy in candies:
            if (extraCandies+candy)==max(maxValue,extraCandies+candy):
                res.append(True)
            else:
                res.append(False)
        return res
        