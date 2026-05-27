class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        for i in range(numCourses):
            prereq[i] = []
        for s,e in prerequisites:
            prereq[s].append(e)
        
        visited = set()
        path = set()

        def dfs(root):
            if root in path:
                return False
            if root in visited:
                return True
            
            path.add(root)
            #Visit all neighbours
            for n in prereq[root]:
                print(prereq[root])
                if not dfs(n):
                    return False
            path.remove(root)
            visited.add(root)
            return True
        for i in prereq:
            if i not in visited:
                if not dfs(i):
                    return False
        
        return True
                
                



        