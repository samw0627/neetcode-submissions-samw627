class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {}
        for i in range(numCourses):
            prereq[i] = []
        for s,e in prerequisites:
            prereq[s].append(e)
        
        visited = set()
        path = set()
        order = []

        def dfs(root):
            nonlocal order
            if root in path:
                return False
            if root in visited:
                return True
            
            path.add(root)

            for n in prereq[root]:
                if not dfs(n):
                    return False
            
            path.remove(root)
            visited.add(root)
            order.append(root)
            return True
        
        for i in prereq:
            if not dfs(i):
                return []
        return order


        