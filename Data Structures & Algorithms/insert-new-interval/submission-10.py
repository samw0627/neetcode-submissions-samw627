class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Case 1: [1,3],[6,7] ; [4,5] => [1,3],[4,5],[6,7]
        #Case 2: [1,3],[6,7] ; [3,6] => [1,7]
        #Case 3: [1,3],[6,7] ; [2,5] => [1,5],[6,7]

        if len(intervals) == 0:
            return [newInterval]
        
        l = 0
        r = len(intervals)

        #Insert interval before merging
        while l < r:
            mid = (l+r)// 2
            #Insert interval new interval start is smaller than mid interval
            if intervals[mid][0] >= newInterval[0]:
                r = mid
            else:
                l = mid + 1
        intervals.insert(l,newInterval)
        #Merge Interval
        res = [intervals[0]]
        
        for curr in intervals[1:]:
            prev = res[-1]            
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1],curr[1])
            else:
                res.append(curr)
            #print(res)
                #[1,3],[2,4] => [1,4] [1,max(prev[1],curr[1])]
                #[1,4],[2,3] => [1,4]
        return res
                


                


                


        
        
        


        



        

        