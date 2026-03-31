class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() #Sort such that you would not see a duplicate number
        final = []
        def dfs(currSet,index):
            if sum(currSet) == target:
                final.append(currSet.copy())
                return
            if sum(currSet) > target or index >= len(candidates):
                return
            
            currSet.append(candidates[index])
            dfs(currSet, index+1)
            currSet.pop()
            while  index < len(candidates)-1 and candidates[index] == candidates[index+1] :
                index += 1
            dfs(currSet, index+1)

        dfs([],0)
        return final
        