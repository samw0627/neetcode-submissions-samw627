class ListNode:
    def __init__(self,key,val):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:
    
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def add(self,node):
        #Move this to the front of the list
        #Connect all related Nodes
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head

    
    def remove(self,node):
        #Get the node before and after it
        node1 = node.prev
        node2 = node.next
        #Rewire connection
        node1.next = node2
        node2.prev = node1

    def get(self, key: int) -> int:
    
        if key not in self.hashmap:
            return -1
        #Get Node
        node = self.hashmap[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        #Update the value of the node if it exisits
        if key in self.hashmap:
            #Update Val
            self.hashmap[key].val = value
             #Move Node to Front
            self.remove(self.hashmap[key])
            self.add(self.hashmap[key])
        #Else Add the Node in Cache
        else:
            #If we are at capacity
            if len(self.hashmap) == self.capacity:
                #delete the last node and its key
                last_node = self.tail.prev
                self.remove(last_node)
                del self.hashmap[last_node.key]
            newNode = ListNode(key,value)
            self.hashmap[key] = newNode
            self.add(newNode)




        
