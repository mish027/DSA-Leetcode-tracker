class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        res=[]
        for candy in candies:
            if (extraCandies+candy)==max(max(candies),extraCandies+candy):
                res.append(True)
            else:
                res.append(False)
        return res
        