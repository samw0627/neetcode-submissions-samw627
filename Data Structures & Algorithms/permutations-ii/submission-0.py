class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()# Sort to check for duplicates
        final = []
        seen = [0]*len(nums)
        def dfs(currSet):
            #BaseCase: when the length of the set equals nums
            if len(currSet) == len(nums):
                final.append(currSet.copy())
                return
            #Loop through each valid options
            for i in range(len(nums)):
                if seen[i] == 1:
                    continue
                # Skip the same element if the previous same element was not used
                if i > 0 and nums[i] == nums[i-1] and seen[i-1] == 0:
                    continue
                seen[i] = 1
                currSet.append(nums[i])
                dfs(currSet)
                currSet.pop()
                seen[i] = 0

        dfs([])
        return final

        