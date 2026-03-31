class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Multi-source BFS on rotten
        ROW = len(grid)
        COL = len(grid[0])
        q = deque()
        fresh_orange = 0
        for i in range(ROW):
            for j in range (COL):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_orange += 1
        level = 0
        while q and fresh_orange > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
                for n in neighbors:
                    nr,nc = r+n[0], c+n[1]
                    if min(nr,nc) < 0 or nr == ROW or nc == COL or grid[nr][nc] != 1:
                        continue
                    q.append((nr,nc))
                    fresh_orange -= 1
                    grid[nr][nc] = 2
            level += 1
            
        
        return level if fresh_orange == 0 else -1




        


        