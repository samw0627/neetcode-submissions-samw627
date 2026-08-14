class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = []
        

    def push(self, val: int) -> None:
        if self.minNum:
            self.minNum.append(min(self.minNum[-1],val))
        else:
            self.minNum.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minNum.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minNum[-1]

        
