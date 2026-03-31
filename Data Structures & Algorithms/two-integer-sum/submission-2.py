class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #For each index check whether diff exists in the array
        if len(nums) == 2:
            return[0,1]
        for i, num2 in enumerate(nums):
            diff = target - num2
            #if diff exists
            if diff in nums:
                #Get the index of the elemnet
                indexList = [i for i in range(len(nums)) if nums[i] == diff]
                for index in indexList:
                    if index != i:
                        return [min(i,index),max(i,index)]

        
            
