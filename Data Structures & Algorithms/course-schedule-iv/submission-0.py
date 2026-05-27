class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        prereq = {}
        for i in range(numCourses):
            adj[i] = []
            prereq[i] = set()
        for a,b in prerequisites:
            adj[a].append(b)
            prereq[a].add(b)
        res = []
        visited = set()
        order = []
        def dfs(root):
            if root in visited:
                return
            for n in adj[root]:
                dfs(n)
                prereq[root].update(prereq[n])#Merge the current preReq with root 
            visited.add(root)
            return

        for i in range(numCourses):
            if i not in visited:
                dfs(i)
        
        for q in queries:
            if q[1] not in prereq[q[0]]:
                res.append(False)
            else:
                res.append(True)
        
        return res




        
        




        
            


        