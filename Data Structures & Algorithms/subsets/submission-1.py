class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Build list from scratch
        res = []
        def dfs(i,currset):
            #Base Case: We have reached the end of the set
            if i == len(nums):
                res.append(currset.copy())
                return
            
            #Include i in the current set
            currset.append(nums[i])
            dfs(i+1,currset)
            
            #Exclude i in the current set
            currset.remove(nums[i])
            dfs(i+1,currset)

        dfs(0,[])
        return res

        
        