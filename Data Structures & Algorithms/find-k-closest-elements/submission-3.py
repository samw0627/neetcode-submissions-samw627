class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #Binary Search, Finding the lower bound of the array
        #[2,4,5,8,10,12]
        #[4,2,1,2,4,6]
        #[F,T,T,F,F,F]

        # if |arr[lo]-x| < |arr[mid]-x|
        lo = 0
        hi = len(arr)-k
        while lo < hi:
            mid = (lo + hi) //2
            if abs(arr[mid]-x) <= abs(arr[mid+k]-x):
                hi = mid
            else:
                lo = mid + 1
        
        return arr[lo:lo+k]


        

        
        
        




        