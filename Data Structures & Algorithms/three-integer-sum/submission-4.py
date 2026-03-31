class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort the numbers
        nums.sort()
        #[-4,-1,-1,0,1,2]
        final = []
        for i in range(len(nums)):
            #Skip when the nums[i] == nums[i+1]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1, len(nums) - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    final.append([nums[l],nums[r],-target])
                    #Check for duplicates
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return final
        





        