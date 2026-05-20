class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #[2,4,-4,-1]
        #Asteriouds explodes if s < 0 and stack[-1] > 0 and s is not destroyed
            #If |s| > |stack[-1]|, pop from the stack and continue comparison
            #If |s| < |stack[-1]|, nothing happens and we continue to the next asterioud
            #If |s| == |stack[-1]|, we pop from from the stack and end comparison

        #If the asteriod is not destroyed, we will push onto the stack
        stack = []
        for s in asteroids:
            destroyed  = False
            while not destroyed and stack and s < 0 and stack[-1] > 0:
                #Handle asteriod logic here
                if abs(s) > abs(stack[-1]):
                    stack.pop()
                elif abs(s) < abs(stack[-1]):
                    destroyed = True
                else:
                    stack.pop()
                    destroyed = True

            if not destroyed:
                stack.append(s)
        return stack



