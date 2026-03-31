class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.mapping = {}
        self.capacity = capacity
        #Initialize head and tail Node
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

   
    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        else:
            self.remove(self.mapping[key])
            self.add(self.mapping[key])
            return self.mapping[key].val          

    def put(self, key: int, value: int) -> None: 
        #First Remove
        if key in self.mapping:
            self.remove(self.mapping[key])
        
        self.mapping[key] = Node(key, value)
        self.add(self.mapping[key])
        
        #Check whehter capacity reached and pop the tail
        if len(self.mapping) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.mapping[lru.key]
        return

    def remove(self, node):
        previous = node.prev
        nxt = node.next
        previous.next = nxt
        nxt.prev = previous

    def add(self,node):
        nextNode = self.head.next
        node.prev = self.head
        node.next = nextNode
        self.head.next = node
        nextNode.prev = node




