class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        found = False
        visited = [[False]*COLS for _ in range(ROWS)]
        

        def dfs(r,c,i):
            #Base case: Index equals to the length of the word
            if i == len(word):
                return True
             #Check for bounds
            if min(r,c) < 0 or r > ROWS-1 or c > COLS-1 or word[i] != board[r][c] or visited[r][c] == True:
                return False    
            visited[r][c] = True 
            
            found = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            
            visited[r][c] = False

            return found
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                     if dfs(r,c,0):
                        return True
        
        return False
                





               

                
                


            


        