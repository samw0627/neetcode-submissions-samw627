class Solution:
    #Need to have the same number of character
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        #Put in Hashset
        anagramMap_s = {}
        anagramMap_t = {}
        for char in s:
            anagramMap_s[char] = anagramMap_s.get(char,0)+1
        for char in t:
            anagramMap_t[char] = anagramMap_t.get(char,0)+1
        for char in s:
            #Check if key is in both maps
            if char not in anagramMap_t:
                return False
            else:
                if anagramMap_s[char] != anagramMap_t[char]:
                    return False
        
        return True

        


        