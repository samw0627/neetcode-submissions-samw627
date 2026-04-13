class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])

            if total < 0:
                res = i + 1
                total = 0
        
        return res
       
        
            


            

            #try the next candidate
        #Greedy Approach, always start at the gas station with the largest amount of gas


        