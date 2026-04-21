class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i,cache):
            if i >= len(s):
                return 1             
            if i in cache:
                return cache[i]
            #Picking only 1 digit
            if s[i] != '0':
                cache[i] += dfs(i+1,cache)
                #Pick the next 2 digit
                if i + 1 < len(s) and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
                    cache[i] += dfs(i+2,cache)
            return cache[i]
        
        cache = defaultdict(int)
        return dfs(0,cache)
        
        
        