class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prevRow = [0]*(len(text1)+1)
        
        for m in range(len(text2)-1,-1,-1):
            currRow = [0]*(len(text1)+1)
            for n in range(len(text1)-1,-1,-1):
                if text1[n] == text2[m]: #
                    currRow[n] = 1 + prevRow[n+1]
                else:
                    currRow[n] = max(currRow[n+1],prevRow[n])
            prevRow = currRow
        
        return prevRow[0]


        

        '''
            cat
           c0000
           r0000
           a0000
           b0000
           t0000 c
            0000 p
        
        '''
        