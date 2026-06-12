class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #min k: 1 per hour
        #max k: max(piles)
        #min t: len(piles)
        #max t sum(piles)
        # t = ceil(piles[i] / k)
        
        def totalTime(k):
            t = 0
            for p in piles:
                t += math.ceil(p/k)
            return t

        l = 1
        r = max(piles)
        while l < r:
            #FFFFTTTT
            mid = (l+r) // 2
            if totalTime(mid) <= h: #Based on this rate we can finish the bananas in less than h hours
                #Search on the left side of the array
                r = mid
            else:
                l = mid + 1
        
        return l
       
        


        