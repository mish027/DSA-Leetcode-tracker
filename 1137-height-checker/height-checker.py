class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        i=0
        count=0
        expected=sorted(heights)
        while i<len(heights):
            if heights[i]!=expected[i]:
                count+=1
            i+=1
        return count
        