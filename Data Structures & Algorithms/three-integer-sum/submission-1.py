class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        nums.sort()
        final = []

        for index, n in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            target = -n
            left = index + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    final.append([-target,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1   
                else:
                    right -= 1

        return final