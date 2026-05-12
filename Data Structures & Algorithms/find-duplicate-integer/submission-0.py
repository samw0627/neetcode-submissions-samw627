class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = set()
        for n in nums:
            if n in d:
                return n
            d.add(n)
        

        

        