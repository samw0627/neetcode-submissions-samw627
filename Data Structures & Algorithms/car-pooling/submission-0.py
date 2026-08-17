class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #We will keep track of the net number of passengers
        #If at any point the number of people is bigger than capacity, it would not be possible to 
        time = []
        for cap,start,end in trips:
            time.append((start,cap))
            time.append((end,-cap))
        time.sort()
        
        curr = 0
        for t in time:
            curr += t[1]
            if curr > capacity:
                return False
        
        return True
