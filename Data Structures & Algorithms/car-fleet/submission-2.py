class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #If the time it takes to reach the end decreases, we will maintain the same speed as the slower car
        cars = []
        time = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(reverse=True)
        for s,v in cars:
            curr = (target-s)/v
            if time and time[-1] >= curr:
                continue
            time.append(curr)
        
        return len(time)



        
        


    

        



    

        