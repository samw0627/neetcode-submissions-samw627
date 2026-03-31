class MyHashMap:

    def __init__(self):
        self.array = []

    def put(self, key: int, value: int) -> None:
        #check each element of the first entry to see whether the value exists
        for n in self.array:
            if key == n[0]:
                n[1] = value
                return None
        self.array.append([key,value])
        return None

    def get(self, key: int) -> int:
        for n in self.array:
            if key == n[0]:
                return n[1]
        return -1

    def remove(self, key: int) -> None:
        for n in self.array:
            if key == n[0]:
                self.array.remove(n)
        return None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)