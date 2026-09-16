class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n+1)]
        wordset = set(wordDict)
        dp[-1] = True
        #dp[k] = True means that starting at position k, we can break it down to words in wordDict

        for i in range(n,-1,-1):
            for j in range(i+1,n+1):

                if s[i:j] in wordset and dp[j] == True:
                    dp[i] = True
                    break
        
        return dp[0]
                    
            


        