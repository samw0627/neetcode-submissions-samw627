class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newSet=set()
        for item in nums:
            if(item in newSet):
                return True
            else:
                newSet.add(item)
        return False