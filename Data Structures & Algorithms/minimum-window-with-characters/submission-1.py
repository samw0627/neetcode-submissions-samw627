class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # Count characters in t
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        window = {}
        need = len(countT)  # number of unique characters we need
        have = 0 #How many characters in t have their required count satisfied in window
        left = 0
        res = ""
        min_len = float('inf')
        
        for right in range(len(s)):
            char = s[right]
            # Add to window
            window[char] = window.get(char, 0) + 1
            
            # Check if this character is in t and we now have enough of it
            if char in countT and window[char] == countT[char]:
                have += 1
            
            # This is the correct condition: when we have all required characters
            while have == need:
                # Update result if this window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]
                
                # Shrink window from left
                left_char = s[left]
                window[left_char] -= 1
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                left += 1
        
        return res



    
            
        


        



    
            
        


        