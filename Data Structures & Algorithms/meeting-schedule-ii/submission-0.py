"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #At each time frame, we count what is the maximum number of overlap
        time = []
        curr = res = 0
        for i in intervals:
            time.append((i.start,1))
            time.append((i.end,-1))
        
        time.sort(key=lambda x:(x[0],x[1]))

        for t in time:
            curr += t[1]
            res = max(res,curr)
        
        return res
        

        


        