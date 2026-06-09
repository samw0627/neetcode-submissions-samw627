class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(l,r,edits):
            if s[l] != s[r] and edits == False:
                return False
            if l >= r:
                return True
            if s[l] == s[r]:
                return checkPalindrome(l+1,r-1,edits)
            else:
                return checkPalindrome(l,r-1,False) or checkPalindrome(l+1,r,False)
                

        return checkPalindrome(0,len(s)-1,True)
        #aca 
        # abbadc
        # abbda



        