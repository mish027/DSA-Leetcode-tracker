class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        diagSum=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j or i+j==len(mat[0])-1:
                    diagSum+=mat[i][j]
        
        return diagSum
                
        