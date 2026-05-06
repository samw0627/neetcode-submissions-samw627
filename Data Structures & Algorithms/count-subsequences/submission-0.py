class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        ROW =len(s)
        COL = len(t)
        dp = [[0 for _ in range(COL+1)] for _ in range(ROW+1) ]
        dp[0][0] = 1

        for i in range(1,ROW+1):
            dp[i][0] = 1
        for j in range(1, COL+1):
            dp[0][j] = 0
        
        for i in range(1,ROW+1):
            for j in range(1, COL+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[ROW][COL]
    

        

        