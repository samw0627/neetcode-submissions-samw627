class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Build Adjacency Graph
        adj = {}
        for p in range(numCourses):
            adj[p] = []
        for s,t in prerequisites:
            adj[s].append(t)
        
        path = set()
        visited = set()
        
        #Run DFS to check whether there are cycles in the graph
        def dfs(root):
            
            #If root is in the path, return False
            if root in path:
                return False
            #If root is visited, return True
            if root in visited:
                return True

            #Add root to path
            path.add(root)
            #Add root to visited
            visited.add(root)
            # Run DFS for neighbors of root
            for n in adj[root]:
                if not dfs(n):
                    return False
            #Remove root from path
            path.remove(root)
            return True
        
        #Run search for all unvisited nodes
        for n in range(numCourses):
            if n not in visited:
                if not dfs(n):
                    return False
        return True

        