class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Run DFS on each of the bordering cell, marking each cell as visited
        #return cells that are reached from pacific and atlantic
        ROW = len(heights)
        COL = len(heights[0])
        pacific = set()
        atlantic = set()
        res = []
        def dfs(r,c,grid,visited,prev):
            if min(r,c) < 0 or r == ROW or c == COL or (r,c) in visited or prev > grid[r][c]:
                return
            visited.add((r,c))

            dfs(r+1,c,grid,visited,grid[r][c])
            dfs(r,c+1,grid,visited,grid[r][c])
            dfs(r-1,c,grid,visited,grid[r][c])
            dfs(r,c-1,grid,visited,grid[r][c])

        
        for i in range(ROW):
            for j in range(COL):
                if i == 0 or j == 0:
                    #Run DFS from Pacific side
                    dfs(i,j,heights,pacific,-1)
                if i == ROW-1 or j == COL - 1:
                     #Run DFS from Atlantic side
                    dfs(i,j,heights,atlantic,-1)

        #Find the union of the two sets
        for p in pacific:
            if p in atlantic:
                res.append([p[0],p[1]])

        return res
        