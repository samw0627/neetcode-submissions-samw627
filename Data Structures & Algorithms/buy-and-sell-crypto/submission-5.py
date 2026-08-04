class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[10,1,5,7,6,8]
        #Buy at the lowest point
        maxProfit = 0
        #left pointer will keep track of the smallest element seen
        #Move the right pointer and calculate the max profit
        l = 0
        for r in range(len(prices)):
            #Move l if prices[r] < prices[l]
            if prices[r] < prices[l]:
                l = r
            #Calculate the maxProfit at each step
            maxProfit = max(maxProfit,prices[r]-prices[l])
        return maxProfit
            
        
        

        
        