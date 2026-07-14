class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Edge Case: Only one 
        if len(strs) == 1:
            return strs[0]
        #Build the prefix one letter at a time
        min_length = float('inf')
        for s in strs:
            min_length = min(min_length, len(s))
        res = ""
        currChar = ""
        for i in range(min_length):
            for j in range(len(strs) - 1):
                #Compare verticially
                currChar = strs[j][i]
                if currChar != strs[j+1][i]:
                    return res
            res += currChar
        return res
            


        