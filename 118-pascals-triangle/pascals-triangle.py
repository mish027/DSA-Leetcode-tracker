class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        mat=[[0]*(i+1) for i in range(numRows)]
        '''for i in range(numRows):
            for j in range(i+1):
                mat[i][j]=0'''

        for i in range(numRows):
            for j in range(i+1):

                if j==0:
                    mat[i][j]=1
                elif i==j:
                    mat[i][i]=1

                else:
                    mat[i][j]=mat[i-1][j-1]+mat[i-1][j]
        return mat

        
        