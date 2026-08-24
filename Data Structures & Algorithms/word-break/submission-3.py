class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[-1] = True
        n = len(s)
        for i in range(n-1,-1,-1):
            for j in range(i+1,n+1):
                if s[i:j] in wordDict and dp[j]:
                    dp[i] = True
                    break
        return dp[0]
                
                
                


            
            


        