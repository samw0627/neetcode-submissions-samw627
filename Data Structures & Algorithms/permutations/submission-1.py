class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(currSet):
            if len(currSet) == len(nums):
                res.append(currSet.copy())
                return
            
            for i in nums:
                if i not in currSet:
                    currSet.append(i)
                    dfs(currSet)
                    currSet.pop()
        
        dfs([])
        return res




        