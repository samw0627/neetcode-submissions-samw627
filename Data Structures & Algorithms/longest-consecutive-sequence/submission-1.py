class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Start of a sequence, n-1 is not in the array
        numsset = set()
        for n in nums:
            numsset.add(n)
        maxlength = 0
        for n in nums:
            if n-1 not in numsset:
                #Start building the sequence from here
                curr = n
                length = 1
                while True:
                    if curr+1 in numsset:
                        length += 1
                        curr += 1
                    else:
                        break
                maxlength = max(maxlength,length)
        
        
        return maxlength










        
        

        