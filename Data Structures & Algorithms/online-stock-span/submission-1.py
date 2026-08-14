class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = 0
        self.days = []
        
    def next(self, price: int) -> int:
        #Maintain a montonically decreasing stack, storing the index of the stack
        self.days.append(price)
        while self.stack and self.days[self.stack[-1]] <= price:
            self.stack.pop()
        prev = self.stack[-1] if self.stack else -1
        self.stack.append(self.idx)
        res = self.idx - prev
        self.idx += 1
        return res


        #days: [100,80,60,70,60,75,85]
        #stack: [0,6]
        #idx :6
        #prev: 0
        #res: 1

        #[1,1,1,2,1,4,6]



        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)