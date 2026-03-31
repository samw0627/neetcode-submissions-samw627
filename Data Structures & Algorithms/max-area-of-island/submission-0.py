class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        maxArea = 0
        def dfs(r,c):
            nonlocal area
            if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] == 0:
                return
            grid[r][c] = 0
            area += 1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j)
                    maxArea = max(area,maxArea)
        
        return maxArea


         
        
        