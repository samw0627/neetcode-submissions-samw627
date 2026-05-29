class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #3 cases
        #Case 1: [1,3],[4,5] => [1,3],[4,5] No Overlap curr[1] < next[0]
        #Case 2: [1,3], [3,5] => [1,5] Overlapping curr[1] >= next[0]
        # Case 3:  [1,5], [2,3] => [1,5] Overlapping curr[1] > next[1]

        #Sort the intervals
        intervals.sort()
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            prev = res[-1]
            curr = intervals[i]
            if prev[1] >= curr[0]:
                #Perform Merge
                if prev[1] >= curr[1]:
                    continue
                else:
                    prev[1] = curr[1]
            else:
                res.append(intervals[i])

        return res