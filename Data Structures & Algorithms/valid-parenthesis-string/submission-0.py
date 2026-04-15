class Solution:
    def checkValidString(self, s: str) -> bool:
        #Using 2 stacks to keep track
        left_paren_stack = []
        star_stack = []

        for i,char in enumerate(s):
            if char == "*":
                star_stack.append(i)
                continue
            if char == ")":
                if left_paren_stack:
                    left_paren_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
                continue
            else:
                left_paren_stack.append(i) 

        #Afterwards, clear the left stack using the remaining star stacks
        #left 0
        #star 23

        #left 5
        #star 23
        #(***)(
        print(left_paren_stack)
        print(star_stack)
        while left_paren_stack and star_stack and star_stack[-1] > left_paren_stack[-1]:
            left_paren_stack.pop()
            star_stack.pop()
        
        return not left_paren_stack
             

        

        
        


        
        
        
        