class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Consecutive: n-1 exisits in the set
        numset = set()
        start = []
        res = 0
        numset = set(nums)
        #identify the start of the list
        for n in nums:
            if n-1 not in numset:
                start.append(n)
        
        #For each ends of the list,calculate the consecutive length
        for s in start:
            curr = 1
            while s+1 in numset:
                curr += 1
                s += 1
            res = max(res,curr)
        
        return res











        
        

        