class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #0/1 Knapsack
        #capacity: 2*len(nums) + 1
        #offset = sum(nums)
        #basecase: dp[offset] = 1

        capacity = 2*sum(nums)+1
        dp = [0 for _ in range(capacity)]
        offset = sum(nums)
        dp[offset] = 1

        for n in nums:
            next_dp = [0 for _ in range(capacity)]
            for j in range(capacity):
                if j+n < capacity:
                    next_dp[j+n] += dp[j]
                if j-n >= 0 :
                    next_dp[j-n] += dp[j]
            dp = next_dp
        return dp[target + offset] if target + offset < len(dp) else 0






        





        

        