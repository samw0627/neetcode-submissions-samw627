class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Swap top and bottom rows
        matrix.reverse()
        #Transpose matrix
        '''
        [3,4]
        [1,2]
        '''
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]


        


        


        