class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[None for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        def dfs(i,j):

            #Base case
            if i < len(s) and j == len(p):
                return False
            if i == len(s):
                if j == len(p):
                    return True
                if j + 1 < len(p) and p[j+1] == '*':
                    cache[i][j] = dfs(i, j+2)
                    return cache[i][j]
                return False

            if cache[i][j] != None:
                return cache[i][j]
            
            #Case 1, matching *
            if i < len(s) and j+1 < len(p) and p[j+1] == '*':
                #0 use when the current character no longer matches
                if s[i] != p[j] and p[j] != '.':
                    cache[i][j] = dfs(i,j+2)
                #1 or more uses if the current character still matches
                else:
                    cache[i][j] =  dfs(i+1,j) or dfs(i,j+2)
                return cache[i][j]

            #Case 2, normal match
            if s[i] == p[j] or p[j] == '.':
                cache[i][j] =  dfs(i+1,j+1)
            else:
                cache[i][j] = False
            return cache[i][j]
        
        return dfs(0,0)
        '''
        def dfs(i,j)

            if cache[i][j] != None:
                return cache[i][j]

            #Base case
            if i == len(s) and j == len(p)
                return True
            if i < len(s) and j == len(p)
                return False
            if i == len(s) and (j >= len(p)-1 or p[j+1] != '*'):
                return False
            
            #Case 1, matching *
            if j+1 < len(p) and p[j+1] == '*':
                #0 use when the current character no longer matches
                if s[i] != p[j] and p[j] != '.'
                    cache[i][j] = dfs(i,j+2)
                    return cache[i][j]
                #1 or more uses if the current character still matches
                if s[i]==p[j] or p[j] == '.':
                    cache[i][j] =  dfs(i+1,j) or dfs(i,j+2)
                    return cache[i][j]

            #Case 2, normal match
            if s[i] == p[j] or p[j] == '.'
                cache[i][j] =  dfs(i+1,j+1)
                return cache[i][j]
            else:
                cache[i][j] = False
                return cache[i][j]

            
        '''
        