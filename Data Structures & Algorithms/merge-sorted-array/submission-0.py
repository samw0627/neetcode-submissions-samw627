class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        final = []
        l,r = 0,0
        while l < m and  r < n:
            if nums1[l] <= nums2[r]:
                final.append(nums1[l])
                l += 1
            else:
                final.append(nums2[r])
                r += 1
        
        if l == m:
            while r < n:
                final.append(nums2[r])
                r += 1
        else:
            while l < m:
                final.append(nums1[l])
                l += 1
        for i,n in enumerate(final):
            nums1[i] = n

        