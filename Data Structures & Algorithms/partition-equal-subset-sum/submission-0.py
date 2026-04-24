class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0 :
            return False
        target = sum(nums) // 2
        def dfs(i, current_sum):

            if current_sum == target:
                return True
            if i >= len(nums) or current_sum > target:
                return False
            
            if dfs(i+1, current_sum + nums[i]):
                return True

            if dfs(i+1, current_sum):
                return True
            
            return False
            
        return dfs(0,0)
            
        
        
        
        

        