class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        visited = set()
        ans = 0
        def dfs(node,parent):
            if node in visited:
                return
            visited.add(node)
            for neighbour in adj[node]:
                if neighbour != parent:
                    dfs(neighbour,node)
        
        for i in range(n):
            if i not in visited:
                dfs(i,-1)
                ans += 1
        return ans





        