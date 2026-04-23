class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums) 
        dp = [1]*n
        dp[n-1] = 1
        #[3, 1, 4, 1, 5]
        #[9,1,4,2,3,3,7]
        #[4,10,4,3,8,9]
        minNum = nums[-1]

        for i in range(n-2, -1,-1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],dp[j] + 1)
        print(dp)
        return max(dp)
        



        