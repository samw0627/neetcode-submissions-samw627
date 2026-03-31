class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Max Heap based on the frequency of the of the task
        count = Counter(tasks)
        maxHeap = []
        timer = deque()
        time = 0

        for c in count:
            maxHeap.append(count[c])
        heapq.heapify_max(maxHeap)

        while maxHeap or timer:
            time += 1
            if maxHeap:
                count = heapq.heappop_max(maxHeap)
                count -= 1

                if count > 0:
                    timer.append((count,time + n))
                
            if timer and time== timer[0][1]:
                heapq.heappush_max(maxHeap,timer.popleft()[0])


        return time 




        


        

        