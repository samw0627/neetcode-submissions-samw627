class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #determine whether that substring contains the same count of 
    
        result = False
        count = Counter(s1)
        size = len(s1)
        
        window = Counter(s2[:size])
        if window ==count:
            return True

        for right in range(size, len(s2)):
            window[s2[right]] += 1
            window[s2[right-size]] -= 1
            if window == count:
                return True
        
        return False
            


        



        