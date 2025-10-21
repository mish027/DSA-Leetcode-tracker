class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:    
        negativeCount=0
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if grid[i][j]>0:
                    break
                elif grid[i][j]<0:
                    negativeCount+=1
        return negativeCount
        