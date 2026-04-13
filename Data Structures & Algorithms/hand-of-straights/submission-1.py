class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)
        heap = list(set(hand))
        heapq.heapify(heap)

        while heap:
            val = heap[0] #Peek the fist element
            #Form groups
            count = 0
            while count != groupSize:
                if val not in freq:
                    return False
                freq[val] -= 1
                if freq[val] == 0:
                    del freq[val]
                val += 1
                count +=1
            # Need to sync elements that are not in the heap
            while heap and heap[0] not in freq:
                heapq.heappop(heap)

        return True
            




        
            

            



        



        
        