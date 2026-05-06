class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        cache = [[0 for _ in range(COL)] for _ in range(ROW)]
        maxVal = -1
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c):
            if cache[r][c] != 0:
                return cache[r][c]
            maxNeigh = 0
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if min(nr,nc) >= 0 and nr < ROW and nc < COL and matrix[nr][nc] > matrix[r][c]:
                    neigh = dfs(nr,nc)
                    maxNeigh = max(maxNeigh,neigh)
                    #cache[r][c] = 1 + max(dfs(r+1,c,matrix[r][c]),dfs(r,c+1, matrix[r][c]),dfs(r-1,c, matrix[r][c]),dfs(r,c-1, matrix[r][c]))
            cache[r][c] = maxNeigh+1
            return cache[r][c]
        
        for i in range(ROW):
            for j in range(COL):
                maxVal = max(maxVal,dfs(i,j))
        
        return maxVal
                
                