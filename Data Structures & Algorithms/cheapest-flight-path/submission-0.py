class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def build_graph(flights):
            adj = defaultdict(list)
            for u,v,w in flights:
                adj[u].append((v,w))
            return adj
        
        adj = build_graph(flights)

        def belleman_ford(adj,src,num_vertices):
            #Step 1: set every vertex distance to infinity
            dist = defaultdict(lambda: float("inf"))
            pred = defaultdict(lambda: None)
            dist[src] = 0

            #Step2: Relax all edges K-1 times

            for iteration in range(k+1):
                updated = False #early exit flag
                tmp_dist = dist.copy()
                for u in adj:
                    #skip vertices we haven't reached yet
                    if dist[u] == float("inf"):
                        continue
                    
                    for v,w in adj[u]:
                        #RELAXATION: can we reach v cheaper by going through u?
                        if dist[u] + w < tmp_dist[v]:
                            tmp_dist[v] = dist[u] + w
                            pred[v] = u
                            updated = True
                #Exit loop if no edge was relaxed
                dist = tmp_dist
                if not updated:
                    break

            return dist, pred
                
        prices, prev = belleman_ford(adj,src,n)
        cheapest = prices[dst]
        return cheapest if cheapest != float("inf") else -1


            
        