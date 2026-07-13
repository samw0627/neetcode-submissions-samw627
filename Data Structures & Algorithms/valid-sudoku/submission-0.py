class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])
        def checker(start_row,end_row, start_col,end_col,check):
            if check == 'g':
                dup = set()
            for i in range(start_row,end_row):
                if check =='h' or check =='v':
                    dup = set()
                for j in range(start_col,end_col):
                    if check == 'h' or check =='g':
                        curr = board[i][j]
                        curr = int(curr) if curr != "." else -1
                        if curr == -1:
                            continue
                        if curr in dup:
                            return False
                    if check == 'v':
                        curr = board[j][i]
                        curr = int(curr) if curr != "." else -1
                        if curr == -1:
                            continue
                        if curr in dup:
                            return False                        
                    dup.add(curr)
            return True
        #Check the horizontal components
        if not checker(0,ROW,0,COL,'h'):
            return False
        #Check Vertical Compoenents
        if not checker(0,ROW,0,COL,'v'):
            return False
        #Check each subsquare
        for x in range(ROW):
            for y in range(COL):
                if x % 3 == 0 and y % 3 == 0:
                    if not checker(x,x+3,y,y+3,'g'):
                        return False
        
        return True
                    






        