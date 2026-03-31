class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = ["+","-","*","/"]
        res = 0
        for n in tokens:
            if n in operation:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if n == "+":
                    res = num1+num2
                if n == "-":
                    res = num2-num1
                if n == "*":
                    res = num1*num2
                if n == "/":
                    res = int(num2/num1)

                stack.append(str(res))
            else:
                stack.append(str(n))

        return int(stack[-1])
        

        