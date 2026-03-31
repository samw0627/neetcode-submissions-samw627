class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random
        def quicksort(arr, s, e):
            #base case: when array = 1
            if e-s+1 <= 1:
                return arr

            # Choose a random pivot to avoid O(n^2) on sorted/reverse arrays
            pivot_idx = random.randint(s, e)
            arr[e], arr[pivot_idx] = arr[pivot_idx], arr[e]

            #Set the pivot and the left pointer
            pivot = arr[e]
            left = s
            #Compare value and swap curr with left pointer if val is smaller than pivot
            for i in range(s,e):
                if arr[i] < pivot:
                    temp = arr[i]
                    arr[i] = arr[left]
                    arr[left] = temp
                    left+= 1
            
            #Move Pivot to the next element
            arr[e] = arr[left]
            arr[left] = pivot
            
            quicksort(arr, s, left-1)

            quicksort(arr, left+1, e)

            return arr
        
        return quicksort(nums, 0, len(nums)-1)

        