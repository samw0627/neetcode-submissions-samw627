class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                #Move the left pointer
                skipL = s[left+1:right+1]
                skipR = s[left:right]
                if not (skipL == skipL[::-1] or skipR == skipR[::-1]):
                    return False
            left += 1
            right -= 1
        
        return True
        