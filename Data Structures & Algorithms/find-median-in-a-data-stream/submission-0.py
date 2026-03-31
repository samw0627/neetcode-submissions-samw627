class MedianFinder:

    def __init__(self):
        minHeap,maxHeap = [],[]
        heapq.heapify(minHeap)
        heapq.heapify_max(maxHeap)

        self.minHeap = minHeap
        self.maxHeap = maxHeap
                

    def addNum(self, num: int) -> None:
        #Push to minHeap
        if self.maxHeap and num < self.maxHeap[0]:
            heapq.heappush_max(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap,num)
        
        if len(self.maxHeap) - len(self.minHeap) > 1:
            elem = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, elem)
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            elem = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap,elem)
        

    def findMedian(self) -> float:
        #If the total number of elements is odd, then we take the top value of the maxHeap
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 1:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return self.maxHeap[0] 
        else:
            return (self.minHeap[0] + self.maxHeap[0]) / 2
        
        