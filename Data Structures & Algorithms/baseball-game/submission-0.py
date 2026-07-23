class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            curr = o
            if curr == 'D':
                top = stack[-1]
                curr = int(top) * 2
            elif curr == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                curr = int(num1)+int(num2)
            elif curr == "C":
                stack.pop()
                continue
            
            stack.append(int(curr))
        
        return sum(stack)



        