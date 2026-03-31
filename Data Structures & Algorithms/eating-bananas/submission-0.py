import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min: 1, max: max(piles)
        # hours: ceil(num / k) for each element in array
        low, high = 1, max(piles)

        def feasible(mid):
            total = 0
            for num in piles:
                total += math.ceil(num/mid)
            if total > h:
                return False
            else:
                return True

        while low < high:
            mid = (low+high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        
        return low


        

        
        