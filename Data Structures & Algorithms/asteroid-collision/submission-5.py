class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #[2,3,-4,-1] => [2], [2,3], [2]
        #[-4,-2,4,1] => 
        
        stack = []
        for a in asteroids:
            destroyed = False
            while not destroyed and stack and stack[-1] > 0 and a < 0:
                if -a > stack[-1]:
                    stack.pop()
                    continue
                if -a < stack[-1]:
                    destroyed = True
                if -a == stack[-1]:
                    stack.pop()
                    destroyed = True
            
            if not destroyed:
                stack.append(a)
        return stack
            

                
                
                

            

        

        