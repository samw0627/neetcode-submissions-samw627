class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Build a min heap, and pop 2 times to get the 2 closest points
        dist = []
        final = []
        for i in range(len(points)):
            d = (points[i][0]**2 + points[i][1]**2)**0.5
            dist.append((d, points[i]))

        heapq.heapify(dist)
        for j in range(k):
            final.append(heapq.heappop(dist)[1])
        
        return final