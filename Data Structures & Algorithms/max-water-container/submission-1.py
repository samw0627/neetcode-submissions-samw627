class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Loop through all bars, moving the one with the smallest value
        l = 0
        r = len(heights) - 1
        maxArea = -1
        while l < r:
            maxArea = max(maxArea,min(heights[l],heights[r])*(r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
        