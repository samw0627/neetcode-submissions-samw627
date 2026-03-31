class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i,h in enumerate(heights + [0]):
            while stack and stack[-1][1] > h:
                topBar, height = stack.pop()
                width = i if not stack else i - stack[-1][0] - 1
                maxArea = max(maxArea, width*height)
            
            stack.append((i,h))
        
        return maxArea
            
            




        