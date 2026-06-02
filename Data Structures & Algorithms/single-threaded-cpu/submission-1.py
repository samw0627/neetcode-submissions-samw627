class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        heap = []
        for i, task in enumerate(tasks):
            task.append(i)

        heapq.heapify(tasks)
        res = []
        currProcessEnd = -1
        nextStart = -1
        processing = False

        while heap or tasks:
            if time == currProcessEnd:
                processing = False
            
            #Queue the task at a certain time
            while tasks and time >= tasks[0][0]:
                start,process,idx = heapq.heappop(tasks)
                heapq.heappush(heap,[process,idx,start])
            #Update the latest processing time if CPU is idle
            if heap and not processing:
                process,idx,start = heapq.heappop(heap)
                nextStart = start
                processing = True
                currProcessEnd = time + process
                res.append(idx)
            
            #Set time to the next available time
            if processing == True:
                time = currProcessEnd
            if processing == False and not heap:
                time = tasks[0][0]



        return res
        