class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)
        for i in range(1,len(dp)):
            minCoins = float('inf')
            if i in coins:
                dp[i] = 1
                continue
            for c in coins:
                if c <= i:
                    minCoins = min(minCoins,dp[i-c]+1)
            dp[i] = minCoins
        
        return dp[-1] if dp[-1] != float('inf') else -1

                
                
            




        