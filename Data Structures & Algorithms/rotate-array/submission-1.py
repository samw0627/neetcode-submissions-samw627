class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[1,2,3,4,5,6,7]
        #[7,1,2,3,4,5,6]
        #[6,7,1,2,3,4,5]
        #[5,6,7,1,2,3,4]
        
        #(i+k)%len(nums)
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            newIndex = (i+k) % len(nums)
            res[newIndex] = nums[i]
        
        for j in range(len(nums)):
            nums[j] = res[j]


        
        
    


        