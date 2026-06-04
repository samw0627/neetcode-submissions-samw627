class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []

        
        currNum = ""
        currStr = ""
        
        for char in s:
            #Case 1: if char is a digit store in currNum
            if char.isdigit():
                currNum = currNum + char
            #Case2: if char is alphabet, add to currStr
            if char.isalpha():
                currStr = currStr + char
                
            #Case3: if char is an [ store in currNum in Numstack and str in strStack
            if char == "[":
                numStack.append(int(currNum))
                currNum = ""
                strStack.append(currStr)
                currStr = ""

            #Case4: if char is ], pop the numStack and apply transformation to currStr, 
            #If strStack is not empty, pop the string and apply
            if char == "]":
                rep = numStack.pop()
                currStr = currStr * rep
                if strStack:
                    c = strStack.pop()
                    currStr = c+currStr
                    
        return currStr



        

        
        