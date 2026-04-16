class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])

    
        heap = []
        res = {}
        j = 0


        for q in sorted(queries):
            while j < len(intervals) and intervals[j][0] <= q:
                heapq.heappush(heap, (intervals[j][1]-intervals[j][0]+1, intervals[j][1]))
                j += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[q] = heap[0][0]
            else:
                res[q] = -1
        
        return [res[q] for q in queries]


                


        
        