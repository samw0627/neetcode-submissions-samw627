class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Initialize visited set for pacific and atlantic
        pacific = set()
        atlantic = set()
        ROW = len(heights)
        COL = len(heights[0])

        def dfs(r,c,visited,prev):
            #Base Case : Out of Bounds or visited or value smaller than prev
            if min(r,c) < 0 or r == ROW or c == COL or (r,c) in visited or heights[r][c] < prev:
                return
            #Add visited cell to set
            visited.add((r,c))

            #DFS in all 4 direction
            dfs(r+1, c,visited,heights[r][c])
            dfs(r-1, c,visited,heights[r][c])
            dfs(r, c+1,visited,heights[r][c])
            dfs(r, c-1,visited,heights[r][c])
        
        #Run DFS on the boundary of pacific and atlantic
        for i in range(ROW):
            for j in range(COL):
                #Run From Pacific
                if i == 0 or j == 0:
                    dfs(i,j,pacific,-1)
                #Run from atlantic
                if i == ROW-1 or j == COL-1:
                    dfs(i,j,atlantic,-1)

        #Process the intersection of the sets
        return list(pacific & atlantic)

        