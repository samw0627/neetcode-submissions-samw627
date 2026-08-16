class Solution:
    def reorganizeString(self, s: str) -> str:
        #We will place the characters in the order of the number of characters it has in th string. 
        char_count = Counter(s)
        heap = []
        queue = deque()
        res = ""
        for c in char_count:
            heapq.heappush_max(heap,(char_count[c],c))
        print(heap)
        while heap:
            count,char = heapq.heappop_max(heap)
            res += char
            count -= 1
            if queue:
                nxt = queue.popleft()
                heapq.heappush_max(heap,nxt)
            if count != 0:
                queue.append((count,char))
        
        print(res)
        if len(queue) != 0:
            return ""
        else:
            return res

            



        
        