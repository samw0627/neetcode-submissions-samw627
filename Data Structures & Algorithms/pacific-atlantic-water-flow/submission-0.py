class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        final = []
        #Track previous height to make comparison easier
        def dfs(r,c,visited,prevHeight):
            if min(r,c) < 0 or r == ROW or c == COL or (r,c) in visited or heights[r][c] < prevHeight:
                return
            
            visited.add((r,c))
            neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
            for nr,nc in neighbors:
                dfs(r+nr, c+nc, visited,heights[r][c])

        
        for i in range(ROW):
            for j in range(COL):
                #Pacific Set
                if i == 0 or j == 0:
                    dfs(i,j,pacific_visited, 0)
                #Atlantic Set
                if i == ROW-1 or j == COL-1:
                    dfs(i,j,atlantic_visited, 0)
        
        for cell in pacific_visited:
            if cell in atlantic_visited:
                r,c = cell
                final.append([r,c])

        return final


            
        


                    

                





        