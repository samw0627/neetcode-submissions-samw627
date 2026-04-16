class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        queries_copy = [[queries[i],i] for i in range(len(queries))]
        queries_copy.sort()
        
        heap = []
        res = [-1]*len(queries)
        j = 0


        for q, i in queries_copy:
            while j < len(intervals) and intervals[j][0] <= q:
                heapq.heappush(heap, (intervals[j][1]-intervals[j][0]+1, intervals[j][1]))
                j += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                res[i] = heap[0][0]
            else:
                res[i] = -1
        
        return res


                


        
        