class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROW = len(grid)
        COL = len(grid[0])
        res = 0
        
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            direction = [[0,1],[0,-1],[1,0],[-1,0]]

            while q:
                for n in range(len(q)):
                    #Pop the queue
                    r,c = q.popleft()
                    #Mark cell as visited
                    visited.add((r,c))
                    #Push unvisited neighbors onto queue
                    for dr,dc in direction:
                        #edge case check
                        if min(r+dr,c+dc) < 0 or r+dr == ROW or c+dc == COL or grid[r+dr][c+dc] == '0' or (r+dr,c+dc) in visited:
                            continue
                        q.append((r+dr,c+dc))
            
                    

  
        #Run BFS on each island
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    res += 1
        
        return res



        
                    
            

        