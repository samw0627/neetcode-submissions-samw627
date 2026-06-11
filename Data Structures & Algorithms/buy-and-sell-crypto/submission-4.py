class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Buy Low Sell High
        l = 0
        minPrice = prices[0]
        profit = -1
        #Move the left pointer if this is the smallest value we have seen
        for r in range(len(prices)):
            if prices[r]< minPrice:
                #Move the left pointer
                l = r
                minPrice = prices[l]
            profit = max(profit, prices[r]-prices[l])
        
        return profit
            
            
            

        

        


        