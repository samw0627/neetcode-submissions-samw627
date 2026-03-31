class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Buy low sell high
        left,right = 0, 1
        profit = 0
        maxP = 0

        #Find the minimum:
        while right < len(prices):
            if prices[right] - prices[left] < 0:
                left = right
                continue
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
            right += 1

        return maxP
        
        

        

        


        


        

        


        


        