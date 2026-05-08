class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        length = len(nums)
        nums = [1] + nums + [1] #Pad the nums with 1
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        #starting at length 1, iterature up
        for l in range(1,length+1):
            for i in range(1,length-l+2):
                j = i + l - 1
                maxVal = -1
                for k in range(i,j+1):
                    maxVal = max(maxVal,dp[i][k-1]+dp[k+1][j] + nums[i-1]*nums[j+1]*nums[k])
                    dp[i][j] = maxVal
        
        return dp[1][length]



        

        
       


        