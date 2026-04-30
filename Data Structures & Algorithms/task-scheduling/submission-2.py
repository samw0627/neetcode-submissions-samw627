class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        q = deque()
        freq = Counter(tasks)
        for f in freq.values():
            heapq.heappush_max(maxHeap, f)
        timer = 0
        print(maxHeap)
        while maxHeap or q:
            #Increment the time
            timer += 1
            #Process the top element on the heap
            if maxHeap:
                quantity = heapq.heappop_max(maxHeap)
                quantity -= 1
                #Push the element to the queue
                if quantity > 0:
                    q.append((quantity,timer+n))
            
            #Pop the first element of the queue back to the heap
            if q and timer == q[0][1]:
                quantity,t = q.popleft()
                heapq.heappush_max(maxHeap,quantity)
        
        return timer
             




        