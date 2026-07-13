class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #For each of the element, check if n+1
        curr = set(nums)
        minNum = float('inf')
        minPositive = float('inf')
        for n in nums:
            #Smallest positive integer in the list
            if min(minPositive,n) > 0:
                minPositive = min(minPositive,n)
            #Check the integer before and after
            if n-1 not in curr:
                if n-1 > 0:
                    minNum = min(n-1,minNum)
            if n+1 not in curr:
                if n+1 > 0:
                    minNum = min(n+1,minNum)
            print(minNum)
        if minPositive != 1:
            return 1
        
        return minNum
        
        #[-2,-1,1,100] => 1 [0+1]
        #[-2,8,600,-1] => 1 [2-1]
        #range[1,(2^31)-1]
            


        



        