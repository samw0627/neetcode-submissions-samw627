class Solution:

    def encode(self, strs: List[str]) -> str:
        #Convert to ASCI code with delimitters signalling how long each char is
        msg = []
        for n in strs:
            msg.append(str(len(n)))
            msg.append('#') 
            msg.append(n) 
        s= "".join(msg) #5Hello5World
        print(s)
        return s

        
        
    def decode(self, s: str) -> List[str]:
        #Read how long the word is k
        #Store the next k character as a string in an array
        #Repeat until we reached the end of the word
        output = []
        ptr = 0
        print(len(s))
        while ptr < len(s): #
            temp = [] 
            #Read the number of characters
            num = []
            while s[ptr] != '#':
                num.append(s[ptr])
                ptr += 1
            
            length = int("".join(num))
                

            #Move the ptr
            ptr += 1 #1
            for n in range(length):
                # Add the characters into temp
                temp.append(s[ptr]) #Hello
                ptr += 1 #6
            out = "".join(temp) #Hello
            output.append(out) #["Hello",""]
        
        return output



            
