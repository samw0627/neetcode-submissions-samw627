class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Build Adjacency List
        adj = {i: [] for i in range(numCourses)}
        for start,end in prerequisites:
            adj[start].append(end)
        
        visited = set()
        path = set()
        topo = []

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
            
            topo.append(node)
            path.remove(node)

            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return topo

        