class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        chosen_arr = [0]*len(nums)
        final = []
        def dfs(currSet):
            #Base Case: All elements are chosen
            if len(currSet) == len(nums):
                final.append(currSet.copy())
                return
            #Recurse for all possibilities
            for i in range(len(nums)):
                if chosen_arr[i] == 1:
                    continue
                currSet.append(nums[i])
                chosen_arr[i] = 1
                dfs(currSet)
                chosen_arr[i] = 0
                currSet.pop()

        dfs([])
        return final



            