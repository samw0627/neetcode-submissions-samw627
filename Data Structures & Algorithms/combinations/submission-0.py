class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i+1 for i in range(n)]
        final = []
        def dfs(currSet, index):
            if index == len(nums):
                if len(currSet) == k:
                    final.append(currSet.copy())
                return

            currSet.append(nums[index])
            dfs(currSet, index + 1)
            currSet.pop()
            dfs(currSet, index + 1)

        dfs([],0)
        return final

        