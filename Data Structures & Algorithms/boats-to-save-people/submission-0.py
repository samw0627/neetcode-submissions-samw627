class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #Sort the List
        #[1,3,2,3,2]
        #[1,2,2,3,3]
        #Target = 3


        #left + right > limit. => count+ 1, right - 1
        #left + right <= limit  => count + 1, left + 1; right - 1
        #if left == right: count + 1


        people.sort()
        left = 0
        right = len(people) - 1
        count = 0

        while left <= right:
            if left == right:
                count += 1
                left += 1
                right -= 1
                continue

            if people[left] + people[right] > limit:
                count += 1
                right -= 1
            
            else:
                count += 1
                left += 1
                right -= 1
            
        return count





        