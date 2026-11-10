class Solution:
    def isValid(self, s: str) -> bool:
        paren_mapping = {"}":"{", ")":"(", "]":"["}
        stack = []
        #Loop through each character
        for c in s:
            
            if c in paren_mapping:
                #Pop the stack if the top equals to c
                if stack and stack[-1] == paren_mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False

                   

            

        