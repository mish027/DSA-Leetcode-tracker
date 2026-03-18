class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        m=len(grid)
        n=len(grid[0])

        total=0
        sumG=0
        for i in range(m):
            for j in range(n):
                total+=grid[i][j]
        
        if total%2!=0:
            return False

        target=total//2
        
        #horizontal cut
        for i in range(m-1):
            for j in range(n):
                sumG+=grid[i][j]
        
            if sumG==target:
                return True
        
        sumG=0
        #vertical cut
        for j in range(n-1):
            for i in range(m):
                sumG+=grid[i][j]
        
            if sumG==target:
                return True
        
        return False
        
