class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        memo = [False]*len(nums)
        memo[goal] = True

        for i in range(goal-1,-1, -1):
            if any(memo[i+1: i+nums[i]+1]) == True:
                memo[i] = True
            else:
                memo[i] = False
        print(memo)
        return memo[0]
        

     

        

     

        