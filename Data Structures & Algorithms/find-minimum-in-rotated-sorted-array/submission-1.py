class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Find the pivot of the rotated array
        lo = 0
        hi = len(nums)-1

        #if mid < hi => Search left side 
        #if mid > hi => Search right side

        
        while lo < hi:
            mid = (lo+hi) // 2
            
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]
        

        #[3,4,5,6,1,2]
        #[6,1,2,3,4,5]



        

        
        