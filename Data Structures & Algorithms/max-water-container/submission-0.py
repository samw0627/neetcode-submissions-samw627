class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Area = min(heights[h],height[w]) * r-l
        l,r = 0,len(heights)-1
        area = 0
        while l < r:
            area = max(area,min(heights[r],heights[l]) * (r-l))
            if heights[r] > heights[l]:
                l += 1
            else:
                r-= 1

        return area


        
        