class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subset = [0 for _ in range(k)]
        
        if sum(nums) % k != 0:
            return False
        total = sum(nums) // k
        nums.sort(reverse=True)

        #Edge Case, if the subsets can't be subdivided equally

        def dfs(i):
            #We reached the last digit
            if i == len(nums):
                return True
            for j in range(k):
                #Skip to the next number if the subset is full
                if subset[j] + nums[i] > total:
                    continue
                subset[j] += nums[i]
                if dfs(i+1):
                    return True
                subset[j] -= nums[i]
                
                #Pruning: if the current integer is 0 after trying all ints, then we can return 0
                if subset[j] == 0:
                    break
            
            return False


        
        return dfs(0)


        
        


        