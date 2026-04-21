class Solution:
    #Check whether a specific substring is a palindrome


    def longestPalindrome(self, s: str) -> str:
        def helper(s, l, r):
            maxLength = -1
            res = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #Keep track of the max length palindrome
                if r-l+1 > maxLength:
                    res = s[l:r+1]
                    maxLength = r-l+1
                l -= 1
                r += 1
            return res

        res = 0
        maxOdd,maxEven = "",""
        for i in range(len(s)):

            odd = helper(s,i,i)
            maxOdd = odd if len(maxOdd) < len(odd) else maxOdd
            even = helper(s,i,i+1)
            maxEven = even if len(maxEven) < len(even) else maxEven
        return maxOdd if len(maxOdd)>=len(maxEven) else maxEven

        
        

        