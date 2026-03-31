class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        
        for i,h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i if not stack else i - index
                maxArea = max(maxArea, width*height)
                start = index
            
            stack.append((start,h))
        
        return maxArea
            
            




        