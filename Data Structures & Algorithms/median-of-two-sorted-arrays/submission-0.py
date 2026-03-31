class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2

        if len(B) < len(A): #We'll make sure A is the shortest array
            A,B = B,A
        
        total = len(A) + len(B)
        half = total // 2

        l,r = 0, len(A) - 1 #We're doing Binary Search on A

        while True:
            i = (l + r) // 2 # Middle index for A
            j = half - i - 2 #Middle index for B. Offset by 2 because both arrays are 0 based

            #Set elements for partitions for A and B, to minimize edge cases set both ends of array by -inf and inf
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                #Found the right partition
                if total % 2 == 0:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
                
                return min(Aright,Bright)
            elif Aleft > Bright:
                #Too many elements from A, move the right pointer
                r = i - 1
            else:
                l = i + 1
        














        