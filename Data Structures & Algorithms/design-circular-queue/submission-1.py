class ListNode:
    def __init__(self,value):
        self.val = value
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = ListNode(-1) #Head
        self.tail = ListNode(-1) #Tail
        self.capacity = k
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = 0
        

    def enQueue(self, value: int) -> bool:
        #Remove the first node if full before adding the new node
        if self.isFull():
            return False
    
        newNode = ListNode(value)
        prevNode = self.tail.prev

        prevNode.next = newNode
        newNode.prev = prevNode

        newNode.next = self.tail
        self.tail.prev = newNode

        self.curr += 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        currNode = self.head.next
        nextNode = currNode.next

        self.head.next = nextNode
        nextNode.prev = self.head
        self.curr -= 1
        return True
        

    def Front(self) -> int:
        return self.head.next.val 
        

    def Rear(self) -> int:
        return self.tail.prev.val
        

    def isEmpty(self) -> bool:
        return self.curr == 0
        

    def isFull(self) -> bool:
        return self.curr == self.capacity
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()