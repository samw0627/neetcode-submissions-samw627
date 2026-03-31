class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Check if the region is reachable from the border
        ROW  = len(board)
        COL = len(board[0])

        def dfs(r,c):
            if min(r,c) < 0 or r == ROW or c == COL or board[r][c] == 'X' or board[r][c] == "#":
                return
            board[r][c] = "#"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(ROW):
            for j in range(COL):
                if i == 0 or i == ROW-1 or j ==0 or j == COL-1:
                    dfs(i,j)
        
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"





        
        