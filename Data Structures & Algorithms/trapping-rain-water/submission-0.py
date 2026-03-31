class Solution:
    def trap(self, height: List[int]) -> int:
        #Build an array for the greatest elements on the left
        #[0,2,0,3,1,0,1,3,2,1]
        #[0,0,2,2,3,3,3,3,3,3]
        #[3,3,3,3,3,3,3,2,1,0]
        #t = min(left,right) - index

        left = []
        right = []
        leftHeight = 0
        rightHeight = 0

        for n in height:
            leftHeight = max(n,leftHeight)
            left.append(leftHeight)
        
        reverse = height[::-1]
        
        for m in reverse:
            rightHeight = max(m, rightHeight)
            right.append(rightHeight)
        right.reverse()

        total = 0
        for item in range(len(height)):
            total += min(left[item],right[item]) - height[item]
        
        return total


        


        

        


        