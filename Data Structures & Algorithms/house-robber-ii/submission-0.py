class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 3:
            return max(nums[0],nums[1],nums[2])
        
        dp1 = [-1]* (len(nums) -1)
        dp1[0],dp1[1] = nums[0],nums[1]
        max1,max2 = -1,-1
        for i in range(2,len(nums)-1):
            dp1[i] = max(dp1[:i-1]) + nums[i]
            max1 = max(max1,dp1[i])

        print(dp1)
        dp2 = [-1]*(len(nums) -1)
        dp2[0],dp2[1] = nums[1],nums[2]
        for j in range(2,len(nums)-1):
            dp2[j] = max(dp2[:j-1]) + nums[j+1]
            max2 = max(max2,dp2[i])
        print(dp2)

        return max(max1, max2)

        
