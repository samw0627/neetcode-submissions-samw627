class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Initialize a hashmap of counting frequencies

        if len(s1) > len(s2):
            return False
        target  = [0]*26
        for i in s1:
            target[ord(i)-ord('a')] += 1
        window = [0]*26
        for j in range(0,len(s1)):
            window[ord(s2[j])-ord('a')] += 1
        ans = False
        if window == target:
            return True
        for r in range(len(s1),len(s2)):
            l = r-len(s1)
            window[ord(s2[l])-ord('a')] -= 1
            window[ord(s2[r])-ord('a')] += 1
            if window == target:
                return True

        return False


        



        

        
        