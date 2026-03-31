class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final = []
        def dfs (index, currSet):
            if index == len(nums) or sum(currSet) > target:
                return
            if sum(currSet) == target :
                final.append(currSet.copy())
                return

            currSet.append(nums[index])
            dfs(index, currSet)
            currSet.pop()
            dfs(index+1, currSet)

        dfs(0, [])
        return final
