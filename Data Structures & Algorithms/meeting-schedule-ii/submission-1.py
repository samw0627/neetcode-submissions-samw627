"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #Line Sweep Algorithm
        #At each of the starting time, we will increase the room by 1
        #At each of the end time, we will decrease the room by 1
        #return the final count
        time = []
        res,curr = 0,0
        for i in intervals:
            time.append([i.start,1])
            time.append([i.end,-1])
        
        #Sort the list of time
        time.sort()

        for t in time:
            curr += t[1]
            res = max(res,curr)

        return res



        