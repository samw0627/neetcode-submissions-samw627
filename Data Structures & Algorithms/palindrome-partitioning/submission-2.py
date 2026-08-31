class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        ans = []
        end = len(s)

        def dfs(i,curr):
            #Base Case, we reached the end of the list
            if i == end:
                ans.append(curr.copy())
                return
            #If this is a palindrome, we will add to the list
            for j in range(i+1,end+1):
                if isPalindrome(s[i:j]):
                    curr.append(s[i:j])
                    dfs(j,curr)
                    curr.pop()
        
        dfs(0,[])

        return ans


            

                
