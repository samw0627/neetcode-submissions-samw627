class Solution:
    def trap(self, height: List[int]) -> int:
        #Highest on the LHS
        #[0,2,0,3,1,0,1,3,2,1]
        #[0,0,2,2,3,3,3,3,3,3]
        #[3,3,3,3,3,3,3,2,1,0]

        total = 0
        left, right = [0 for _ in range(len(height))],[0 for _ in range(len(height))]
        maxLeft,maxRight = -1,-1
        for l in range(len(height)):
            maxLeft = max(maxLeft,height[l])
            left[l] = maxLeft
        
        for r in range(len(height)-1,-1,-1):
            maxRight = max(maxRight,height[r])
            right[r] = maxRight
        for i in range(len(height)):
            res = min(left[i],right[i]) - height[i] 
            if res >= 0:
                total += res
        
        return total
