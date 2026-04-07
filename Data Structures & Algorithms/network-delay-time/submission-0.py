class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Build Adjacency List
        def build_graph(edges):
            graph = defaultdict(list)
            for u,v,w in edges:
                graph[u].append((v,w))
            return graph
        
        adj = build_graph(times)

        def dijkstra(graph,start):
            dist = defaultdict(lambda: float('inf')) #Set initial dist to inf
            dist[start] = 0
            prev = {}

            heap = [(0,start)]

            while heap:
                cost,node = heapq.heappop(heap) #pop the heap

                #skip if we found a better path
                if cost > dist[node]:
                    continue

                for neigh, weight in graph[node]:
                    new_cost = cost + weight
                    if new_cost < dist[neigh]:
                        dist[neigh] = new_cost
                        prev[neigh] = node
                        heapq.heappush(heap,(new_cost,neigh))
                    
            return dict(dist),prev
        
        distances, prev = dijkstra(adj,k)

        if len(distances) == n:
            return max(distances.values())
        else:
            return -1







        

        