class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        final = [intervals[0]]

        if len(intervals) == 1:
            return final
        
        print(intervals)
        for i in intervals[1:]:
            if final[-1][1] >= i[0]:
                final[-1][1] = max(i[1],final[-1][1])
            else:
                final.append(i)
        return final

        
        


        

            



        

        

        