class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(currTotal, index):
            if index == len(nums):
                return currTotal
            
            include = backtrack(currTotal^nums[index], index + 1) 
            exclude = backtrack(currTotal, index + 1)

            return include+exclude
        
        return backtrack(0,0)
            
            
        




        