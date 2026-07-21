class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        #[-4,-1,-1,0,1,2]
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l,r = i+1,len(nums)-1
            while l<r:
                res = nums[l] + nums[r]
                if res < target:
                    l += 1
                elif res > target:
                    r -= 1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l +=1
                    r -= 1
                    #Check for duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
    
        return ans




        