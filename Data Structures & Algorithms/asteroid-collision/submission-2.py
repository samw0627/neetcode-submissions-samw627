class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        #[2,4,-1]
        for i in range(1,len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                destroyed = False
                while stack and stack[-1] > 0 and asteroids[i] < 0:
                    if abs(asteroids[i]) > abs(stack[-1]):
                        stack.pop()
                    elif abs(asteroids[i]) < abs(stack[-1]):
                        destroyed = True
                        break
                    else:
                        stack.pop()
                        destroyed = True
                        break
                    
                if not destroyed:
                    stack.append(asteroids[i])

        return stack
        