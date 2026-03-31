class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort the list in ascending order
        nums.sort()
        final = []

        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            #-4,-1,-1,0,1,2
            target = -nums[index]
            left, right = index + 1, len(nums) - 1
            while left < right:
                #If left + right is smaller than target, move left
                if nums[left] + nums[right] < target:
                    left+= 1
                    continue
                if nums[left] + nums[right] > target:
                    right -= 1
                    continue
                if nums[left] + nums[right] == target:
                    final.append([nums[left], nums[right] , nums[index]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                #If left + right is larget, move right
                #If left == right: record the final pair, then move left until it is different


        
        return final

        
        