class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x:x[1])
        final = [intervals[0]]
        res = 0
        
        print(intervals)
        for i in intervals[1:]:
            if final[-1][1] > i[0]:
                res += 1
            else:
                final.append(i)
        
        return res





        