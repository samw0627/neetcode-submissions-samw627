class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Implement Cyclic Sort
        n = len(nums)
        i = 0

        for i in range(n):
            while 1<= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                index = nums[i]-1
                nums[i], nums[index] = nums[index], nums[i]
        
        for j in range(n):
            if nums[j] != j+1:
                return j+1

        return n+1

        
        

        #Move the elements to
        #[1,2,4,5,6,3,1]
        #[1,2,5,4,6,3,1]
        #[1,2,6,4,5,3,1]
        #[1,2,3,4,5,6,1]
        