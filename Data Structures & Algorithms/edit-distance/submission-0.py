class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROW = len(word1)+1
        COL = len(word2)+1

        dp = [[0 for _ in range(COL)]for _ in range(ROW)]
        
        for i in range(1,ROW):
            dp[i][0] = i
        
        for j in range(1,COL):
            dp[0][j] = j
        
        for i in range(1,ROW):
            for j in range(1,COL):
                if word1[i-1]== word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1]+1)
        print(dp)
        return dp[-1][-1]
        



        