class Solution:
    def isValid(self, s: str) -> bool:
        paren = {"(":")", "[":"]", "{":"}"}
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" or char == "}" or char == "]":
                if stack and paren[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return True if not stack else False

            

        