class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #Use backtracking to explore all possibilties
        #Using a set to keep track of used sticks
        
        #Check for the target length
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        length = total // 4

        n = len(matchsticks)
        matchsticks.sort(reverse = True)
        used = [False for _ in range(n)]
        def dfs(index,remain,side):
            #Base Case: we have reached the end of the third side and curr == side
            if side == 3:
                return True
            if remain == 0:
                return dfs(0,length,side+1)
            for j in range(index,n):
                if matchsticks[j] > remain or used[j]:
                    continue
                used[j] = True
                if dfs(j+1,remain - matchsticks[j], side):
                    return True
                used[j] = False

                while j + 1 < n and matchsticks[j] == matchsticks[j+1]:
                    j += 1
            
            return False

        return dfs(0,length,0)

            

                
            
            
                


            

                    
                    



            
                





        
        