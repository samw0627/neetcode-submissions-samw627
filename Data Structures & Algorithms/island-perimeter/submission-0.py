class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #Find cell with land
        visited = set()
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(r,c,visited):
            #Base Case
            res = 0
            if min(r,c) < 0 or r == ROW or c == COL or (r,c) in visited or grid[r][c] == 0:
                return res
            visited.add((r,c))
            #Check whether the 4 perimeter is water or boundary
            for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
                if min(r+dr,c+dc) < 0 or r+dr == ROW or c+dc == COL or grid[r+dr][c+dc] == 0:
                    res+= 1
            
            res += dfs(r+1,c,visited)
            res += dfs(r-1,c,visited)
            res += dfs(r,c-1,visited)
            res += dfs(r,c+1,visited)

            return res
        
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and grid[r][c] == 1:
                    return dfs(r,c,visited)
            

        