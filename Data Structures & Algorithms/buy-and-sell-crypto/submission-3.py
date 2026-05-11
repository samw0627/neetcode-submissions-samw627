class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Build dp table
        l = 0
        minPrice = prices[0]
        maxProfit = 0
        for r in range(1,len(prices)):
            if prices[r] < minPrice:
                #shift the left pointer
                l = r
                minPrice = prices[r]
                continue
            maxProfit = max(maxProfit, prices[r]-prices[l])
        return maxProfit
            

        



        