class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for curr in intervals[1:]:
            prev = res[-1]
            #If interval overlap, change bounds
            if prev[1] >= curr[0]:
                prev[1] = max(prev[1],curr[1])
            else:
                res.append(curr)
        return res





        