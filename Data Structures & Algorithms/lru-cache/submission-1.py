class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.hashmap = {}
        # Initialize left and right sentinel nodes
        self.left = Node(-1, 0)  # Most Recently Used
        self.right = Node(-1, 0) # Least Recently Used
        self.left.nxt = self.right
        self.right.prev = self.left
    
    def insert(self, node: Node):
        """Insert node right after the left sentinel (MRU position)."""
        prevNode = self.left
        nextNode = self.left.nxt

        node.nxt = nextNode
        node.prev = prevNode
        prevNode.nxt = node
        nextNode.prev = node
    
    def remove(self, node: Node):
        """Remove an existing node from the linked list."""
        prevNode = node.prev
        nxtNode = node.nxt
        prevNode.nxt = nxtNode
        nxtNode.prev = prevNode

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        get_node = self.hashmap[key]
        val = get_node.value
        # Move the accessed node to the front (MRU)
        self.remove(get_node)
        self.insert(get_node)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # Remove the old node from the linked list
            self.remove(self.hashmap[key])
        # Insert the new node into the linked list and hashmap
        self.hashmap[key] = Node(key, value)
        self.insert(self.hashmap[key])
        # If capacity is exceeded, remove the LRU node
        if len(self.hashmap) > self.capacity:
            # The node to remove is the one before the right sentinel
            lru = self.right.prev
            self.remove(lru)
            del self.hashmap[lru.key]


        
