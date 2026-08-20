class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #Build a graph that builds that shows the different combination of the lock, then run BFS
        combination = defaultdict(list)
        queue = deque()
        queue.append("0000")
        visited = set()
        ans = 0
        def children(code):
            result = []
            if code in deadends:
                return []
            for i in range(len(code)):
                for change in [1,-1]:
                    newDigit = str((int(code[i])+ change)% 10)
                    newCode = code[:i] + newDigit + code[i+1:]
                    result.append(newCode)
            return result
        
        while queue:
            for i in range(len(queue)):
                #Pop the queue
                #Mark the node as visited
                curr = queue.popleft()
                if curr == target:
                    return ans
                neigh = children(curr)
                 #Add neighbors to queue
                for n in neigh:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
            ans += 1

        return -1


       
           

            
            
                

        
        
            



        

       


        