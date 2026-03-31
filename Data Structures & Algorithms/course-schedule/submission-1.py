class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for start, end in prerequisites:
            adj[start].append(end)
        
        #Topological sort
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            visited.add(node)
            path.add(node)

            for neigh in adj[node]:
                if dfs(neigh) == False:
                    return False
            
            path.remove(node)

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True

        

            
        


        

        