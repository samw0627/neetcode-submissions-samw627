class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Check each character on the array one at a time
        #strs[0][0] == strs[0][1] == strs[0][2] == ...strs[0][n] where m is the str and n is the 
        #find min length of string
        min_length = 200
        for i in strs:
            min_length = min(min_length,len(i))
    
        num_str = len(strs)
        ans = ""
        for m in range(min_length):
            for n in range(num_str-1):
                if strs[n][m] != strs[n+1][m]:
                    return ans
            ans+= strs[0][m]
        
        return ans