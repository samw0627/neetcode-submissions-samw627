class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Build adjacency list, storing edges 2 times
        adj = {i: [] for i in range(n)}
        for start,end in edges:
            adj[start].append(end)
            adj[end].append(start)
        visited = set()

        # A tree has n-1 edges: Check for cycles
        if len(edges) != n-1:
            return False

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            #Search all neighbors
            for neighbour in adj[node]:
                if neighbour != parent:
                    if not dfs(neighbour, node):
                        return False
            return True

        return dfs(0,-1) and len(visited) == n
    
        



            