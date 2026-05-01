class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * m
        for i in range(n):
            currRow = [0] * m
            for r in range(m-1,-1,-1):
                if r == m-1:
                    currRow[r] = 1
                    continue
                currRow[r] = prevRow[r] + currRow[r+1]
            prevRow = currRow

        return prevRow[0]
            
        
        




        