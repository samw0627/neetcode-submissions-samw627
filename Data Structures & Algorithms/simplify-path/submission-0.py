class Solution:
    def simplifyPath(self, path: str) -> str:
        #/neetcode/.. => / => Using a stack to track the depth of the directory
        #Check whether the a slash is folliwed by another slash, remove

        stack = []
        curr = ""
        for char in path+"/":
            if char == "/":
                #Get the directory name before the next slash
                if curr =="..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += char
        
        return "/" + "/".join(stack)
                
                



        

        

        