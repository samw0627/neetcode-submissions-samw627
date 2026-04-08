class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def build_graph(edges):
            graph = defaultdict(list)
            for u,v in edges:
                graph[u].append(v)
            return graph
        
        adj = build_graph(tickets)

        for e in adj.values():
            e.sort()
        print(adj)

        #Eulerian Path Algorithm
        def eulerian_path(graph,start):
            path = []
            stack = [start]

            while stack:
                v= stack[-1]
                if graph[v]:
                    stack.append(graph[v].pop(0))
                else:
                    path.append(stack.pop())

            path.reverse()

            return path

        return eulerian_path(adj,'JFK')

