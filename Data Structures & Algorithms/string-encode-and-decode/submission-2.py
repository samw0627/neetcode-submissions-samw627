class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        return res



    def decode(self, s: str) -> List[str]:
        final = []
        length = len(s)
        i = 0
        while i < length:
            #Read in the int
            curr = ""
            while s[i] != "#":
                curr += s[i]
                i+=1
            char_length = int(curr)
            curr = ""
            i += 1
            #Consume letters
            for _ in range(char_length):
                curr+=s[i]
                i += 1
            final.append(curr)
        
        return final
                


        

