class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #initiate fast and slow pointer
        #if fast and slow pointer interscts, the number will be the duplicate number

        f,s = nums[nums[0]],nums[0]
        
        while f != s:
            f = nums[nums[f]]
            s = nums[s]
        print(f,s)
        s = 0
        while f != s:
            f = nums[f]
            s = nums[s]
        return f

        

        

        