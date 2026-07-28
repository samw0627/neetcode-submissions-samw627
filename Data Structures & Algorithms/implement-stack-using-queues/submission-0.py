class MyStack:

    def __init__(self):
        self.queue = deque()
        self.num = 0
        
    def push(self, x: int) -> None:
        self.queue.append((x,self.num))
        self.num += 1
        

    def pop(self) -> int:
        #Repeatedly push and pop onto the queue until curr[1] == self.num
        curr = self.queue.popleft()
        while curr[1] != self.num - 1:
            self.queue.append(curr)
            curr = self.queue.popleft()
        self.num -= 1
        return curr[0]
    def top(self) -> int:
        top = -1
        curr = self.queue.popleft()

        while curr[1] != self.num - 1:
            self.queue.append(curr)
            curr = self.queue.popleft()
        
        top = curr[0]
        self.queue.append(curr)
        return top

    def empty(self) -> bool:
        return True if self.num == 0 else False
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()