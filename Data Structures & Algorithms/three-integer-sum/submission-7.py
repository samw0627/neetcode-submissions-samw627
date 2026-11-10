class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort the array
        res = []
        nums.sort()
        #[-4,-1,-1,0,1,2]
        for i in range(len(nums)-1):
            #Duplicate check
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    #Move both pointers
                    l += 1
                    r -= 1
                    while l < r:
                        #Move to the next distinct entry
                        if nums[l] == nums[l-1]:
                            l += 1
                        else:
                            break
        return res

            
            



        