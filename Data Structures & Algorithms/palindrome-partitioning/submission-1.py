class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(string):
            left = 0
            right = len(string)-1
            while left <= right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        final = []
        currSet = []
        def dfs(start):
            #Base Case: When we have partitioned all of the strings
            if start == len(s):
                final.append(currSet.copy())
                return
            
            for end in range(start,len(s)):
                if not isPalindrome(s[start:end+1]):
                    continue
                currSet.append(s[start:end+1])
                dfs(end+1)
                currSet.pop()
            
        dfs(0)
        return final
                

                

                

        
        