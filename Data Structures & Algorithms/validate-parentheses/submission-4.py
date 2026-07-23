class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {'}':'{',')':'(',']':'['}
        stack = []
        #Push Open Brackets onto the stack
        #If it is a close bracket:
        #   if stack is not empty 
        #       pop the stack
        #       return False if element does not equal parenMap[element]
        #   if stack is empty 
        #       return False
        #   
        #Else push bracket onto stack

        for c in s:
            if c in parenMap:
                if stack:
                    paren = stack.pop()
                    if parenMap[c] != paren:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
