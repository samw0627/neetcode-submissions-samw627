class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #[2,-1,1,2] k = 2
        #[2,1,2,4]
        p = []
        total = 0
        res = 0
        prev = defaultdict(int)
        for n in nums:
            total += n
            p.append(total)
        
        #Two sum problem
        #prefix[j] + (- prefix[i]) = k
        prev[0] = 1
        for i in range(len(p)):
            diff = p[i] - k
            if diff in prev:
                res += prev[diff]
            prev[p[i]] += 1
            
        return res

           
            

            




            

        