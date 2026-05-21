class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #[5,1,3]; target = 3
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            #If l , mid, r is the same, shrink the window and try again
            if target == nums[l] or target== nums[r] or target == nums[mid]:
                return True
            
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            elif nums[l] <= nums[mid]:
                #Left half is sorted
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                #Right Half is Sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid - 1
                else:
                    r = mid - 1
            
        return False


            #[3,3,4,5,1,2,2]
            




        