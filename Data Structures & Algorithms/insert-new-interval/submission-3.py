class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Insert the new Interval in the sorted interval list through Binary Search
        if len(intervals) == 0:
            return [newInterval]

        l = 0
        r= len(intervals) - 1
        
        while l < r:
            mid = (l+r+1) // 2
            if intervals[mid][0] <= newInterval[0]:
                #Search on the left hand side
                l = mid
            else:
                r = mid-1
        
        #Insert Interval
        if intervals[l][0] >= newInterval[0]:
            intervals.insert(l,newInterval)
        else:
            intervals.insert(l+1, newInterval)
        
        #Merge Intervals
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            prev = res[-1]
            curr = intervals[i]

            if prev[1] >= curr[0]:
                #Merge
                prev[1] = max(prev[1],curr[1])
            else:
                res.append(curr)
            
        return res

            



        