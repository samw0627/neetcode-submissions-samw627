class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        def calculate(n):
            digits = [int(s) for s in str(n)]
            ans = 0
            for d in digits:
                #Sum the square of each digits
                ans += d**2
            if ans == 1:
                return True
            if ans in hashset:
                return False
            hashset.add(ans)
            print(hashset)
            return calculate(ans)
        
        return calculate(n)


            

        

        