from string import ascii_uppercase
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {ch: 0 for ch in ascii_uppercase}
        left = 0
        res = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            while sum(freq.values()) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            
            res = max(res,sum(freq.values()))
        
        return res



        

            


        
        

        #Replacing the character with the highest frequency
        #AAAABCABC
        
        #Window size:



        

        