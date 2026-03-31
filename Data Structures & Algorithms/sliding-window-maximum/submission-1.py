class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices
        l = 0
        
        for r in range(len(nums)):
            # 1. Maintain the Monotonic Deque
            # Remove smaller values from the back (they can't be the max)
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # 2. Check if the window has reached size k
            if (r - l + 1) == k:
                # The front of the deque is the maximum for this window
                output.append(nums[q[0]])
                
                # 3. Slide the window: move l forward
                # But first, check if the index we're about to leave was the max
                if q[0] == l:
                    q.popleft()
                
                l += 1
                
        return output
            
            
                

                
            
            
            





        
        
        


        
        