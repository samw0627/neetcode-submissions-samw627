class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #For each entry in target, search of arrays that contain element in their position
        candidates = []
        
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                candidates.append(t)
        if not candidates:
            return False
        for i in range(len(target)):
            for j,c in enumerate(candidates):
                if c[i] == target[i]:
                    break
                if j == len(candidates)-1:
                    return False

        return True
        



        

        