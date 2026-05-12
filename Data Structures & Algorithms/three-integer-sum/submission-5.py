class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        #                
        #Sort the list of numbers
        nums.sort()
        final = []
        for i in range(len(nums)):
            target = -nums[i]
            #Skip current iteratiion if nums[i] == nums[i-1] 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                #if l+r > target, move right pointer
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    final.append([nums[l],nums[r],nums[i]])
                    l += 1
                    r -= 1
                    #Move the left pointer if there are duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return final


        



        