class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1

        # Phase 1: Find pivot (index of smallest element)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1

        pivot = low

        # Phase 2: Binary search in the correct half
        # If pivot == 0, we can't trust the pivot finder due to duplicates
        if pivot == 0:
            return target in nums  # O(n) fallback

        elif target >= nums[0]:
            low, high = 0, pivot - 1
        else:
            low, high = pivot, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return True

        return False
        