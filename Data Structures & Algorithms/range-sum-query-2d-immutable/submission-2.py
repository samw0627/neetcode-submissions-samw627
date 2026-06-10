class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        #initailize matrix sum
        sum_matrix = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        print(sum_matrix)
        #Iinitialize the rest of the matrix
        for i in range(1,len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                sum_matrix[i][j] = sum_matrix[i-1][j] + sum_matrix[i][j-1] + matrix[i-1][j-1] - sum_matrix[i-1][j-1]
        
        self.summation = sum_matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.summation[row2+1][col2+1] - self.summation[row2+1][col1] - self.summation[row1][col2+1] + self.summation[row1][col1]
        
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)