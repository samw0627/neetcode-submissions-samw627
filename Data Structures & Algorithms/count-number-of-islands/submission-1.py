class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROW = len(grid)
        COL = len(grid[0])
        res = 0
        def dfs(r,c, grid,visited):
            #Base Case
            if min(r,c) < 0 or r == ROW or c == COL or (r,c) in visited or grid[r][c] == '0':
                return
            
            visited.add((r,c))
            dfs(r+1,c,grid,visited)
            dfs(r,c+1,grid,visited)
            dfs(r-1,c,grid,visited)
            dfs(r,c-1,grid,visited)
        
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and grid[r][c] == '1':
                    dfs(r,c,grid,visited)
                    res += 1
        
        return res
                    
            

        