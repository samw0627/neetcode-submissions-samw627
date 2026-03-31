class MinStack:

    def __init__(self):
        self.stack = []
        #Store the value and the min element by the time we store the number


        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            minVal = min(val,self.stack[-1][1])
            self.stack.append((val,minVal))
        
    
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
