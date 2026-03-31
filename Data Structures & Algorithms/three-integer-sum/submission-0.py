class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort the numbers
        nums.sort()
        res = []
        #[-4,-1,-1,0,1,2]
        #Loop through each integer
        for i,a in enumerate(nums):
            if a > 0:
                break
            if a == nums[i-1] and i > 0:
                continue 
            L = i + 1
            R = len(nums)-1
            while L < R:                    
                threeSum = a + nums[L] + nums[R]
                if threeSum < 0:
                    L += 1
                elif threeSum > 0:
                    R -= 1
                else:
                    res.append([a,nums[L],nums[R]])
                    L += 1 #Shift the pointer to find additional pairs
                    R -= 1 
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        return res

                

        