class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0

        final = ""
        shortest = -1
        minLength = -1
        if len(word1) <= len(word2):
            shortest = 1
            minLength = len(word1)
        else:
            shortest = 2
            minLength = len(word2)

        while l < minLength:
            final += word1[l]
            l += 1
            final += word2[r]
            r += 1
        
        if shortest == 1:
            final += word2[r:]
        else:
            final += word1[l:]
        
        return final
        


        