class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:    
        negativeCount=0
        i=0
        j=len(grid[0])-1
        
        while j>=0 and i<len(grid):
            if grid[i][j]<0:
                negativeCount+=len(grid)-i
                j-=1
            else:
                i+=1
        
        return negativeCount