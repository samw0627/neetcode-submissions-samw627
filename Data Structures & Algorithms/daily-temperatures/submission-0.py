class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        # maintain a monotonic decreasing stack

        for i in range(len(temperatures)):

            if not stack:
                stack.append(i)
                continue

            while stack and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
    
        
        return ans



            

        

        
        