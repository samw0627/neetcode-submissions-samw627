class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #
        def calculateDaysToShip(cap):
            total, days = 0, 1
            for index in range(len(weights)):
                    if total + weights[index] > cap:
                        days += 1
                        total = weights[index]
                    else:
                        total += weights[index]
            return days

        def feasible(mid):
            print("Days:", calculateDaysToShip(mid))
            if calculateDaysToShip(mid) > days:
                return False
            else:
                return True
        
        lo, hi = max(weights), sum(weights)

        while lo < hi:
            mid = (lo + hi)//2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo



            
            

            
        



        