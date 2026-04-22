class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = nums[0]
        minimum = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            prevMax = maximum
            prevMin = minimum
            maximum = max(nums[i],nums[i]*prevMax, nums[i]*prevMin)
            minimum = min(nums[i],nums[i]*prevMax, nums[i]*prevMin)
            res = max(res,maximum)

        return res



        

        
        