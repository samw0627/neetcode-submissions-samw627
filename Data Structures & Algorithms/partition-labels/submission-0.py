class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #xyxxyzbxzbbisl
        #x:[0,7]; y:[1,4]; z:[5,8]; b[6,10]; i[11,11]; s[12:12]; l[13:13]
        #Check whether there overlapping in intervals

        interval = defaultdict(int)
        for i, char in enumerate(s):
            interval[char] = i

        result = []
        partition_start = -1
        max_boundary = 0
        
        for i, char in enumerate(s):
            max_boundary = max(max_boundary,interval[char])
            if i == max_boundary:
                result.append(max_boundary-partition_start) #Close partition when currIndex = maxBoundary
                partition_start = max_boundary
        
        return result

            



        
        
        
        


        