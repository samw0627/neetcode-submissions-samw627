class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0 ,len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return True
            #Determine which half is sorted
            if nums[l] < nums[m]:
                #left half is sorted, do binary search in that range
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            elif nums[l] == nums[m]:
                l += 1
                        
        return False

            #[3,5,6,0,0,1,2]
            #[6,0,0,1,2,3,5]
            
        