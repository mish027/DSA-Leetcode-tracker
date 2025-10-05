class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        result=[[0]*len(matrix) for i in  range(len(matrix[0]))] #gives len(matrix) columns and 1st element length rows
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][i]=matrix[i][j]

        return result
    
    '''The time complexity of this transpose function is O(m * n), where m is the number of rows in the input matrix and n is the number of columns. This is because the nested loops iterate over each element of the matrix exactly once, performing a constant-time assignment operation for each element.

The space complexity is also O(m * n). The function creates a new result matrix with dimensions n (rows of the original matrix) by m (columns of the original matrix). This additional space is proportional to the size of the input matrix, as it stores the transposed data.'''