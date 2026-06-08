class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #[2,10,10,30,30,30,40,40,40,50,50]
        w, r = 1, 1
        while r < len(nums):
            if nums[r] != nums[r-1]:
                nums[w] = nums[r]
                w += 1
            r += 1
        return w

                



        





        