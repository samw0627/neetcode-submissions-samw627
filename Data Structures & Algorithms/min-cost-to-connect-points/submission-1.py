class UnionFind:
    def __init__(self,n):
        self.paren = {}
        self.rank = {}

        for i in range(n):
            self.paren[i] = i
            self.rank[i] = 0
    
    def find (self,n):
        if n != self.paren[n]:
            self.paren[n] = self.find(self.paren[n]) #Path Compression
        return self.paren[n]
    
    def union(self,n1,n2):
        p1,p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.paren[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.paren[p1] = p2
        else:
            self.paren[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Build minimum spanning tree using Kruskal's algorithm
        #Calculate distance across each points
        minHeap= []
        indexToPoint = defaultdict(set)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist = abs(points[j][0]-points[i][0]) + abs(points[j][1]-points[i][1])
                heapq.heappush(minHeap,(dist,i,j))
        unionfind = UnionFind(len(points))
        mst = []
        total = 0

        while len(mst)< len(points) - 1:
            weight, n1,n2 = heapq.heappop(minHeap)
            if not unionfind.union(n1,n2):
                continue
            total += weight
            mst.append([n1,n2])
        
        return total
        
        




                





        