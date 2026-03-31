class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = 0
        r = len(nums)-1


        #if the nums[i] is 0, swap  nums[l] and increment both i and l
        #if the nums[i] is 2, swap nums[r] with nums[i], decrease the r pointer by 1
        #if nums[i] is 1, increment i

        while i <= r:
            if nums[i] == 0:
                nums[i],nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1

        return nums