class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Sliding window of window size k, using a set to keep track of numbers
        numSet = set()

        #Initialize initial set
        for i in range(min(len(nums),k+1)):
            if nums[i] not in numSet:
                numSet.add(nums[i])
            else:
                return True
        
        for r in range(k+1,len(nums)):
            #Remove the element outside of the window
            l = r - k - 1
            numSet.remove(nums[l])
            if nums[r] not in numSet:
                numSet.add(nums[r])
            else:
                return True

        return False 



        

        