class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []

        def backtracking (currSet, index):
            #Base Case
            if index == len(nums):
                final.append(currSet.copy())
                return
            #include currentNumber
            currSet.append(nums[index])
            backtracking(currSet, index + 1)
            currSet.pop()
            backtracking (currSet, index+1)
                
        backtracking([],0)
        return final