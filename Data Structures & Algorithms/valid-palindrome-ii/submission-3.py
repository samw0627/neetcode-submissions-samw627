class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(l,r,skip):
            #If s[l] != s[r] and skip = True: return False
            #If s[l] != s[r] and skip. = False: Recursively search s[l] and s[r]
            #If s[l] == s[r], recursively search l+1 and r-1
            #Exit when l >= r
            if l >= r:
                return True
            if s[l] != s[r]:
                if not skip:
                    return False
                else:
                    return checkPalindrome(l+1,r,False) or checkPalindrome(l,r-1,False)
            else:
                return checkPalindrome(l+1,r-1,skip)
        return checkPalindrome(0,len(s)-1,True)

        