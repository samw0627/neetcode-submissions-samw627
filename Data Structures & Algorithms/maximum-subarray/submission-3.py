class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]

        for n in nums:
            currSum = max(currSum,0) #Reset to 0 if the current Sum is negative
            currSum += n
            maxSum = max(currSum,maxSum)

        return maxSum
        
        