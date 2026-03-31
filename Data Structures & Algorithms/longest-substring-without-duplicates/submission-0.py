class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            char = s[r]
            while char in window:
                window.remove(s[l])
                l += 1
            window.add(char)
            ans = max(ans, r-l+1)
        
        return ans


            
        


        