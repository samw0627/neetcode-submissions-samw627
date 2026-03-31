class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.klargest = k

        

    def add(self, val: int) -> int:
        ans = 0
        self.nums.append(val)
        copy = self.nums.copy()
        heapq.heapify(copy)
        while len(copy) != self.klargest:
            ans = heapq.heappop(copy)
        return heapq.heappop(copy)

        
