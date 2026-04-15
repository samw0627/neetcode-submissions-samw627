class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Overlap
        #b[0] <= a[1]
        if len(intervals) == 0:
            return [newInterval]
        #If Overlap
        #[1,4][2,5] => [min(a[0],b[0]), max(a[1],b[1])]
        #[1,3][2,100]       [4,6]


        # intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
        # Output: [[1,2],[3,5],[6,7],[9,10]]

        #Before: new[0] < i[0] and new[1] < i[0]
        #After: new[0] > i[1] and new[1] > i[1]
        #overlapping: i[0]< new[0] or i[1] > new[1]
        interval_added = False
        
        final = []
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            final.append(intervals[i])
            i += 1

        while i< len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
            i += 1
        
        final.append(newInterval)
        
        while i < len(intervals):
            final.append(intervals[i])
            i += 1

        return final
                
            

            

        
        
        
        