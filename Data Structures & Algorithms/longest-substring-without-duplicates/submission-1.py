class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Using a set to keep track of characters
        #Flexible sliding window(Longest)
        window = set()
        ans = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
                   
            window.add(s[r])    
            ans = max(ans, r-l+1)
        
        return ans




        
        