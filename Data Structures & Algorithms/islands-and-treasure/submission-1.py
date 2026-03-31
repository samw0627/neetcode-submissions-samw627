class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Use BFS to find the shortest distance from cell to every land

        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    queue.append((i,j))
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                direction = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in direction:
                    if min(r+dr,c+dc) < 0 or r + dr == ROW or c + dc == COL or grid[r + dr][c+dc] != 2147483647:
                        continue
                    grid[r+dr][c+dc] = grid[r][c] + 1
                    queue.append((r+dr,c+dc))
        
        



                    






        