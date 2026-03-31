class Node:
    def __init__(self,key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

              

    def get(self, key: int) -> int:
        #If value doesn't exisits, return -1
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        #Move the node to the front of the list
        self.delete(node)
        self.add(node)
        return node.val
        
    

    def put(self, key: int, value: int) -> None:
        
        #If key is in hashmap, then we will move it
        if key in self.hashmap:
            self.delete(self.hashmap[key])
        self.hashmap[key] = Node(key,value)
        self.add(self.hashmap[key])
        #If capacity is reach, delete the LRU node
        if len(self.hashmap) > self.capacity:
            key = self.tail.prev.key
            self.delete(self.tail.prev)
            del self.hashmap[key]
        #If a key already exisits, first remove the current entry
        #Create a new Node and link it with hasmap


        
    
    #Move the node from LRU to MRU
    def add(self, node):
        nextNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextNode
        nextNode.prev = node

    
    #Remove the node from the cache
    def delete(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode




'''

'''
