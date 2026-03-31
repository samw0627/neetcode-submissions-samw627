class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        #[1,4],[4,6],[7,8],[10,10]
        car = []
        time = []
        stack = []
        for n in range(len(position)):
            car.append((position[n],speed[n]))
        #We sort the array based on position, since the car no car can go before the car in the last position
        car.sort(reverse=True)
        for t in range(len(car)):
            time.append((target-car[t][0])/car[t][1])
        #Car fleet will meet if the speed before is strictly smaller the current speed
        #We will try to maintain a monotonically increasing stack
        
        for i in range(len(time)):
            if not stack or time[i] > time[stack[-1]]:
                stack.append(i)
                
        return len(stack)