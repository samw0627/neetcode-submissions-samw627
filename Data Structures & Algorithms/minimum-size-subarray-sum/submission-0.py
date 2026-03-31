class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #target
        window = 0
        ans = float("inf")
        left = 0

        for right in range(len(nums)):
            window += nums[right]
            #while valid
            while window >= target:
                ans = min(ans, right-left+1)
                window -= nums[left]
                left += 1
        
        return ans if ans < float("inf") else 0
        






        

        




        
        
        
        