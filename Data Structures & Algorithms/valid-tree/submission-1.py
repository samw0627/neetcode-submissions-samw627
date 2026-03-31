class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Build adjacency list, storing edges 2 times
        adj = {i: [] for i in range(n)}
        for start,end in edges:
            adj[start].append(end)
            adj[end].append(start)
        visited = set()

        # A tree has n-1 edges:
        if len(edges) != n-1:
            return False

        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            #Search all neighbors
            for neighbour in adj[node]:
                if neighbour != parent:
                    dfs(neighbour, node)

        dfs(0,-1)
        
        if len(visited) == n:
            return True
        else:
            return False
        



            