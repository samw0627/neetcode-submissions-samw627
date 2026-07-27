class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[1,2,3,4,5,6,7,8]
        k = k % len(nums)

        def reverse(start,end):
            l = start
            r = end
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)