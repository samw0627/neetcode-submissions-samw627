class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #[5,1,4,2]
        #[1,3,2,3,2] 
        #[1,2,2,3,3]
        #[1,2,4,5]

        people.sort()
        l,r = 0,len(people) - 1
        res = 0

        while l <= r:
            if people[l] + people[r] > limit :
                #Move the pointer with the biggest value
                r -= 1
            else:
                r-= 1
                l += 1
            res += 1

        return res 



        