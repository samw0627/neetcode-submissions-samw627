class Solution:
    def jump(self, nums: List[int]) -> int:
        #Based on the current value array, search the all values in that range
        n = len(nums) - 1
        numJumps = 0
        currentEnd = 0 #The index where the level ends
        farthest = 0 #THe index where the index can take you the farthest
        #Pick the maximum value
        for i in range(n):
            farthest = max(farthest, i + nums[i])

            if i == currentEnd:
                numJumps += 1
                currentEnd = farthest #We'll move the pointer to the farthest point

            if currentEnd >= n:
                break
        
        return numJumps
        #nums = [2,4,1,1,1,1]
        #i    = [0,1,2,3,4,5]

        
        
        