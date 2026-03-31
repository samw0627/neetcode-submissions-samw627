class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        def dfs (currSet, index):
            #Base Case
            if index == len(nums):
                if currSet not in final:
                    final.append(currSet.copy())
                return
            
            #Add a optopn
            currSet.append(nums[index])
            dfs(currSet, index+1)
            #Remove a option
            currSet.pop()
            dfs(currSet,index+1)
        
        dfs([],0)
        return final

        