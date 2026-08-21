class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[-1] = 0

        for i in range(n-1,-1,-1):
            skip = 1 + dp[i+1]
            use = float('inf')
            for j in range(i,n+1):
                if s[i:j] in dictionary:
                    #Take the minimum
                    use = min(use,dp[j])
            dp[i] = min(skip,use)
        print(dp)
        return dp[0]

        


        

        

        
        


        

        
        