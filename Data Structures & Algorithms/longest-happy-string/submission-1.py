class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #Put the character in the queue if it has been used 2 times in a row
        heap = []
        if a != 0:
            heap.append((a,"a"))
        if b != 0:
            heap.append((b,"b"))
        if c != 0:
            heap.append((c,"c"))
        
        queue = deque()
        heapq.heapify_max(heap)
        res = ""
        lastChar = ""
        
        while heap:
            #Pop the heap
            count,char = heapq.heappop_max(heap)
            res +=char
            #Decrease the character count by 1
            count -= 1
            if queue:
                a,b= queue.popleft()
                heapq.heappush_max(heap,(a,b))

            #If the lastChar == currChar: Put chracter to queue
            if lastChar == char and count != 0:
                queue.append((count,char))
            elif count != 0:
                #Else Push back to the heap
                heapq.heappush_max(heap,(count,char))
            #Store lastChur = currChar
            lastChar = char
        
        return res

    



            





        
        
        

        