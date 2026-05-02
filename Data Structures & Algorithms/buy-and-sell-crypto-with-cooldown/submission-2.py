class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for n in range(len(prices))] for m in range(2)]
        #0 = Hold, 1 = Not Hold
        for c in range(len(prices)):
            if c == 0:
                dp[0][c] = -prices[c]
                dp[1][c] = 0
            elif c == 1:
                dp[0][c] = max(-prices[c],dp[0][c-1])
                dp[1][c] = max(dp[0][c-1]+prices[c],dp[1][c-1])
            else:
                dp[0][c] = max(dp[1][c-2]-prices[c],dp[0][c-1])
                dp[1][c] = max(dp[0][c-1]+prices[c],dp[1][c-1])
        
        return dp[-1][-1]
        



                
        


        