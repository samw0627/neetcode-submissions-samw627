class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])

        row_boolean = set()
        col_boolean = set()

        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    row_boolean.add(i)
                    col_boolean.add(j)
        
        #Set Rows to 0
        for r in row_boolean:
            for c in range(COL):
                matrix[r][c] = 0
        #Set Cols to 0
        for r in range(ROW):
            for c in col_boolean:
                matrix[r][c] = 0

        
        

        
        